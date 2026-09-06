"""Fetch the SSR <head> of every live URL: title, description, canonical,
robots, OG/Twitter, JSON-LD, and any custom head code Wix injects.
Wix server-renders the head even though it client-renders the body, so this
is a faithful capture of what search engines currently see."""
import json, re, sys, os, html
from concurrent.futures import ThreadPoolExecutor
import urllib.request

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/140.0 Safari/537.36"


import time, random

def get(url, tries=5):
    last = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=90) as r:
                return r.status, r.read().decode("utf-8", "replace"), r.geturl()
        except urllib.error.HTTPError as e:
            last = e
            if e.code in (429, 503):
                time.sleep((2 ** i) * 3 + random.random() * 2)
                continue
            raise
        except Exception as e:
            last = e
            time.sleep(2 + i)
    raise last


def head_of(h):
    i = h.lower().find("</head>")
    return h[: i + 7] if i > 0 else h[:400000]


def parse(url):
    rec = {"url": url}
    try:
        st, body, final = get(url)
        rec["status"], rec["finalUrl"] = st, final
        hd = head_of(body)
        t = re.search(r"<title[^>]*>(.*?)</title>", hd, re.S | re.I)
        rec["title"] = html.unescape(t.group(1).strip()) if t else None
        metas = {}
        for m in re.finditer(r'<meta\s+[^>]*?(?:name|property)="([^"]+)"[^>]*?content="([^"]*)"', hd, re.I):
            metas[m.group(1)] = html.unescape(m.group(2))
        for m in re.finditer(r'<meta\s+[^>]*?content="([^"]*)"[^>]*?(?:name|property)="([^"]+)"', hd, re.I):
            metas.setdefault(m.group(2), html.unescape(m.group(1)))
        rec["meta"] = {k: v for k, v in metas.items()
                       if k in ("description", "robots", "keywords", "og:title", "og:description",
                                "og:image", "og:url", "og:type", "twitter:card", "twitter:title",
                                "twitter:description", "twitter:image")}
        c = re.search(r'<link[^>]+rel="canonical"[^>]+href="([^"]+)"', hd, re.I)
        rec["canonical"] = html.unescape(c.group(1)) if c else None
        rec["jsonld"] = [s.strip() for s in
                         re.findall(r'<script type="application/ld\+json">(.*?)</script>', hd, re.S)]
        # custom head code Brady installed through Wix Custom Code
        ce = re.search(r'<script id="pageHtmlEmbeds\.head start">.*?</script>(.*?)<script id="pageHtmlEmbeds\.head end">',
                       body, re.S)
        rec["customHeadCode"] = (ce.group(1).strip()[:20000] or None) if ce else None
        # iframe embeds referenced anywhere in the document
        rec["embedUrls"] = sorted(set(re.findall(r'https://[a-z0-9\-]*\.?filesusr\.com/html/[^"\'\\\s]+', body)))
        rec["htmlBytes"] = len(body)
    except Exception as e:
        rec["error"] = str(e)[:200]
    return rec


if __name__ == "__main__":
    urls = [u.strip() for u in open(sys.argv[1]) if u.strip()]
    out = sys.argv[2]
    recs = []
    prev = json.load(open(out)) if os.path.exists(out) else []
    done = {r["url"]: r for r in prev if not r.get("error")}
    for i, u in enumerate(urls):
        if u in done:
            recs.append(done[u]); continue
        recs.append(parse(u))
        time.sleep(2.2)
        if (i + 1) % 10 == 0:
            print(f"  {i+1}/{len(urls)}", flush=True)
    recs.sort(key=lambda r: r["url"])
    json.dump(recs, open(out, "w"), indent=1)
    ok = sum(1 for r in recs if not r.get("error"))
    print(f"fetched {ok}/{len(recs)} | with description: {sum(1 for r in recs if r.get('meta',{}).get('description'))}"
          f" | with jsonld: {sum(1 for r in recs if r.get('jsonld'))}"
          f" | with custom head: {sum(1 for r in recs if r.get('customHeadCode'))}")
    for r in recs:
        if r.get("error"):
            print("  ERR", r["url"], r["error"][:80])
