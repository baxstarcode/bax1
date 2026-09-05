"""Extract a readable content inventory from Wix page-JSON files.

Wix stores each page as structure (component tree, gives ORDER) + data
(document_data, gives the actual text/images/links). This walks the tree in
render order and emits plain, migration-ready content per page.
Read-only: fetches published JSON over HTTPS, writes local files only.
"""
import json, re, sys, os, html, urllib.request, urllib.error

BASE = "https://static.wixstatic.com/sites/{}.json.z"
TAGS = re.compile(r"<[^>]+>")


def fetch(name, cache_dir):
    os.makedirs(cache_dir, exist_ok=True)
    p = os.path.join(cache_dir, name + ".json")
    if os.path.exists(p) and os.path.getsize(p) > 200:
        return json.load(open(p))
    req = urllib.request.Request(BASE.format(name), headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=90) as r:
        raw = r.read()
    open(p, "wb").write(raw)
    return json.loads(raw)


def clean(h):
    if not h:
        return ""
    h = re.sub(r"<br\s*/?>", "\n", h, flags=re.I)
    h = re.sub(r"</(p|h[1-6]|li|div)>", "\n", h, flags=re.I)
    t = html.unescape(TAGS.sub("", h))
    return re.sub(r"[ \t]+", " ", t).strip()


def heading_level(h):
    m = re.search(r"<h([1-6])", h or "", re.I)
    return "H" + m.group(1) if m else None


def extract(pj):
    """Walk the component tree in order, resolving each component's data."""
    dd = pj.get("data", {}).get("document_data", {})
    out = []

    def resolve(q):
        return dd.get((q or "").lstrip("#"), {}) if q else {}

    def walk(comp, depth=0):
        if not isinstance(comp, dict):
            return
        ctype = comp.get("componentType", "") or comp.get("type", "")
        d = resolve(comp.get("dataQuery"))
        dtype = d.get("type", "")
        rec = None

        if dtype == "StyledText":
            txt = clean(d.get("text"))
            if txt:
                rec = {"kind": "text", "level": heading_level(d.get("text")), "text": txt}
        elif dtype == "Image":
            rec = {"kind": "image", "uri": d.get("uri"), "alt": d.get("alt") or "",
                   "title": d.get("title") or "", "w": d.get("width"), "h": d.get("height")}
        elif dtype in ("LinkableButton", "SiteButton"):
            lk = resolve(d.get("link"))
            rec = {"kind": "button", "label": clean(d.get("label")),
                   "href": lk.get("url") or lk.get("pageId") or None,
                   "target": lk.get("target")}
        elif dtype == "HtmlComponent" or ctype.endswith("HtmlComponent"):
            rec = {"kind": "embed_html", "url": d.get("url"), "srcType": d.get("sourceType"),
                   "title": d.get("title")}
        elif dtype in ("Video", "WixVideo"):
            rec = {"kind": "video", "uri": d.get("videoId") or d.get("uri"), "title": d.get("title")}
        elif dtype == "AppPage" or ctype.endswith("TPAWidget") or ctype.endswith("TPASection"):
            rec = {"kind": "wix_app", "appId": d.get("appDefinitionId") or comp.get("data"),
                   "widget": d.get("appPageId") or comp.get("id")}
        elif ctype.endswith("FormContainer") or dtype == "FormContainer":
            rec = {"kind": "form", "id": comp.get("id")}
        elif dtype in ("LinkList", "AnchorLink", "ExternalLink", "PageLink"):
            rec = {"kind": "link", "href": d.get("url") or d.get("pageId"), "target": d.get("target")}

        if rec:
            rec["compId"] = comp.get("id")
            rec["depth"] = depth
            out.append(rec)

        for key in ("components", "children"):
            for c in comp.get(key, []) or []:
                walk(c, depth + 1)

    walk(pj.get("structure", {}))
    return out


def summarize(pj, blocks):
    heads = [b for b in blocks if b["kind"] == "text" and b.get("level")]
    return {
        "title": pj.get("title"),
        "slug": pj.get("pageUriSEO"),
        "counts": {k: sum(1 for b in blocks if b["kind"] == k)
                   for k in sorted({b["kind"] for b in blocks})},
        "headings": [{"level": h["level"], "text": h["text"][:120]} for h in heads][:40],
    }


if __name__ == "__main__":
    pmap = json.load(open(sys.argv[1]))
    outdir = sys.argv[2]
    cache = os.path.join(outdir, "_raw")
    os.makedirs(outdir, exist_ok=True)
    index = []
    for pid, meta in sorted(pmap.items(), key=lambda kv: kv[1].get("pageUriSEO") or ""):
        fn = meta.get("pageJsonFileName")
        slug = meta.get("pageUriSEO") or pid
        if not fn:
            index.append({"pageId": pid, "slug": slug, "title": meta.get("title"),
                          "note": "no page JSON (app/system page)"})
            continue
        try:
            pj = fetch(fn, cache)
            blocks = extract(pj)
            rec = {"pageId": pid, "slug": slug, "title": pj.get("title") or meta.get("title"),
                   "jsonFile": fn, "blocks": blocks}
            json.dump(rec, open(os.path.join(outdir, slug.replace("/", "__") + ".json"), "w"), indent=1)
            s = summarize(pj, blocks)
            s.update({"pageId": pid, "blocks": len(blocks)})
            index.append(s)
            print(f"  {slug[:44]:46s} {len(blocks):4d} blocks  {s['counts']}")
        except Exception as e:
            index.append({"pageId": pid, "slug": slug, "error": str(e)[:200]})
            print(f"  {slug[:44]:46s} ERROR {str(e)[:80]}")
    json.dump(index, open(os.path.join(outdir, "_index.json"), "w"), indent=1)
    print("pages processed:", len(index))
