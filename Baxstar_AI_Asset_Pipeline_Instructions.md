# AI Execution Instructions — Baxstar Asset Optimization Pipeline

## Purpose
These instructions are written for an AI agent to execute the full image and video optimization workflow for Baxstar Fishing web assets. Follow each step in order. Do not skip steps.

---

## TASK 1: Image Optimization (Squoosh)

**Input:** A JPEG or PNG photo intended for use as a website hero background
**Output:** A compressed WebP file ready for Wix Media Manager upload

**Instructions:**
1. Navigate to https://squoosh.app
2. Upload the source image
3. In the right panel, set format to **WebP**
4. Set quality to **82**
5. Open the resize panel and set width to:
   - **1080px** if the image is vertical (mobile hero)
   - **1920px** if the image is horizontal (desktop hero)
   - Maintain aspect ratio must be enabled
6. Zoom into the preview and inspect face and fine detail areas. If visible degradation exists, increase quality to **85**. If no degradation, attempt **78** to reduce file size further.
7. Confirm file size target is met:
   - Mobile (vertical): **under 150KB**
   - Desktop (horizontal): **under 250KB**
8. If file size exceeds target, reduce quality by 3 points and recheck
9. Download the WebP file
10. Rename file using this convention: `baxstar-[descriptor]-[device].webp`
    - Example: `baxstar-hero-mobile.webp` / `baxstar-hero-desktop.webp`
11. Save to: Desktop → Baxstar Assets folder

---

## TASK 2: Video Compression (Handbrake)

**Input:** An MP4 video exported from Kling or Runway (AI-generated cinemagraph)
**Output:** A compressed web-optimized MP4 ready for Wix video CDN upload

**Instructions:**
1. Open Handbrake (download only from https://handbrake.fr if not installed)
2. Drag source MP4 into Handbrake
3. **Summary tab:**
   - Format: MP4
   - Check: Web Optimized
   - Uncheck: Passthru Common Metadata
   - Check: Align A/V Start
4. **Audio tab:**
   - Delete all audio tracks — hero videos are muted, audio is dead weight
5. **Video tab:**
   - Codec: H.264
   - RF Quality: 22
   - Framerate: 30 FPS constant
6. **Dimensions tab:**
   - Anamorphic: None
   - Set exact display dimensions:
     - Mobile vertical: **810×1080**
     - Desktop horizontal: **1920×1080**
7. **Output settings:**
   - Rename file: `baxstar-hero-mobile.mp4` or `baxstar-hero-desktop.mp4`
   - Save destination: Desktop → Baxstar Assets
8. Click **Start**
9. Confirm output file size is **under 3MB** for a 5-second clip
10. If over 3MB, re-run with RF quality set to **24** instead of 22

---

## TASK 3: Upload to Wix

**Instructions:**
1. Log into Wix at https://manage.wix.com
2. Navigate to Media Manager
3. Upload the WebP image file — note the CDN URL after upload
4. Upload the MP4 video file — note the CDN URL after upload
5. CDN URL format for images: `https://static.wixstatic.com/media/[FILE_ID]~mv2.webp`
6. CDN URL format for video: `https://video.wixstatic.com/video/[FILE_ID]/1080p/mp4/file.mp4`
7. Paste image URL into hero HTML file at: `background-image: url('[PASTE HERE]')`
8. Paste video URL into hero HTML file at: `<source src="[PASTE HERE]" type="video/mp4"/>`

---

## File Naming Convention
| Asset | Convention | Example |
|---|---|---|
| Mobile WebP | baxstar-[page]-mobile.webp | baxstar-hero-mobile.webp |
| Desktop WebP | baxstar-[page]-desktop.webp | baxstar-hero-desktop.webp |
| Mobile video | baxstar-[page]-mobile.mp4 | baxstar-hero-mobile.mp4 |
| Desktop video | baxstar-[page]-desktop.mp4 | baxstar-hero-desktop.mp4 |

---

## Quality Checkpoints
- [ ] WebP file under target KB size
- [ ] No visible quality loss in face/detail areas
- [ ] MP4 under 3MB
- [ ] MP4 has no audio track
- [ ] MP4 dimensions match display dimensions (not storage dimensions)
- [ ] Web Optimized flag enabled in Handbrake
- [ ] Both files renamed correctly before upload
- [ ] Both CDN URLs confirmed after Wix upload

---

*Version 1.0 — April 29, 2026 — Baxstar Fishing Asset Pipeline*
