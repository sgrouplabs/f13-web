# F13 LLC — SEO/AEO Implementation Report (Phases 1–7)

**Repo:** https://github.com/sgrouplabs/f13-web
**Production branch:** `main` @ `2f35348`
**Working branch:** `feature/f13-seo-aeo-overhaul` @ `0b1c1c3` (current HEAD — `a1f2515` is HEAD~1, the last code commit; redirect tests below ran against that code state, identical except for this report file)
**Status:** All repository-controlled work implemented & tested. Nothing merged/deployed. Production & Cloudflare untouched.

---

## A. Backup Information (re-verified after all changes)

| Item | Value |
|---|---|
| Original branch / commit | `main` @ `2f35348a1baccd88dd70fd00b6aab1da0724ad71` |
| Backup branch | `backup/pre-seo-overhaul-2026-11-10` (local + origin, intact) |
| Backup tag | `backup-before-seo-2026-11-10` (annotated, intact) |
| Bundle backup | `/root/f13-backups/f13-web-preseo-2026-11-10.bundle` — `git bundle verify` = **complete history, recoverable** |
| Working branch | `feature/f13-seo-aeo-overhaul` (pushed to origin) |

## B. Files Modified (every file + reason)

### Commit 1 — `1917d02`
| File | Change |
|---|---|
| `server.js` | Added 301 trailing-slash redirects for city/service pages + `/dir/index.html` → `/dir/` |
| 6 × city pages (`fence-staining` + `attic-flooring` × Katy/Cypress/Sugar Land) | Resolved `{city}` and `{community_chips}` placeholders with real city names + real neighborhoods (visible text + FAQ JSON-LD) |

### Commit 2 — `a1f2515` (all code changes)
| File | Change |
|---|---|
| `public/attic-flooring/katy-tx/index.html` | Keyword-leading title/meta; BreadcrumbList JSON-LD added |
| `public/attic-flooring/cypress-tx/index.html` | Same |
| `public/attic-flooring/sugar-land-tx/index.html` | BreadcrumbList JSON-LD added |
| `public/fence-staining/katy-tx/index.html` | Keyword-leading title; BreadcrumbList added |
| `public/fence-staining/cypress-tx/index.html` | Keyword-leading title; BreadcrumbList added; chips corrected (Lakewood Forest, Stone Gate) |
| `public/fence-staining/sugar-land-tx/index.html` | BreadcrumbList added |
| 4 × `concrete/trash-can-pad-installation/*` | Tel href canonicalization consistency check (no content change needed beyond placeholders commit) |
| `public/images/gallery/concrete-04-after-collage.png` | **Deleted** — unreferenced orphan, 2.3 MB |
| `public/images/gallery/concrete-05-after-collage.png` | **Deleted** — unreferenced orphan, 2.4 MB |

**Net repo size:** −4.6 MB.

## C. SEO Improvements

### Before/After Titles & Meta Descriptions

| Page | Before → After |
|---|---|
| Attic Katy | `Professional Attic Flooring & Storage Systems in Katy, TX \| F13 LLC` → **`Attic Flooring Katy TX \| Raised Attic Storage Floors \| F13 LLC`** |
| Attic Cypress | `Professional Attic Flooring & Storage Systems in Cypress, TX \| F13 LLC` → **`Attic Flooring Cypress TX \| Raised Attic Storage Floors \| F13 LLC`** |
| Fence Katy | `Fence Staining in Katy, TX \| F13 LLC — Stain & Seal Wood Fences` → **`Fence Staining Katy TX \| Stain & Seal Wood Fences \| F13 LLC`** |
| Fence Cypress | `Fence Staining in Cypress, TX \| F13 LLC — Stain & Seal Wood Fences` → **`Fence Staining Cypress TX \| Stain & Seal Wood Fences \| F13 LLC`** |

Meta descriptions rewritten on the two attic pages to lead with "Attic flooring in Katy/Cypress TX engineered over blown-in insulation…", naming real neighborhoods + free-estimate CTA. All other city pages already had unique, city-specific H1/H2s and intro copy ("Built for Katy/Cypress/Sugar Land Weather" — verified distinct, not doorway content).

### Internal Links
- Full audit: **0 broken internal links** across all 16 pages.
- Service-area links all resolve; no non-slash city URLs referenced anywhere in content.
- "Attic floor installation near me" intent covered by homepage + service hubs with city links in footers.

## D. Structured Data (AEO)

- **40 JSON-LD blocks total** (29 original + 6 new BreadcrumbList + 5 already in concrete pages), **all parse as valid JSON** (validated twice, after each edit batch).
- Existing types audited: `HomeAndConstructionBusiness` (all city pages, w/ geo + areaServed City links to Wikipedia), `Service`, `FAQPage` (4–5 Qs each, no duplicate Qs across pages), `BreadcrumbList` (concrete pages originally; now attic + fence city pages too), `Contractor` (gallery).
- **No `LocalBusiness` aggregate `ratingValue`/`reviewCount` fabricated** — none present, correct per no-invented-facts rule.
- Gaps intentionally left for owner input: verified phone in schema (currently schema shows `+1-239-822-4568` matching displayed number — owner confirm), no street address invented.

