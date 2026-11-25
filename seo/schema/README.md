# Baxstar Fishing — Page-Level Structured Data (JSON-LD)

Paste-ready schema blocks for www.baxstarfishing.com. One file per page.
Every fact, price, and claim is grounded in the page's visible text as of 2026-07-30.
All blocks are minified and well under Wix's 7000-character limit.

**Status: LIVE.** All 12 page blocks below are installed in Wix under the markup
name `Baxstar Schema` and the site was published on 2026-08-05. Verified serving
on all 12 URLs — see the Install log.

## How to install (per page, ~2 min each)

1. Wix editor -> **Pages & Menu** -> hover the page -> **...** -> **SEO basics**
2. **Advanced SEO** tab -> open **Structured data markup** -> **+ Add New Markup**
3. Paste the ENTIRE contents of the page's .json file, verbatim
4. Name it `Baxstar Schema` (naming convention as of 2026-08-05) -> Apply -> Save -> Publish

## Page -> file map

| # | Page | File | Status |
|---|------|------|--------|
| 1 | /fishing-trips | schema-fishing-trips.json | live 2026-08-05 |
| 2 | /icefishing | schema-icefishing.json | live 2026-08-05 |
| 3 | /ice-castle-rentals | schema-ice-castle-rentals.json | live 2026-08-05 |
| 4 | /detroit-lakes-pontoon-rentals | schema-detroit-lakes-pontoon-rentals.json | live 2026-08-05 |
| 5 | /about | schema-about.json | live 2026-08-05 |
| 6 | /21-ice-castle-rental | schema-21-ice-castle-rental.json | live 2026-08-05 |
| 7 | /17-ice-castle-luxury-rv-edition-rental | schema-17-ice-castle-luxury-rv-edition-rental.json | live 2026-08-05 |
| 8 | /17-hybrid-ii-ice-castle-detroit-lakes | schema-17-hybrid-ii-ice-castle-detroit-lakes.json | live 2026-08-05 (duplicate — see log) |
| 9 | /icefishing/ice-house-rentals | schema-icefishing--ice-house-rentals.json | live 2026-08-05 |
| 10 | /datenight | schema-datenight.json | live 2026-08-05 |
| 11 | /familytrips | schema-familytrips.json | live 2026-08-05 |
| 12 | /fishing-consultations | schema-fishing-consultations.json | live 2026-08-05 |

Installed earlier:
- Homepage: schema-homepage.json (live since 2026-07-30; re-synced to the live homepage block 2026-11-25, see the Install log)
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

## Verify

Run each page URL through https://validator.schema.org - expect the graph
to parse with 0 errors. (Google's Rich Results Test no longer reports
FAQ/LocalBusiness for most sites; the validator is the right tool.)

## Install log

### 2026-08-05 — all 12 page blocks installed and published

Added through Page Settings -> Advanced SEO -> Structured data markup ->
+ Add New Markup, each entry named exactly `Baxstar Schema`. Each file was
fetched from its raw GitHub URL and injected verbatim, then byte-compared
against the source before Apply was clicked, so every entry is an exact match
with no reformatting. Nothing else in SEO settings (titles, descriptions,
meta tags) was touched. Homepage and /faq were skipped - already live.
The site was then published.

Live verification (2026-08-05): every one of the 12 URLs was fetched and the
`application/ld+json` block length compared against the source file. All 12
match exactly.

| Page | Bytes | Live check |
|------|-------|-----------|
| /fishing-trips | 2028 | match |
| /icefishing | 2043 | match |
| /ice-castle-rentals | 2370 | match |
| /detroit-lakes-pontoon-rentals | 2321 | match |
| /about | 1760 | match |
| /21-ice-castle-rental | 2453 | match |
| /17-ice-castle-luxury-rv-edition-rental | 2534 | match |
| /17-hybrid-ii-ice-castle-detroit-lakes | 2540 | match, but emitted twice |
| /icefishing/ice-house-rentals | 2539 | match |
| /datenight | 2542 | match |
| /familytrips | 2088 | match |
| /fishing-consultations | 2495 | match |

**Open item - /17-hybrid-ii-ice-castle-detroit-lakes:** the live page outputs the
same 2540-byte block **twice**, back to back. Before this rollout the page had a
second markup entry named `SEO Scheme JSON` (3691 chars, pretty-printed, wrapped
in a `<script type="application/ld+json">` tag); that older content does not
appear in the published HTML, so the duplicate is two copies of the new block.
Open that page's Structured data markup list in the editor and delete one of the
two entries. Duplicate identical graphs are not an error, but they are noise.

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


### 2026-11-17 — Blue Diamond rename (Handoff #749)

