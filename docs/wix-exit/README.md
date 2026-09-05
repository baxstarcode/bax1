# Wix Exit Inventory

Everything about **baxstarfishing.com** that currently exists *only* inside Wix,
captured to this repo so a migration is a rebuild from files rather than an
archaeology project.

**Captured:** 2026-09-04 · read-only · nothing on the live site was changed.

This is an inventory, not a migration. No cutover decision is implied — see
`INVENTORY.md` for the timing recommendation and the blockers.

---

## What's here

| Path | What it is |
|---|---|
| `INVENTORY.md` | **Read this first.** Findings, gaps, and what a migration would take. |
| `redirect-map.csv` | Every live URL with a blank `new_path` column to fill in. This is the 301 map. |
| `pages/` | One JSON per Wix page: every heading, paragraph, button, and image **in render order**. |
| `pages/_index.json` | Page-by-page summary: block counts and heading outline. |
| `pages/_masterPage.json` | Site nav tree (63 items, with hierarchy) and footer. |
| `seo/pages.json` | Per-page title, meta description, canonical, robots, OG/Twitter, JSON-LD. |
| `seo/blog-posts.json` | The same for every blog post. |
| `embeds/embed-map.json` | Which repo file is pasted into which Wix page, with live hashes. |
| `embeds/not-in-repo/` | **The embeds that existed nowhere but Wix.** Now preserved here. |
| `blog/` | Blog post metadata from the Wix Blog API. |
| `tools/` | The scripts that produced all of the above, so this can be re-run. |

## How it was captured

Wix serves this site as a client-rendered Thunderbolt app: the HTML a crawler
receives contains only the nav and the H1. The real page content lives in
per-page JSON files. The capture works like this:

1. `tools/pagesMap.json` — the page map lifted from the live homepage HTML,
   giving every page's ID, slug, and data-file name.
2. `tools/wix_extract.py` — fetches each page's JSON from
   `static.wixstatic.com/sites/<pageJsonFileName>.json.z` and walks the
   component tree in render order, resolving each component to its text,
   image, button, or embed.
3. `tools/seo_heads.py` — fetches every public URL and parses the
   server-rendered `<head>`, which *is* accurate (Wix SSRs the SEO tags even
   though it client-renders the body).
4. `tools/match_embeds.py` — fetches each live `filesusr.com` embed and scores
   it against every HTML file in this repo to rebuild the file → page map.

## Re-running it

```bash
cd docs/wix-exit/tools
python3 wix_extract.py pagesMap.json ../pages          # page content
python3 seo_heads.py urls.txt ../seo/pages.json        # SEO heads
python3 match_embeds.py embeds_by_page.json ../embeds/embed-map.json
```

`pagesMap.json` goes stale when pages are added or renamed. Refresh it by
pulling `"pagesMap":{...}` out of the live homepage HTML.

Wix rate-limits at roughly 1 request/second; the scripts back off on 429 and
resume from what they already have.