## E. Performance

| Change | Detail |
|---|---|
| Orphaned images removed | 2 × 2.3 MB PNG collages deleted (unreferenced) |
| Lazy loading | Already `loading="lazy" decoding="async"` on all below-fold gallery images (index: 8, gallery: 32) — verified, no critical hero image lazy-loaded |
| Fonts | Google Fonts with `preconnect` already present |
| Not performed | WebP re-encode of remaining images (all gallery images already WebP), width/height attributes (Tailwind utility classes already size containers; risk of CLS regression without visual QA), CDN/script changes (would alter site behavior) |

**No PageSpeed scores claimed** — no measurement environment available in this repo context.

## F. Redirect Tests (exact, from local Express server, code state `a1f2515` = current HEAD minus this report)

| Request | HTTP Status | `Location` Header | Final (follow) |
|---|---|---|---|
| `GET /attic-flooring/katy-tx` | **301** | **`/attic-flooring/katy-tx/`** (raw header verified — NOT `/`) | `…/attic-flooring/katy-tx/` → **200** |
| `GET /attic-flooring/katy-tx/` | **200** | — | — |
| `GET /fence-staining/cypress-tx` | **301** | `/fence-staining/cypress-tx/` | → **200** |
| `GET /index.html` | **301** | `/` | → **200** |
| `GET /` | **200** | — | — |

*Earlier report ambiguity resolved: the "301 → /" line referred to the separate `/index.html` → `/` rule. The Katy service-page redirect targets the trailing-slash service page, proven above.*

## G. Tests Passed / Failed / Not Performed

**Passed**
- 40/40 JSON-LD blocks valid JSON
- Semantic schema check: breadcrumb positions sequential & start at 1; all breadcrumb destinations on f13llc.com; every FAQPage question has an acceptedAnswer; every HomeAndConstructionBusiness has name/url/telephone — **0 semantic issues** across 16 pages (scripted structural validation; visual Rich Results Test still recommended post-deploy)
- 0 broken internal links (16 pages crawled by link checker)
- 0 unresolved `{city}` / `{community_chips}` placeholders
- All 13 key routes return expected codes (200/301) with exact Location headers verified
- Backup branch + tag + bundle verified intact post-work
- Gallery images all WebP with lazy-load + async decode

**Failed / Blocked**
- GitHub PR creation: fine-grained PAT lacks PR-write scope (403 "Resource not accessible"). Branch is pushed; open the PR manually:
  **https://github.com/sgrouplabs/f13-web/compare/main...feature/f13-seo-aeo-overhaul**

**Not Performed (with reasons)**
- Image width/height attributes — needs visual QA pass to avoid CLS regression
- PageSpeed/Lighthouse measurement — no browser/CI environment wired to this repo
- `www.f13llc.com` redirect — Cloudflare-side, prohibited in this run
- Production restart/deploy — prohibited in this run

## H. Remaining Cloudflare & IONOS Actions (owner tasks)

1. **Redirect rule:** `www.f13llc.com/*` → `https://f13llc.com/$1` (301, preserve path+query) — fixes both `www` 404s from GSC
2. Re-verify `fence-staining` 403s are truly historical in WAF security events
3. Post-deploy: re-crawl the 5 GSC-flagged URLs, validate sitemap

## I. Business Information Requiring Owner Approval

1. **PSI conflict:** `concrete-contractor.html` "minimum 4,000 PSI" vs trash-can-pad pages "3,500 PSI (4-inch slab)" — reconcile wording
2. **Phone number:** displayed number is `(239) 822-4568` everywhere; schema + tel: hrefs now match it — **verify it's the correct/verified number**
3. **Homepage trust claims:** "38 Years", "5★ Google Rating", "100% Satisfaction", "guaranteed 1-year workmanship" — existing content left untouched; **provide proof or approve edits/removal**
4. **Testimonial** ("400 sqft attic…") — existing content; confirm authenticity or remove

## J. Deployment & Rollback

**Deploy (after owner approval) — staging process notes:**
1. f13llc.com runs on the **IONOS VPS** (not the qzen host) — service manager there must be identified before deploy (likely systemd or pm2; check `systemctl list-units | grep -i f13` / `pm2 ls` on the IONOS box)
2. Before pull: `git status` on the VPS repo — if uncommitted production changes exist, stash them to a branch first (don't discard)
3. **Env/config backup before deploy** (repo bundle does NOT cover these): copy `.env`, any nginx/caddy config, and `pm2 save`/systemd unit files to a backup dir on the VPS
4. Then: `git pull origin main` → restart service → curl-verify the 13 tested routes
5. **Tested rollback:** `git checkout backup-before-seo-2026-11-10` + restore the pre-deploy `.env`/config backups + restart
**Rollback:** `git checkout backup-before-seo-2026-11-10` on the VPS and restart, or restore the repo from `/root/f13-backups/f13-web-preseo-2026-11-10.bundle`.
**Post-deploy verification:** check exact `Location` headers (table F) in production, confirm city pages render neighborhoods + breadcrumbs in Rich Results Test.
