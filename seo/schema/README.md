# Baxstar Fishing — Page-Level Structured Data (JSON-LD)

Paste-ready schema blocks for www.baxstarfishing.com. One file per page.
Every fact, price, and claim is grounded in the page's visible text as of 2026-07-30.
All blocks are minified and well under Wix's 7000-character limit.

## How to install (per page, ~2 min each)

1. Wix dashboard -> Pages -> (page) -> SEO settings -> **Advanced SEO** tab
2. Open **Structured data markup** -> **+ Add markup**
3. Paste the ENTIRE contents of the page's .json file
4. Name it (e.g. "Baxstar Fishing Trips SEO Markup JSON") -> Save -> Publish

## Page -> file map (paste in this order)

| # | Page | File |
|---|------|------|
| 1 | /fishing-trips | schema-fishing-trips.json |
| 2 | /icefishing | schema-icefishing.json |
| 3 | /ice-castle-rentals | schema-ice-castle-rentals.json |
| 4 | /detroit-lakes-pontoon-rentals | schema-detroit-lakes-pontoon-rentals.json |
| 5 | /about | schema-about.json |
| 6 | /21-ice-castle-rental | schema-21-ice-castle-rental.json |
| 7 | /17-ice-castle-luxury-rv-edition-rental | schema-17-ice-castle-luxury-rv-edition-rental.json |
| 8 | /17-hybrid-ii-ice-castle-detroit-lakes | schema-17-hybrid-ii-ice-castle-detroit-lakes.json |
| 9 | /icefishing/ice-house-rentals | schema-icefishing--ice-house-rentals.json |
| 10 | /datenight | schema-datenight.json |
| 11 | /familytrips | schema-familytrips.json |
| 12 | /fishing-consultations | schema-fishing-consultations.json |

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
