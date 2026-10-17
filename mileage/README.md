# Baxstar Miles

A dead-simple cumulative mileage counter. One file, no accounts, no GPS, no
tracking of where you go — it only counts **miles**.

## How it works

1. **First open** — type in what the odometer reads right now. That's mile zero.
2. **Add miles whenever** — a day's driving, a week's worth, a ballpark number.
   Optional; skip it entirely if you want.
3. **Weekly odometer check** — the app asks for the real odometer reading once
   a week (the check card turns gold when it's due). It compares the truck's
   number against what you logged and one tap trues the total up, so the
   cumulative count always matches reality. If you never log anything between
   checks, the odometer check alone keeps the count perfect.

The big number is total miles since mile zero. The week / month / year tiles
underneath split the same entries by date.

## Putting it on your phone

The app is `index.html` — one self-contained file.

- Host it anywhere that serves HTML (a hidden page on the site works), open it
  in Safari/Chrome on the phone, then **Add to Home Screen**. It opens
  full-screen like a real app.
- Always open it from the **same address** — the data is saved in the
  browser's storage for that address, on that device.

## Where the data lives (and keeping it safe)

- Everything is stored locally in the browser (`localStorage`). Nothing is
  sent anywhere.
- **Backup** (in Backup & Settings) downloads a JSON file with everything.
  Do it once in a while; **Restore** brings it back on any device.
- **Export CSV** gives a plain spreadsheet of every entry, odometer check,
  and the running total.
- Clearing the browser's site data wipes the app's memory — that's what the
  backup file is for.

## Notes

- Entry mistakes are no big deal: delete the entry (tap ✕ twice) and the next
  odometer check squares the total up automatically.
- "Fix Starting Odometer" in settings is only for correcting a typo in the
  day-one reading.
- Standalone tool — not a Wix iframe embed, so the embed scroll rules and the
  `indexifembedded` tag don't apply to it. It's marked `noindex`.
