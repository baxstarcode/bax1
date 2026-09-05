# baxstarfishing.com — Wix Exit Inventory

**Captured 2026-09-04, read-only. Nothing on the live site was changed.**

## BLUF

The site is 26 public pages and 136 blog posts. The custom section embeds —
the expensive part — were already versioned in this repo and are **byte-identical
to what is live**, so nothing has drifted. The migration gap was never the
embeds; it is the Wix-native layer around them, which this inventory now
captures. Two things found here need attention regardless of when a cutover
happens: **six embeds existed nowhere but inside Wix** — all one-liners, but
five carry live FareHarbor booking IDs (now preserved in
`embeds/not-in-repo/`) — and **the homepage still lives at the legacy slug
`/bradybaxter`**.

Timing: **park the cutover until the open-water season ends.** DNS and email are
both hosted at Wix, which makes email the first domino, not the pages.

---

## 1. What is live

| | Count | Source |
|---|---|---|
| Public pages | 26 | `pages-sitemap.xml` |
| Blog posts | 136 | `blog-posts-sitemap.xml` |
| Pages in the Wix page map | 60 | includes system/app pages (cart, checkout, profile, popups) |
| Pages with real captured content | 40 | `pages/_index.json` |
| Text blocks captured | 390 | headings + body copy, in render order |
| Images referenced | 94 | with alt text where set |
| Nav items | 63 | `pages/_masterPage.json`, hierarchy preserved |
| HTML embed instances | 24 | across 11 pages |

## 2. The embeds — file → page map

There are 24 embed instances using 22 distinct embed files. **17 instances (16
distinct repo files) match at a similarity of 0.99–1.00 — byte-identical.** The
Baxstar Sync workflow has been keeping repo and live in step; there is no drift
to reconcile anywhere on the site.

**Homepage (`/bradybaxter`) — 12 embeds, in page order:**
`baxstar_hero_video_banner.html` · `baxstar_guide.html` ·
`baxstar_experiences.html` · `baxstar_fish_gallery.html` ·
`baxstar_testimonials.html` · `baxstar_whats_included.html` ·
`baxstar_where_we_fish_short.html` · `baxstar_pricing.html` ·
`baxstar_faq_light.html` · `baxstar_CTA.html` (the "KNOW WHEN TO BOOK" section) ·
`baxstar_press_strip.html` · plus the boat-teaser iframe (below).

**Other pages:** `/fishing-trips` → `baxstar_hero_video_banner_fishing_trips.html`,
`baxstar_experiences_fishing_trips.html`, `baxstar_CTA.html` ·
`/about` → `about_your_guide_full.html` · `/faq` → `baxstar_faq.html` ·
`/terms` → `baxstar_terms.html`.

Full detail with hashes: `embeds/embed-map.json`.

## 3. Findings that need action

### 3.1 Six embeds existed only inside Wix — now preserved

These had no source file anywhere in the repo. All six are one-liners, saved
verbatim in `embeds/not-in-repo/`. **Five carry live FareHarbor booking IDs**,
which is revenue-critical to carry across:

| Page | What it is | Detail |
|---|---|---|
| `/ice-castle-range-runner` | FareHarbor calendar | item 422226, flow 1375094 |
| `/ice-castle-trophy-hunter` | FareHarbor calendar | item 422226 + `ref=Trophy Hunter Web Calendar` |
| `/17-hybrid-ii-ice-castle-detroit-lakes` **and** `/17-lake-of-the-woods-edition` | FareHarbor calendar (same file on both) | item 681248, flow 1375094 |
| `/17-ice-castle-luxury-rv-edition-rental` | FareHarbor calendar | item 681247, flow 1375094 |
| `/21-ice-castle-rental` | FareHarbor calendar | item 593973, flow 1375094 |
| `/bradybaxter` (homepage) | Boat teaser iframe | points at `boat.baxstarfishing.com/teaser.html` (repo `baxstar-vexus`) |

Note the ice-castle calendars use **flow 1375094**, which is a different flow
from the fishing CTAs' `flow=576827`. Both are live and both must survive.

