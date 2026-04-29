# Baxstar Asset Optimization Guide

---

## Squoosh — Image Compression

**What it is:** Free browser-based Google tool that converts and compresses images to WebP format for fast web loading without visible quality loss.

**Steps:**
1. Go to squoosh.app and drag your image onto the page
2. Set format to **WebP**, quality to **82**, resize width to **1080px** (mobile) or **1920px** (desktop)
3. Zoom into faces and fine details in the side-by-side preview — if it looks identical, you're done
4. Target file size: under **150KB** (mobile) / under **250KB** (desktop)
5. Download and upload the WebP directly to Wix Media Manager

---

## Handbrake — Video Compression

**What it is:** Free open source video tool that compresses MP4 files for fast web playback without quality loss — download only from handbrake.fr.

**Steps:**
1. Drag your MP4 into Handbrake
2. Summary tab: Format **MP4**, check **Web Optimized**, uncheck Passthru Metadata
3. Audio tab: **delete all audio tracks**
4. Video tab: Codec **H.264**, RF quality **22**, Framerate **30 FPS**
5. Dimensions tab: Anamorphic **None**, set exact pixel dimensions (e.g. 810×1080 mobile)
6. Rename file descriptively (e.g. baxstar-hero-mobile.mp4), save to Baxstar Assets folder, hit **Start**
7. Target file size: under **3MB** for a 5-second hero clip

---

*Saved: April 29, 2026 — Baxstar Fishing Asset Pipeline*
