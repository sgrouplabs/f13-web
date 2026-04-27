# F13 LLC — Competitive Site Audit & Gap Analysis

**Date:** 2026-04-27
**Analyst:** El Padrino
**Project:** f13-web

---

## 1. Executive Summary

The F13 LLC website is a solid lead-generation tool with a clean mobile-first design, functional quote form, and good foundational SEO. The structure is semantic, the stack is lightweight (Node.js + Express + Supabase), and the UX is conversion-oriented with prominent click-to-call CTAs.

**Current Strengths:**
- Clean semantic HTML5 structure (header, nav, section, footer)
- Proper meta tags, Open Graph, and JSON-LD Schema (Contractor type) already in place
- Mobile-responsive Tailwind CSS with sticky header and smooth anchor scrolling
- Vimeo video integration for before/after project showcases
- Quote lead form connected to Supabase backend
- Multiple trust signals: stats bar, testimonial section, "Why Choose Us" with insured badge
- Toast notification system for form feedback
- Service area tag list for local SEO
- Click-to-call on all devices; phone number in sticky header

**Overall Assessment:** The site is a capable MVP. It will hold its own against low-tier competitors but lacks the depth and trust-building elements that separate top-ranking Houston contractors from the rest.

---

## 2. SEO & Content Gaps

### 2.1 Missing Pages / Content

| Gap | Why It Matters |
|-----|----------------|
| **No dedicated Service Pages** | Each of the 3 services (attic flooring, fence staining, concrete) deserves its own page with keyword-rich content, process description, FAQs, and a lead form. Homepage alone can't target all service keywords. |
| **No About Page** | Competitors use this to build trust (team photos, company story, licensing info). Absence reads as a red flag to suspicious homeowners. |
| **No Blog** | Top-ranking contractor sites publish seasonal guides ("How to Prepare Your Fence for Houston Summers", "Attic Ventilation 101"). No blog = no long-tail organic traffic. |
| **No FAQ Page / FAQ Schema** | FAQ schema boosts SERP real estate via rich snippets. Missing from both markup and content. |
| **No project portfolio page** | Only 3 static gallery cards on homepage. A proper portfolio with filtering by service/location would dramatically improve engagement and SEO. |
| **No sitemap.xml or robots.txt** | Basic SEO infrastructure missing. |
| **No canonical URL** | `<link rel="canonical">` not set — creates duplicate content risk. |
| **hreflang missing** | Not applicable unless multilingual, but worth noting if English/Spanish versions are planned (Houston is heavily bilingual market). |

### 2.2 Content Depth Issues

- **Service descriptions are thin.** The 3 service cards have ~40–60 words each. Top competitors have 300–500 word service pages.
- **Testimonials are minimal.** Only 1 customer quote on the entire site. Most competitors display 4–8 testimonials with names, photos, and Google review stars.
- **Stats are unverifiable.** "5★ Google Rating" and "100% Satisfaction" are bold claims with no attribution or link to the review source.
- **No local keywords beyond city names.** Missing neighborhood-level keywords (e.g., "attic flooring Cinco Ranch", "fence staining Memorial") that capture high-intent local searches.
- **No alt text audit performed** on gallery images (images have alt attributes but should be verified for descriptive accuracy).

### 2.3 Technical SEO

- **No lazy loading** on gallery images or Vimeo embeds — hurts Core Web Vitals LCP.
- **No resource hints** (preconnect, dns-prefetch) for Vimeo, Google Fonts, or CDN domains.
- **Images lack explicit width/height attributes** — contributes to CLS (Cumulative Layout Shift).
- **No structured data beyond Contractor schema.** Consider adding `Review`, `LocalBusiness`, and `FAQPage` schemas.

---

## 3. UX & Conversion Rate Optimization (CRO) Gaps

### 3.1 Trust & Credibility

| Gap | Severity |
|-----|----------|
| No Google Reviews widget or linked rating | High — "5★ Google Rating" claim with no clickable proof loses credibility instantly. |
| No license/insurance badge images displayed | Medium-High — competitors prominently display "Fully Insured", "BBB A+", "Angie's List" logos. |
| Only 1 testimonial on site | Medium — social proof is thin. Most Houston contractors show 4–8 reviews. |
| No company address on footer | Low-Medium — only "Greater Houston, TX" with no street address. Google Business Profile requires consistent NAP. |

### 3.2 Lead Capture Friction