Two things worth flagging: `/17-lake-of-the-woods-edition` and
`/17-hybrid-ii-ice-castle-detroit-lakes` share the *same* FareHarbor calendar
(item 681248) — verify that is intentional, since they are sold as different
units. And `/ice-castle-trophy-hunter` and `/ice-castle-range-runner` both
point at item 422226, differing only by a `ref` tracking parameter.

### 3.2 The homepage is still at `/bradybaxter`

`mainPageId` resolves to the page whose slug is `bradybaxter` — a leftover from
when this was the classroom tech blog. It works because Wix serves it at `/`,
but it shows up in the nav data ("Home" and "Rates" both point at
`/bradybaxter`) and it is the kind of thing that breaks in a migration. Fixing
this in Wix now would need a 301; on a rebuilt site it simply becomes `/`.

### 3.3 SEO gaps to fix before or during a move

- **4 pages have no meta description:** `/basstomouth`, `/inquiry-services-page`,
  `/jandk`, `/muscatell`.
- **13 of 26 pages carry JSON-LD**, matching the schema blocks in `seo/schema/`.
  The other 13 have none.
- No page is set to `noindex` — the whole site is indexable, so every URL needs
  a redirect.
- No page-level custom head code was detected, so the JSON-LD is coming from the
  installed schema blocks rather than per-page snippets.

### 3.4 Wix apps in use — these do not migrate as files

Identified by app ID and corroborated by the pages they sit on:

| App | Pages |
|---|---|
| Pro Gallery (13 instances) | `ice-castle-rentals`, `ice-house-rentals`, `guided-ice-fishing`, `basstomouth`, `icecastlerental`, `portableicehouse`, and others |
| Wix Blog | `detroitlakesfishingreport` (+ 136 posts) |
| Wix Stores | `shop` |
| Wix Bookings | `booking` |
| Members Area / Followers | `profile-1`, `followers` |

Each of these is a replacement decision, not a copy job. The blog is the big
one — 136 posts of genuine SEO value.

### 3.5 Wix native forms

Seven pages carry a Wix form: `21-ice-castle-rental`,
`fishing-consultations`, `ice-castle-rentals`, `ice-house-rentals`,
`ice-house-services`, and two `copy-of-ice-services-and-rates` duplicates.
Form submissions currently land in the Wix dashboard; a rebuilt site needs a
new destination for them.

### 3.6 Housekeeping visible in the page map

Duplicate/stale pages that should not be carried across: `copy-of-ice-services-and-rates`,
`copy-2-of-ice-services-and-rates`, `general-1`, `blank`, `buymyboat`.

## 4. What a migration actually takes

**Already solved (in this repo):** all 17 section embeds, the boat page
(separate repo, already on GitHub Pages), the JSON-LD schema blocks, and now
every page's native copy, nav, SEO fields, and orphan embeds.

**Still to decide:**

1. **Email first.** DNS *and* email are hosted at Wix (confirmed by Brady,
   2026-09-04). Moving the domain while mail is Wix-routed risks bookings and
   inbox at once. Move email to a dedicated host, verify it for a week, then
   touch DNS. There is a parked TODO doc for the same problem on
   BradyBaxter.com — solve both together.
2. **The blog.** 136 posts. Either keep the blog on Wix behind a subdomain, or
   export and rebuild. This is the single largest content decision.
3. **Wix apps.** Gallery, Stores, Bookings, Members each need a replacement or
   a decision to drop.
4. **Forms.** Pick a destination (email, a Worker, or a form service).
5. **Redirects.** `redirect-map.csv` has all 162 URLs with a blank `new_path`
   column. Every one needs a 301.

**Recommended window:** the lull between open-water and ice bookings. Do the
email move first, then DNS, then the site — never the same week.

## 5. Known limits of this capture

- Blog post *bodies* are not captured here — only titles, URLs, dates, and SEO
  fields. Wix's API truncates bulk content responses; a full post export is a
  separate step.
- Two pages (`/21-ice-castle-rental`, `/team-1`) hit Wix rate limits during the
  SEO pass. Their content is captured in `pages/`; re-run `seo_heads.py` to
  fill in their head tags.
- Visual design (fonts, colors, spacing) is not captured. The embeds carry
  their own styling; the Wix-native sections would be restyled in a rebuild.
- This is a point-in-time snapshot. Re-run the tools before any cutover.
