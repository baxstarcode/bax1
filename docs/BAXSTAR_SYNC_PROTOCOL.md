# BAXSTAR SYNC — Master Protocol v1.1
*Say "baxstar sync" — Claude executes this entire sequence automatically.*

---

## Trigger Phrase
> **"baxstar sync"**

---

## What Claude Executes (in order)

### Step 1 — Pull GitHub
Fetch every `baxstar_*.html` file from `baxstarcode/bax1`.
Raw URL: `https://raw.githubusercontent.com/baxstarcode/bax1/refs/heads/main/[filename]`

### Step 2 — Diff Against Project Files
Compare each file against `/mnt/project/`. Report what changed, skip identicals.

### Step 3 — Sync Project Files
Copy changed files to `/home/claude/`, apply upgrades, write to `/mnt/user-data/outputs/`.

### Step 4 — Push to GitHub
Commit updated files with message: `"Baxstar sync — [date] — [changed files]"`

### Step 5 — Update Wix via Chrome
Open each changed embed block in Wix editor and paste updated code.

**Section mapping:**
| File | Wix Section Name |
|---|---|
| baxstar_fish_gallery.html | Gallery Embed |
| baxstar_hero_banner.html | baxstar_hero |
| baxstar_scrolling_banner.html | Ticker Embed |
| baxstar_pricing__1_.html | Pricing Embed |
| baxstar_testimonials.html | Testimonials Embed |
| baxstar_how_it_works.html | baxstar_how_it_works |
| baxstar_guide.html | Guide Embed |
| baxstar_press_strip.html | Press Embed |
| baxstar_whats_included.html | Included Embed |
| baxstar_intro.html | Intro Embed |

### Step 6 — Send Publish Notification Email
After Wix is updated, Claude sends an email via Gmail:

**To:** brady@baxstarfishing.com
**Subject:** Baxstar Site Updated — Ready to Publish

**Body includes:**
- List of every section updated (by name)
- One-line summary of what changed in each (e.g. "Gallery: portrait carousel rebuilt")
- Direct link to Wix editor: https://manage.wix.com
- Reminder: nothing goes live until you hit Publish

### Step 7 — Confirm in Chat
- Files synced
- GitHub updated
- Wix sections updated
- Publish email sent to brady@baxstarfishing.com
- Any sections needing manual attention flagged

---

## Status
- [x] GitHub PAT active (bax1, Contents + Workflow R/W)
- [x] Wix section names confirmed
- [x] Baxstar Sync bookmark on Chrome bookmark bar
- [x] Gmail notification step added
- [x] Page-level JSON-LD schema installed on all 12 pages in the Wix editor
  (2026-08-05, markup name `Baxstar Schema`) — saved but **not yet published**.
  Full per-page log: `seo/schema/README.md`

---

## Site State Log
Running record of what has been changed in Wix and whether it is live.

| Date | Change | Live? |
|---|---|---|
| 2026-08-05 | JSON-LD structured data added to all 12 remaining pages via Page Settings -> Advanced SEO -> Structured data markup, each named `Baxstar Schema`. Pre-existing `SEO Scheme JSON` entry on /17-hybrid-ii-ice-castle-detroit-lakes left in place and flagged for a keep-or-remove decision. | Saved, **not published** |
| 2026-07-30 | Homepage schema (schema-homepage.json) | Live |
| 2026-07-29 | /faq schema (schema-faq.json) | Live |

Note on schema installs: they are done in the **Wix editor** (Pages & Menu -> hover
page -> ... -> SEO basics -> Advanced SEO), not the dashboard, and editor page names
differ from URL slugs. The slug -> page-name map is in `seo/schema/README.md`.

---
*Protocol version: 1.1 — April 2026*
*Status and Site State Log last updated: 2026-08-05*
