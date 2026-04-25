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

---
*Protocol version: 1.1 — April 2026*
