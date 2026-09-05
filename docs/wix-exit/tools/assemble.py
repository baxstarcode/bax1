"""Assemble the Wix exit inventory into bax1/docs/wix-exit/.

Everything here is captured read-only from the live site. The point is that
nothing about baxstarfishing.com lives ONLY inside Wix any more.
"""
import json, os, shutil, glob, csv, re, datetime

S = "/tmp/claude-0/-home-user-bax1/0bd83c40-b201-5abf-b16e-cf7f06e4bb0c/scratchpad"
OUT = "/home/user/bax1/docs/wix-exit"
for d in ("pages", "seo", "embeds", "embeds/not-in-repo", "blog", "tools"):
    os.makedirs(os.path.join(OUT, d), exist_ok=True)

# ---- page content -------------------------------------------------------
n_pages = 0
for f in glob.glob(os.path.join(S, "wix_pages", "*.json")):
    b = os.path.basename(f)
    if b == "_index.json" or not b.startswith("_"):
        shutil.copy(f, os.path.join(OUT, "pages", b))
        n_pages += 1
    elif b == "_masterPage.json":
        shutil.copy(f, os.path.join(OUT, "pages", b))

# ---- seo ----------------------------------------------------------------
for src, dst in (("seo_pages.json", "pages.json"), ("seo_blog.json", "blog-posts.json")):
    p = os.path.join(S, src)
    if os.path.exists(p):
        shutil.copy(p, os.path.join(OUT, "seo", dst))

# ---- embeds -------------------------------------------------------------
emap = json.load(open(os.path.join(S, "embed_map.json")))
shutil.copy(os.path.join(S, "embed_map.json"), os.path.join(OUT, "embeds", "embed-map.json"))

# preserve every embed that has NO source file in the repo
import urllib.request
UA = {"User-Agent": "Mozilla/5.0"}
saved = []
for r in emap:
    if r.get("match") or r.get("error"):
        continue
    name = r["embedUrl"].rsplit("/", 1)[-1]
    dest = os.path.join(OUT, "embeds", "not-in-repo", name)
    if not os.path.exists(dest):
        try:
            c = urllib.request.urlopen(urllib.request.Request(r["embedUrl"], headers=UA), timeout=60).read()
            open(dest, "wb").write(c)
        except Exception as e:
            print("  save failed", name, str(e)[:60]); continue
    saved.append({"file": name, "page": r["page"], "bytes": r.get("liveBytes")})
json.dump(saved, open(os.path.join(OUT, "embeds", "not-in-repo", "_manifest.json"), "w"), indent=1)

# ---- blog ---------------------------------------------------------------
p = os.path.join(S, "blog", "posts_meta.json")
if os.path.exists(p):
    shutil.copy(p, os.path.join(OUT, "blog", "posts-meta-partial.json"))

# ---- redirect map -------------------------------------------------------
rows = []
seo_pages = json.load(open(os.path.join(S, "seo_pages.json")))
for r in seo_pages:
    path = "/" + r["url"].split("baxstarfishing.com/", 1)[-1].rstrip("/") if "baxstarfishing.com/" in r["url"] else "/"
    rows.append({"type": "page", "live_url": r["url"], "path": path,
                 "title": (r.get("title") or "").replace("\n", " "),
                 "new_path": "", "notes": ""})
bp = os.path.join(S, "seo_blog.json")
if os.path.exists(bp):
    for r in json.load(open(bp)):
        path = "/" + r["url"].split("baxstarfishing.com/", 1)[-1]
        rows.append({"type": "blog_post", "live_url": r["url"], "path": path,
                     "title": (r.get("title") or "").replace("\n", " "),
                     "new_path": "", "notes": ""})
with open(os.path.join(OUT, "redirect-map.csv"), "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=["type", "live_url", "path", "title", "new_path", "notes"])
    w.writeheader(); w.writerows(rows)

# ---- tools --------------------------------------------------------------
for t in ("wix_extract.py", "seo_heads.py", "match_embeds.py", "assemble.py"):
    shutil.copy(os.path.join(S, t), os.path.join(OUT, "tools", t))
for t in ("pagesMap.json", "embeds_by_page.json"):
    shutil.copy(os.path.join(S, t), os.path.join(OUT, "tools", t))

print(f"pages: {n_pages} | redirect rows: {len(rows)} | embeds preserved: {len(saved)}")
