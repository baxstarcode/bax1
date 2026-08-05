# Baxstar Fishing — Page-Level Structured Data (JSON-LD)

Paste-ready schema blocks for www.baxstarfishing.com. One file per page.
Every fact, price, and claim is grounded in the page's visible text as of 2026-07-30.
All blocks are minified and well under Wix's 7000-character limit.

**Status as of 2026-08-05: all 12 page blocks below are installed in the Wix
editor under the markup name `Baxstar Schema`. Saved, but NOT yet published —
see the Install log at the bottom.**

## How to install (per page, ~2 min each)

1. Wix editor -> **Pages & Menu** -> hover the page -> **...** -> **SEO basics**
2. **Advanced SEO** tab -> open **Structured data markup** -> **+ Add New Markup**
3. Paste the ENTIRE contents of the page's .json file, verbatim
4. Name it `Baxstar Schema` (naming convention as of 2026-08-05) -> Apply -> Save -> Publish

## Page -> file map (paste in this order)

| # | Page | File | Installed |
|---|------|------|-----------|
| 1 | /fishing-trips | schema-fishing-trips.json | 2026-08-05 |
| 2 | /icefishing | schema-icefishing.json | 2026-08-05 |
| 3 | /ice-castle-rentals | schema-ice-castle-rentals.json | 2026-08-05 |
| 4 | /detroit-lakes-pontoon-rentals | schema-detroit-lakes-pontoon-rentals.json | 2026-08-05 |
| 5 | /about | schema-about.json | 2026-08-05 |
| 6 | /21-ice-castle-rental | schema-21-ice-castle-rental.json | 2026-08-05 |
| 7 | /17-ice-castle-luxury-rv-edition-rental | schema-17-ice-castle-luxury-rv-edition-rental.json | 2026-08-05 |
| 8 | /17-hybrid-ii-ice-castle-detroit-lakes | schema-17-hybrid-ii-ice-castle-detroit-lakes.json | 2026-08-05 (flagged) |
| 9 | /icefishing/ice-house-rentals | schema-icefishing--ice-house-rentals.json | 2026-08-05 |
| 10 | /datenight | schema-datenight.json | 2026-08-05 |
| 11 | /familytrips | schema-familytrips.json | 2026-08-05 |
| 12 | /fishing-consultations | schema-fishing-consultations.json | 2026-08-05 |

Already installed (archived here for reference):
- Homepage: schema-homepage.json (live since 2026-07-30)
- /faq: schema-faq.json (live since 2026-07-29)

## What's inside each block

Compound @graph: WebPage (or AboutPage) + LocalBusiness + Person (Brady Baxter,
5x Minnesota Master Angler) + Service, interlinked via @id anchors
(#business / #brady) so Google unifies all pages into one business entity.
Real prices from the visible page text are marked up as Offer / AggregateOffer
nodes on 7 pages. No fabricated prices, reviews, or ratings.

## Deliberate omissions

- No aggregateRating on the pontoon page: the visible 4.9/100+ figure is from
Google reviews; marking up third-party ratings on your own site violates
Google's self-serving review policy. The visible badge stays - it works on
humans; the schema skips it so it can't be flagged.
- No FAQPage nodes: these pages have no visible Q&A sections. Schema must
match visible content. The /faq page already carries the FAQPage block.
- No offers on /fishing-trips, /icefishing, /familytrips: those pages show
no prices. If you want rates marked up there, put the prices in the page
text first, then ask Claude to regenerate that block.

## Verify after publishing

Run each page URL through https://validator.schema.org - expect the graph
to parse with 0 errors. (Google's Rich Results Test no longer reports
FAQ/LocalBusiness for most sites; the validator is the right tool.)

## Install log

### 2026-08-05 — all 12 page blocks installed in the Wix editor

Added through Page Settings -> Advanced SEO -> Structured data markup ->
+ Add New Markup, each entry named exactly `Baxstar Schema`. Each file was
fetched from its raw GitHub URL and injected verbatim, then byte-compared
against the source before Apply was clicked, so every entry is an exact match
with no reformatting. Nothing else in SEO settings (titles, descriptions,
meta tags) was touched. Homepage and /faq were skipped - already live.

| Page | Bytes | Result |
|------|-------|--------|
| /fishing-trips | 2028 | added |
| /icefishing | 2043 | added |
| /ice-castle-rentals | 2370 | added |
| /detroit-lakes-pontoon-rentals | 2321 | added |
| /about | 1760 | added |
| /21-ice-castle-rental | 2453 | added |
| /17-ice-castle-luxury-rv-edition-rental | 2534 | added |
| /17-hybrid-ii-ice-castle-detroit-lakes | 2540 | added - flagged |
| /icefishing/ice-house-rentals | 2539 | added |
| /datenight | 2542 | added |
| /familytrips | 2088 | added |
| /fishing-consultations | 2495 | added |

Totals: 11 added, 1 added-and-flagged, 0 already present, 0 failed.

**Flag - /17-hybrid-ii-ice-castle-detroit-lakes:** this page already carried a
separate markup entry named `SEO Scheme JSON` (3691 chars, pretty-printed and
wrapped in a `<script type="application/ld+json">` tag). It was left in place
as instructed, so the page now has two overlapping WebPage/LocalBusiness
graphs. Decide whether to remove the older entry before publishing - duplicate
entity graphs on one URL can send mixed signals.

**Open item: the site was Saved in the Wix editor but NOT published.** None of
these 12 blocks are live on www.baxstarfishing.com until Publish is clicked.
Publish, then run all 12 URLs through https://validator.schema.org.

**Wix editor slug -> page-name map** (editor page names differ from slugs, which
made the pages hard to find - recorded here for next time):

| Slug | Wix editor page name |
|------|----------------------|
| /fishing-trips | Fishing Trips |
| /icefishing | Ice Fishing |
| /ice-castle-rentals | Ice Castles |
| /detroit-lakes-pontoon-rentals | Detroit Lakes Pontoon Rentals |
| /about | About |
| /21-ice-castle-rental | 21' RV Extreme Edition |
| /17-ice-castle-luxury-rv-edition-rental | 17' Luxury RV Edition |
| /17-hybrid-ii-ice-castle-detroit-lakes | 17' Hybrid II RV Edition |
| /icefishing/ice-house-rentals | Ice House Rentals (child of Ice Fishing) |
| /datenight | Date Night On The Ice |
| /familytrips | Family Trips |
| /fishing-consultations | Consults |