Published through the Wix SEO API and verified in rendered HTML: the house-page title, Open Graph and Twitter titles are `Blue Diamond | Most Luxurious Ice House`; its meta description and JSON-LD use Blue Diamond. The homepage OfferCatalog names this house Blue Diamond. The per-page JSON, schema map and injector are synchronized; the URL, file names, prices and other house facts are unchanged. The homepage API required JSON minification to meet its 4096-byte tag limit; the graph otherwise changed only the house name.

The Wix editor was signed out in this session. The visible H1, menu label, sibling links, body aliases and two image alt texts still require the editor pass; publishing these SEO changes does not complete those edits. Historical capture files and the install log above retain their original names.


### 2026-11-17 — The Hearth naming (Handoff #758)

Brady confirmed the house: "The Hearth = 17' Ice Castle Hybrid II, FareHarbor item 681248." Published through the Wix editor and verified in rendered HTML. The page's `Baxstar Schema` markup now leads with The Hearth (WebPage name and description; Service name, serviceType and description). The title tag is `The Hearth | 17′ Ice Castle Hybrid II RV Edition Rental`; Open Graph and X titles are `The Hearth | 17′ Ice Castle Hybrid II RV Edition | Premium Ice House Rental`. The homepage OfferCatalog (Wix markup `Baxstar Homepage SEO Markup JSON`, not mirrored in this folder) names the house The Hearth. The editor page name, which is also the menu label, is now `The Hearth`. The URL /17-hybrid-ii-ice-castle-detroit-lakes, file names and offers are unchanged. The per-page JSON, schema map and injector match the published graph.

Known mismatch left in place: the markup offers are $475 single night and $825 2-night weekend, while the visible page shows $500 and $875. Prices were out of scope for the rename. The "emitted twice" open item above no longer reproduces: on 2026-11-17 the page emitted one block. The install log and slug map above keep their original names.

### 2026-11-17 — The Hearth prices $485 / $850 (Handoff #763)

Brady, verbatim: "Change The Hearth to $485 and $850 anywhere and everywhere." The visible page, the page's `Baxstar Schema` markup and FareHarbor item 681248 (Base sheet, before FareHarbor's 6% fee) now say $485 single night and $850 3 Day/2 Night. The per-page JSON, schema map and injector offers were changed from 475/825 to 485/850 to match the published graph. This closes the "Known mismatch" noted in the entry above. Not changed here: the Lodge weekend offer in schema-map.json and the injector still says 975, while the live Lodge markup says 1025.

### 2026-11-18 — The Lodge mirror synced to live (Handoff #764)

The Lodge per-page JSON, schema map and injector now match the published /21-ice-castle-rental markup: 2-night weekend offer 975 to 1025 (live since Handoff #717) and "7 pre-drilled holes" (live; Brady confirmed 7 holes on Nov 14). This closes the Lodge mismatch noted in the entry above.

### 2026-11-25 — Homepage mirror synced to live

Read-only check: all 14 pages were fetched and each live JSON-LD block was compared with this folder. 13 matched exactly: the 12 page files and schema-faq.json. The schema-map.json page nodes match the page files, and the injector's embedded map equals schema-map.json. The homepage did not match. schema-homepage.json still held the 2026-07-30 fishing-only graph. The live homepage serves the ice-season graph: WebPage name `Detroit Lakes Ice Fishing Guide & Fish House Rentals | Baxstar`, an Ice Castle rentals OfferCatalog (Range Runner, The Hearth, Blue Diamond, 21' RV Extreme Edition, Date Night on the Ice) and a guided ice fishing Service. schema-homepage.json now holds the live block verbatim (3415 bytes, byte-identical to the served block), so pasting it can no longer overwrite the live homepage markup with the old graph. The homepage is not in schema-map.json, so the loader and injector are unaffected. Nothing in Wix was changed. /17-hybrid-ii-ice-castle-detroit-lakes emitted one block, as noted on 2026-11-17.

### 2026-11-24 — Blue Diamond markup drops LiveScope

Brady, verbatim: "Remove livescope from blue diamond". The /17-ice-castle-luxury-rv-edition-rental `Baxstar Schema` markup had three LiveScope phrases, all describing the hole layout. They now read "8 pre-drilled fishing holes", matching the page's "8 pre-drilled holes" line. Prices and every other node are unchanged. This was written and published through the Wix Item SEO Tags API (page z6iby, targeted SEO publish), after confirming the page's draft markup still equalled the live block. The served page then returned the new markup (2439 bytes, no LiveScope). The page text was not published, so it still carries its old LiveScope lines, and /icefishing-new still returned 404. The per-page JSON, schema map and injector now match the published graph. The two LiveScope mentions left in the map belong to Brady's Person node and the /fishing-trips guided service, not Blue Diamond.
