"""Fetch each live Wix HTML embed and match it to its source file in bax1.

The Wix embed is the DEPLOY TARGET; the repo file is the source. Nothing has
recorded which repo file is pasted into which page — this rebuilds that map by
comparing the live embed bytes against every candidate HTML file in the repo.
"""
import json, os, re, sys, time, hashlib, difflib
import urllib.request

BASE = "https://www-baxstarfishing-com.filesusr.com/"
REPO = "/home/user/bax1"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/140.0"


def norm(s):
    """Collapse whitespace so formatting drift doesn't hide a real match."""
    return re.sub(r"\s+", " ", s).strip()


def fingerprint(s):
    """Signals that survive edits: title, h1/h2 text, and distinctive ids."""
    t = re.search(r"<title[^>]*>(.*?)</title>", s, re.S | re.I)
    heads = re.findall(r"<h[12][^>]*>(.*?)</h[12]>", s, re.S | re.I)[:6]
    ids = set(re.findall(r'id="([a-zA-Z][\w\-]{3,30})"', s))
    return {
        "title": norm(re.sub(r"<[^>]+>", "", t.group(1))) if t else None,
        "heads": [norm(re.sub(r"<[^>]+>", "", h))[:60] for h in heads],
        "ids": ids,
    }


def score(live, cand):
    # full-text similarity dominates: an embed pasted from the repo is usually
    # byte-identical or very close, even when it has no headings or ids
    full = difflib.SequenceMatcher(None, norm(live), norm(cand)).quick_ratio()
    if full > 0.90:
        full = difflib.SequenceMatcher(None, norm(live), norm(cand)).ratio()
    if full >= 0.85:
        return round(full, 3)
    a, b = fingerprint(live), fingerprint(cand)
    s = 0.0
    if a["title"] and b["title"]:
        s += 0.35 * difflib.SequenceMatcher(None, a["title"], b["title"]).ratio()
    if a["ids"] or b["ids"]:
        inter = len(a["ids"] & b["ids"])
        union = len(a["ids"] | b["ids"]) or 1
        s += 0.40 * (inter / union)
    if a["heads"] and b["heads"]:
        s += 0.25 * difflib.SequenceMatcher(None, " ".join(a["heads"]), " ".join(b["heads"])).ratio()
    return round(s, 3)


def fetch(url, tries=4):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read().decode("utf-8", "replace")
        except Exception as e:
            if i == tries - 1:
                raise
            time.sleep(2 ** i * 2)


if __name__ == "__main__":
    by_page = json.load(open(sys.argv[1]))
    out_path = sys.argv[2]
    cands = {}
    for root, _, files in os.walk(REPO):
        if "/.git" in root:
            continue
        for f in files:
            if f.endswith(".html") or f in ("baxstar_homepage_final", "blank", "open-water/where_we_fish"):
                p = os.path.join(root, f)
                try:
                    cands[os.path.relpath(p, REPO)] = open(p, encoding="utf-8", errors="replace").read()
                except Exception:
                    pass
    print(f"repo candidates: {len(cands)}")

    seen, results = {}, []
    for page, urls in sorted(by_page.items()):
        for rel in urls:
            full = BASE + rel.lstrip("/")
            if full in seen:
                live = seen[full]
            else:
                try:
                    live = fetch(full)
                except Exception as e:
                    results.append({"page": page, "embedUrl": full, "error": str(e)[:120]})
                    print(f"  {page:38s} FETCH ERROR {str(e)[:60]}")
                    continue
                seen[full] = live
                time.sleep(1.0)
            ranked = sorted(((score(live, c), n) for n, c in cands.items()), reverse=True)[:3]
            best_score, best_name = ranked[0]
            t = fingerprint(live)["title"]
            results.append({
                "page": page, "embedUrl": full,
                "liveTitle": t, "liveBytes": len(live),
                "liveSha256": hashlib.sha256(live.encode()).hexdigest()[:16],
                "match": best_name if best_score >= 0.45 else None,
                "matchScore": best_score,
                "runnersUp": [{"file": n, "score": s} for s, n in ranked[1:]],
            })
            flag = "" if best_score >= 0.45 else "  <-- NO CONFIDENT MATCH"
            print(f"  {page:38s} {best_score:.2f}  {best_name[:46]:48s}{flag}")
    json.dump(results, open(out_path, "w"), indent=1)
    matched = sum(1 for r in results if r.get("match"))
    print(f"embeds: {len(results)} | matched to a repo file: {matched}")
