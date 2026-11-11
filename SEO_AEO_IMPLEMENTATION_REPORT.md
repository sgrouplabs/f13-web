# F13 LLC — SEO/AEO Implementation Report (Phase 1–2)

**Date:** 2026-11-11
**Repo:** https://github.com/sgrouplabs/f13-web
**Production branch:** `main` @ `2f35348`
**Working branch:** `feature/f13-seo-aeo-overhaul` @ `1917d02`

---

## A. Backup Information

| Item | Value |
|---|---|
| Original branch / commit | `main` @ `2f35348a1baccd88dd70fd00b6aab1da0724ad71` |
| Backup branch | `backup/pre-seo-overhaul-2026-11-10` (pushed to origin) |
| Backup tag | `backup-before-seo-2026-11-10` (annotated, pushed) |
| Bundle backup | `/root/f13-backups/f13-web-preseo-2026-11-10.bundle` — `git bundle verify` = **complete history, recoverable** |
| Working branch | `feature/f13-seo-aeo-overhaul` (pushed) |
| Uncommitted changes | None found at start (clean tree) |

Recovery: `git clone f13-web-preseo-2026-11-10.bundle -b main` or `git fetch /root/f13-backups/... main:restored-main`.

## B. Files Modified (7)

| File | Purpose |
|---|---|
| `server.js` | Added trailing-slash 301 redirects for city/service pages + `/dir/index.html` → `/dir/` canonicalization |
| `public/fence-staining/katy-tx/index.html` | `{city}` → "Katy"; `{community_chips}` → 8 real Katy neighborhoods (Cinco Ranch, Elyson, Cane Island, Firethorne, Seven Meadows, Grand Lakes, Katy Brookshire, Williamsburg Reserve) |
| `public/fence-staining/cypress-tx/index.html` | Same for Cypress (Bridgeland, Coles Crossing, Fairfield, Towne Lake, Cypress Creek Lakes, Vintage Park, Cypress Mill, Fry Road Corridor) |
| `public/fence-staining/sugar-land-tx/index.html` | Same for Sugar Land (First Colony, Riverstone, Telfair, Sweetwater, New Territory, Greatwood, Lake Pointe, Avalon) |
| `public/attic-flooring/katy-tx/index.html` | `{city}` / `{community_chips}` resolved |
| `public/attic-flooring/cypress-tx/index.html` | Resolved |
| `public/attic-flooring/sugar-land-tx/index.html` | Resolved |

## C. SEO Improvements Implemented

- **Redirect fix (GSC "Redirect error")**: `/attic-flooring/katy-tx` → 301 → `/attic-flooring/katy-tx/` (200). Also applies to all attic/fence/concrete city pages and `/dir/index.html` variants.
- **Placeholder elimination**: no `{city}` or `{community_chips}` template vars remain anywhere in `public/` (grep-verified). FAQ JSON-LD and visible summaries now carry real city names — also fixes AEO FAQ answers.
- **Neighborhood chips**: real, city-specific neighborhoods replace the unresolved chips — improves local relevance signals.

## D. Technical Fixes — Problem Disposition

### Fixed in GitHub (this PR)
- `/attic-flooring/katy-tx` redirect error → origin-level 301 (was 404 at origin)
- City-page placeholder defects

### Verified already OK (historical GSC errors)
- `https://f13llc.com/fence-staining/cypress-tx/` → **200 OK** live (403 historical)
- `https://f13llc.com/fence-staining.html` → **200 OK** live (403 historical)
- All canonical tags already `https://f13llc.com` (no-www) — no changes needed
- `robots.txt` + `sitemap.xml` already clean; every sitemap URL returns 200

### Requires Cloudflare-side change (outstanding — owner task)
- `https://www.f13llc.com/` and `http://www.f13llc.com/` → **404**. Needs a www→apex redirect rule (Bulk Redirect or Page Rule on the `www.f13llc.com` hostname). **Cannot be fixed in the repo.** Not attempted per instructions.
- If fence-staining 403s recur in GSC after a fresh crawl, check Cloudflare WAF security events.

### Flagged for owner (not changed)
- **Concrete PSI conflict**: `concrete-contractor.html` says "minimum 4,000 PSI for all our concrete work"; trash-can-pad pages say 3,500 PSI (4-inch slab). Plausible reconciliation: pads = 4" 3,500 PSI, heavier work = 4,000+. Owner to confirm before any wording change.

## E. Tomorrow's Cloudflare Checklist
1. Add redirect rule: `www.f13llc.com/*` → `https://f13llc.com/$1` (301, preserve path+query)
2. Confirm tunnel ingress routes for f13llc.com are intact
3. Review WAF/security events if fence-staining 403s persist
4. Validate HTTPS + apex/www behavior end-to-end
5. Final URL response test for all GSC-flagged URLs

## F. Google Search Console Checklist
1. URL Inspection (live test) on the 5 flagged URLs
2. Re-submit `https://f13llc.com/sitemap.xml`
3. Request re-indexing of fixed city pages
4. Validate the "Redirect error" as fixed
5. Monitor Performance over 2 weeks

## G. Testing Results
- ✅ All 29 JSON-LD blocks parse as valid JSON
- ✅ Local server (port 3999): 13 route tests — all expected codes:
  - `/attic-flooring/katy-tx` 301 → `/`; trailing slash 200; `/index.html` 301 → `/`
  - all city pages, gallery, privacy, sitemap, robots = 200
- ✅ Zero remaining placeholders (grep-verified)
- ✅ No build/lint/typecheck scripts exist in this project (plain Express static site) — npm start verified
- ⚠️ PR creation **blocked**: fine-grained PAT lacks PR-write scope (403). Branch is pushed; open manually:
  **https://github.com/sgrouplabs/f13-web/compare/main...feature/f13-seo-aeo-overhaul**
  (Issue #1 created in the repo documenting this.)

## H. Deployment & Rollback
**Deploy (owner-approved only):** merge PR → pull `main` on IONOS VPS → restart the f13 service (supervisor/systemd unit already runs `node server.js`).
**Rollback:** `git checkout backup-before-seo-2026-11-10` and restart, or restore from the bundle file.
**Verify after deploy:** curl the 5 GSC URLs + spot-check a city page for rendered neighborhoods.

## Remaining Owner Inputs Needed
1. PSI reconciliation (4,000 vs 3,500) — confirm or correct
2. Verified phone number (footer tel links display a partially masked number)
3. Approval to proceed with Phase 4–6 (schema expansion, meta refresh, image optimization)