| Gap | Severity |
|-----|----------|
| No sticky mobile footer bar with phone number | High — mobile users must scroll up to find the call button. A sticky "tap to call" bar at the bottom of mobile screens is standard for contractor sites and dramatically increases phone leads. |
| No WhatsApp or SMS lead option | Medium — many homeowners prefer texting to calling. A "Text Us" or WhatsApp CTA reduces friction. |
| Quote form exists but is not prominently anchored | Medium — on the homepage, the quote form is at the bottom of the page (indexed as `#quote` but never actually appears in the HTML body, only in gallery.html's CTA). **There is no visible quote request form on `index.html`.** |

### 3.3 Navigation & Flow

| Gap | Severity |
|-----|----------|
| `#quote` anchor in nav/CTA links to a non-existent section on index.html | High — clicking "Get Quote" or "Request Free Estimate" from index.html leads nowhere. The actual form lives only in `gallery.html`. |
| Phone number inconsistency | Medium — `gallery.html` footer has `+12815550199` while `index.html` uses `+12398224568`. Same company, two different numbers is a trust killer. |
| No "Request Quote" CTA inside service cards | Medium — after reading a service description, users must scroll to find the quote form. A inline "Get a Quote" button in each card would shorten the path. |

### 3.4 Media & Engagement

- Vimeo embeds auto-play muted (good) but load on page visit even if below fold — **add `loading="lazy"` or Intersection Observer** to defer off-screen video loads and improve LCP.
- No photo lightbox/gallery modal — static images in gallery.html don't give users a full-screen experience.
- No "Share this project" or social proof embed (Nextdoor, Facebook) on completed projects.

---

## 4. Actionable Phase 2 Roadmap

Prioritized by estimated impact on lead generation and SEO ranking.

### P0 — Fix Broken Lead Flow (Do First)

1. **Add the missing quote form to `index.html`** anchored at `#quote`. The `#quote` links in nav and CTAs currently point to nothing on the homepage.
2. **Fix phone number inconsistency.** Audit all phone numbers across files — there are at least 3 different numbers in the codebase (`+12398224568`, `+12815550199`, `+12815550199` in gallery.html footer). Consolidate to one canonical number.
3. **Add sticky mobile "Tap to Call" footer bar** on all pages — a fixed bottom bar on mobile that shows the phone number and a "Call Now" button. Industry standard for contractor conversion optimization.

### P1 — Trust Building (High Impact)

4. **Add Google Reviews widget or section.** Link the "5★ Google Rating" claim to the actual Google Business Profile. Display 3–5 recent reviews with names, star ratings, and review date. If no Google profile exists, create and claim it first.
5. **Add insurance/license trust badges.** Display logos for: General Liability Insurance, Workers' Comp, and any state contractor license numbers.
6. **Expand testimonials to 4–8.** Each should include: customer name, city, service performed, star rating, and ideally a photo avatar.

### P2 — SEO Infrastructure (High Impact)

7. **Create dedicated service pages** at `/attic-flooring`, `/fence-staining`, `/concrete-work` — each with 400+ words of unique content, FAQs, process description, and embedded lead form.
8. **Add FAQ schema and FAQ page** targeting question-keyword phrases ("how much does attic flooring cost houston", "how long does fence stain take").
9. **Add `sitemap.xml` and `robots.txt`** to public root and server config.
10. **Add canonical URL meta tag** to all pages.
11. **Add `hreflang`** if English/Spanish versions are planned (strongly recommended for Houston market).

### P3 — Technical Performance (Medium Impact)

12. **Lazy-load off-screen Vimeo embeds** using Intersection Observer so videos below the fold don't hit network until scrolled into view.
13. **Add explicit `width`/`height` attributes** to all `<img>` tags to eliminate CLS.
14. **Add `preconnect` resource hints** for `fonts.googleapis.com`, `fonts.gstatic.com`, `cdn.tailwindcss.com`, `player.vimeo.com`.
15. **Consider converting from Tailwind CDN to a build step** (Vite/Webpack) for production — CDN Tailwind can't be cached long-term and generates larger-than-necessary CSS bundles.

### P4 — Content & Engagement (Medium Impact)

16. **Build project portfolio page** with filter by service type and location. Include 8–12 projects with descriptions, before/after images, and project specs.
17. **Add an About page** with company story, team photo, and licensing info.
18. **Add a blog** with at least 4 seed posts: seasonal maintenance guides targeting long-tail Houston contractor keywords.

---

## 5. Summary Scorecard

| Category | Score (1–10) | Notes |
|----------|-------------|-------|
| Semantic HTML & Structure | 8 | Clean, well-organized. Minor room for improvement in heading hierarchy documentation. |
| SEO Foundation | 6 | Good meta/base, weak on technical SEO (no sitemap, no canonical, no schema beyond Contractor). |
| Content Depth | 4 | Service descriptions are thin. No blog, no dedicated service pages. |
| Trust & Credibility | 5 | One testimonial, unverifiable stats, no review links, no insurance badges. |
| Mobile UX / CRO | 5 | Good mobile layout, but missing sticky call bar, broken quote form anchor, and inconsistent phone numbers. |
| Media & Engagement | 7 | Vimeo integration is strong. Gallery is functional but basic. No lightbox or social embeds. |
| Performance | 6 | Tailwind CDN, no lazy loading, no resource hints. Room for improvement. |
| **Overall** | **~6 / 10** | Functional MVP. Competitive but not commanding. The P0 fixes (especially the broken quote form) should be addressed before any marketing spend. |

---

*Audit completed by El Padrino. Next action: await Maestra's direction on which Phase 2 items to execute first.*
