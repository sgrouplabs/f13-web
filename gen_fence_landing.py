# Generate F13 LLC fence-staining geo landing pages (mirrors gen_landing.py template)
import json, os

PUB = "/root/f13-web/public"
PHONE_HREF = "tel:+123****4568"
PHONE_TXT = "(239) 822-4568"
SITE = "https://f13llc.com"

CITIES = {
    "katy": {
        "name": "Katy", "zips": "77494, 77493, 77450",
        "communities": "Cinco Ranch, Elyson, Cane Island, and Firethorne",
        "geo": (29.7858, -95.8245),
        "blurb": "Katy's fast-growing master-planned neighborhoods — Cinco Ranch, Elyson, Cane Island, and Firethorne — are full of brand-new cedar pine fences that take a beating from Gulf Coast sun and humidity. A professionally stained fence resists rot, fading, and warping for years. We serve all of Katy including the 77494, 77493, and 77450 zip codes.",
        "slug": "fence-staining/katy-tx",
    },
    "cypress": {
        "name": "Cypress", "zips": "77433, 77429",
        "communities": "Bridgeland, Towne Lake, Fairfield, and Coles Crossing",
        "geo": (29.9691, -95.6972),
        "blurb": "From Bridgeland and Towne Lake to Fairfield and Coles Crossing, Cypress's newer subdivisions have thousands of feet of unstained builder-grade fencing. Sealing it now is the cheapest way to double its life. We serve all of Cypress including the 77433 and 77429 zip codes.",
        "slug": "fence-staining/cypress-tx",
    },
    "sugar-land": {
        "name": "Sugar Land", "zips": "77479, 77478",
        "communities": "First Colony, Greatwood, Telfair, and Riverstone",
        "geo": (29.5994, -95.6142),
        "blurb": "Sugar Land's established neighborhoods — First Colony, Greatwood, Telfair, and Riverstone — have mature wood fences that need periodic staining to stay weather-tight and HOA-sharp. We serve all of Sugar Land including the 77479 and 77478 zip codes.",
        "slug": "fence-staining/sugar-land-tx",
    },
}

FAQS = [
    ("How long does fence staining last in {city}, TX?",
     "In the Houston climate, a quality stain applied to properly prepped wood typically holds its color and protection for 3 to 5 years. Houston humidity and UV exposure are the main drivers — that's why we only use exterior-grade stains rated for Gulf Coast weather and re-application schedules that fit {city} conditions."),
    ("Do you pressure wash before staining?",
     "Yes — surface prep is the difference between stain that lasts and stain that peels. Every fence we stain in {city} gets cleaned first to remove mildew, dirt, and grayed wood fibers, then allowed to dry to the correct moisture level before we apply any stain."),
    ("Is staining better than painting a fence?",
     "For wood fences, staining wins almost every time. Stain soaks into the wood instead of sitting on top like paint, so it won't chip, peel, or blister. It moves with the wood as it expands and contracts through Houston's humidity swings, and touch-ups are far easier."),
    ("How much does fence staining cost in {city}?",
     "Pricing depends on fence height, condition, and whether it needs cleaning or repairs first. We give free in-person quotes throughout {city} and the surrounding {zips} zip codes — we walk the fence line, measure, and give you an honest, no-pressure price."),
]

PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Fence Staining in {city}, TX | F13 LLC — Stain &amp; Seal Wood Fences</title>
  <meta name="description" content="Professional fence staining and sealing in {city}, TX. F13 LLC power washes, repairs, and stains wood fences for {communities} and {zips}. Free on-site estimate.">
  <meta name="robots" content="index, follow">
  <meta property="og:title" content="Fence Staining in {city}, TX | F13 LLC">
  <meta property="og:description" content="Fence staining engineered for Houston humidity and sun. Serving {communities} and the {zips} zip codes. Free in-person estimate.">
  <meta property="og:type" content="website">
  <link rel="canonical" href="{site}/{slug}/">

  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
  <script>
    tailwind.config = {{ theme: {{ extend: {{ fontFamily: {{ sans: ['Inter','system-ui','sans-serif'] }}, colors: {{ navy: {{ 700:'#1e3a5f', 800:'#1a3354', 900:'#0f2342', 950:'#0a1a33' }} }} }} }} }}
  </script>

  <script type="application/ld+json">
  {localbusiness_json}
  </script>
  <script type="application/ld+json">
  {faq_json}
  </script>

  <link rel="stylesheet" href="/css/styles.css">
</head>
<body class="font-sans text-gray-800 antialiased bg-white">

  <header id="site-header" class="sticky top-0 z-50 bg-white shadow-sm border-b border-gray-100">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-16 lg:h-20">
        <a href="/index.html" class="flex items-center gap-3 group">
          <div class="w-10 h-10 bg-navy-900 rounded-lg flex items-center justify-center shadow-md group-hover:bg-navy-700 transition-colors">
            <img loading="lazy" decoding="async" src="/brand/f13-logo-512px.png" alt="F13 LLC Logo" class="h-10 w-auto object-contain">
          </div>
          <div class="hidden sm:block">
            <p class="text-navy-900 font-bold text-lg leading-none">F13 LLC</p>
            <p class="text-gray-400 text-[10px] uppercase tracking-widest leading-none mt-0.5">Katy, TX</p>
          </div>
        </a>
        <nav class="hidden lg:flex items-center gap-8">
          <a href="/index.html#services" class="text-slate-800 hover:text-blue-600 font-bold text-xl transition-colors px-3">Services</a>
          <a href="/gallery.html" class="text-slate-800 hover:text-blue-600 font-bold text-xl transition-colors px-3">Gallery</a>
          <a href="/fence-staining.html" class="text-slate-800 hover:text-blue-600 font-bold text-xl transition-colors px-3">Fence Staining</a>
        </nav>
        <div class="flex items-center gap-3">
          <a href="{phone_href}" class="flex items-center gap-2 bg-navy-900 hover:bg-slate-800 text-white font-bold text-sm px-4 py-2.5 rounded-lg shadow-md transition-all">
            <i class="fa-solid fa-phone text-xs"></i><span class="hidden sm:inline">Call Now</span>
          </a>
        </div>
      </div>
    </div>
  </header>

  <!-- HERO -->
  <section class="bg-navy-950 text-white py-20">
    <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
      <p class="text-blue-400 font-bold uppercase tracking-widest text-sm mb-3">Serving {city}, TX &amp; the {zips} Zip Codes</p>
      <h1 class="text-3xl sm:text-4xl lg:text-5xl font-extrabold leading-tight mb-5">Fence Staining &amp; Sealing in {city}, TX</h1>
      <p class="text-blue-200 text-lg mb-8 max-w-3xl">Houston's humidity and blazing sun destroy untreated wood fences fast. F13 LLC cleans, preps, and stains fences across {city} so they seal out moisture and UV damage — and keep their color for years, not months.</p>
      <div class="flex flex-col sm:flex-row gap-4">
        <a href="{phone_href}" class="inline-flex items-center justify-center gap-2 bg-white text-navy-900 font-bold text-lg px-8 py-4 rounded-xl shadow-lg hover:bg-gray-100 transition-all">
          <i class="fa-solid fa-phone"></i> Get a Free Quote — {phone_txt}
        </a>
        <a href="/gallery.html" class="inline-flex items-center justify-center gap-2 border-2 border-blue-400 text-blue-200 hover:bg-blue-900/40 font-bold text-lg px-8 py-4 rounded-xl transition-all">
          <i class="fa-solid fa-images"></i> See Our Work
        </a>
      </div>
    </div>
  </section>

  <!-- LOCAL INTRO -->
  <section class="py-16 bg-white">
    <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
      <h2 class="text-2xl font-extrabold text-navy-900 mb-6">Fence Staining Built for {city} Weather</h2>
      <div class="prose prose-gray max-w-none text-gray-600 leading-relaxed">
        <p class="mb-4">{blurb}</p>
      </div>

      <!-- Why-stain differentiators -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mt-10 mb-6">
        <div class="bg-gray-50 rounded-2xl p-6 border border-gray-200">
          <div class="w-12 h-12 bg-navy-900/10 rounded-xl flex items-center justify-center mb-4"><i class="fa-solid fa-sun text-navy-900 text-xl"></i></div>
          <h3 class="font-bold text-navy-900 text-lg mb-2">UV &amp; Fade Protection</h3>
          <p class="text-gray-500 text-sm leading-relaxed">Houston sun grays and cracks untreated wood within a couple of seasons. Quality stain blocks UV damage and keeps your fence's rich color far longer.</p>
        </div>
        <div class="bg-gray-50 rounded-2xl p-6 border border-gray-200">
          <div class="w-12 h-12 bg-navy-900/10 rounded-xl flex items-center justify-center mb-4"><i class="fa-solid fa-droplet text-navy-900 text-xl"></i></div>
          <h3 class="font-bold text-navy-900 text-lg mb-2">Sealed Against Humidity</h3>
          <p class="text-gray-500 text-sm leading-relaxed">Gulf Coast moisture warps boards and feeds rot and mildew. Staining seals the wood so it sheds rain and holds its shape through Houston's humidity swings.</p>
        </div>
        <div class="bg-gray-50 rounded-2xl p-6 border border-gray-200">
          <div class="w-12 h-12 bg-navy-900/10 rounded-xl flex items-center justify-center mb-4"><i class="fa-solid fa-screwdriver-wrench text-navy-900 text-xl"></i></div>
          <h3 class="font-bold text-navy-900 text-lg mb-2">Prep Done Right</h3>
          <p class="text-gray-500 text-sm leading-relaxed">We power wash, remove mildew and grayed fibers, and let the wood reach the right moisture level before staining — because prep is what makes stain last.</p>
        </div>
      </div>
      <div class="prose prose-gray max-w-none text-gray-600 leading-relaxed mt-8">
        <p class="mb-4">Every job starts with a fence-line walk-through: we check board condition, fasteners, and previous coatings, then recommend the right stain system for your wood type and sun exposure. A stained fence costs a fraction of a replacement — and staining every few years is the cheapest way to add years of life to the fence you already have.</p>
      </div>
    </div>
  </section>

  <!-- NEIGHBORHOODS -->
  <section class="py-16 bg-gray-50 border-t border-gray-200">
    <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
      <h2 class="text-2xl font-extrabold text-navy-900 mb-6">Proudly Serving {city} Neighborhoods</h2>
      <p class="text-gray-600 mb-8 max-w-3xl">{communities_intro}</p>
      <div class="flex flex-wrap gap-3">
        {{community_chips}}
      </div>
      <p class="text-gray-500 text-sm mt-6">Zip codes served in {city}: <strong>{zips}</strong>. Don't see your neighborhood? Call us — we cover all of Greater Houston.</p>
    </div>
  </section>

  <!-- FAQ -->
  <section class="py-16 bg-white">
    <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
      <h2 class="text-2xl font-extrabold text-navy-900 mb-8 text-center">Fence Staining FAQs — {city}, TX</h2>
      <div class="space-y-4">
        {faq_items}
      </div>
    </div>
  </section>

  <!-- CTA -->
  <section class="py-16 bg-navy-900">
    <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
      <h2 class="text-2xl font-extrabold text-white mb-3">Ready to Protect Your Fence in {city}?</h2>
      <p class="text-blue-200 mb-8 max-w-xl mx-auto text-sm">Get a free, no-obligation on-site estimate anywhere in {city} or the {zips} zip codes. We walk the fence, explain your options, and give you an honest price — no pressure.</p>
      <a href="{phone_href}" class="inline-flex items-center gap-2 bg-white text-navy-900 font-bold text-lg px-8 py-4 rounded-xl shadow-lg hover:bg-gray-100 transition-all">
        <i class="fa-solid fa-phone"></i> Call {phone_txt}
      </a>
    </div>
  </section>

  <!-- FOOTER -->
  <footer class="bg-navy-950 text-white pt-12 pb-8">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 md:grid-cols-4 gap-8 mb-10">
        <div>
          <div class="flex items-center gap-3 mb-4">
            <div class="w-10 h-10 bg-navy-800 rounded-lg flex items-center justify-center">
              <img loading="lazy" decoding="async" src="/brand/f13-logo-512px.png" alt="F13 LLC Logo" class="h-10 w-auto object-contain">
            </div>
            <div>
              <p class="font-bold text-white">F13 LLC</p>
              <p class="text-gray-400 text-xs">Katy, TX</p>
            </div>
          </div>
          <p class="text-gray-400 text-sm">Trusted general contracting and specialized home upgrades for the Greater Houston area.</p>
        </div>
        <div>
          <h4 class="text-white font-bold mb-4">Services</h4>
          <ul class="space-y-2 text-gray-400 text-sm">
            <li><a href="/attic-flooring.html" class="hover:text-white transition-colors">Attic Flooring</a></li>
            <li><a href="/fence-staining.html" class="hover:text-white transition-colors">Fence Staining</a></li>
            <li><a href="/concrete-contractor.html" class="hover:text-white transition-colors">Concrete Contractor</a></li>
          </ul>
        </div>
        <div>
          <h4 class="text-white font-bold mb-4">Fence Staining Service Areas</h4>
          <ul class="space-y-2 text-gray-400 text-sm">
            <li><a href="/fence-staining/katy-tx/index.html" class="hover:text-white transition-colors">Katy, TX</a></li>
            <li><a href="/fence-staining/cypress-tx/index.html" class="hover:text-white transition-colors">Cypress, TX</a></li>
            <li><a href="/fence-staining/sugar-land-tx/index.html" class="hover:text-white transition-colors">Sugar Land, TX</a></li>
            <li><a href="/fence-staining.html" class="hover:text-white transition-colors">All Greater Houston</a></li>
          </ul>
        </div>
        <div>
          <h4 class="text-white font-bold mb-4">Contact</h4>
          <ul class="space-y-2 text-gray-400 text-sm">
            <li><i class="fa-solid fa-phone mr-2"></i><a href="{phone_href}" class="hover:text-white">{phone_txt}</a></li>
            <li><i class="fa-solid fa-clock mr-2"></i>Mon&ndash;Fri 8am&ndash;6pm</li>
          </ul>
        </div>
      </div>
      <div class="border-t border-navy-800 pt-6 flex flex-col sm:flex-row items-center justify-between gap-4 text-sm text-blue-400">
        <p>&copy; 2026 F13 LLC. All rights reserved.</p>
        <div class="flex gap-4">
          <a href="/gallery.html" class="hover:text-white transition-colors">Gallery</a>
          <a href="/index.html#services" class="hover:text-white transition-colors">Services</a>
        </div>
      </div>
    </div>
  </footer>
  <script src="/js/main.js"></script>
</body>
</html>
"""

FAQ_ITEM = """<details class="bg-gray-50 rounded-xl border border-gray-200 p-5" {open}>
  <summary class="font-bold text-navy-900 cursor-pointer">{q}</summary>
  <p class="text-gray-600 text-sm leading-relaxed mt-3">{a}</p>
</details>"""

os.makedirs(PUB, exist_ok=True)
for key, c in CITIES.items():
    city = c["name"]
    slug = c["slug"]
    faqs = [(q, a.replace("{city}", city).replace("{zips}", c["zips"])) for q, a in FAQS]

    localbusiness = {
        "@context": "https://schema.org",
        "@type": "HomeAndConstructionBusiness",
        "@id": "https://f13llc.com/#business",
        "name": "F13 LLC",
        "url": "https://f13llc.com",
        "telephone": "+1-239-822-4568",
        "priceRange": "$$",
        "address": {"@type": "PostalAddress", "addressLocality": city,
                    "addressRegion": "TX", "addressCountry": "US"},
        "geo": {"@type": "GeoCoordinates",
                "latitude": c["geo"][0], "longitude": c["geo"][1]},
        "areaServed": [{"@type": "City", "name": city,
                        "sameAs": "https://en.wikipedia.org/wiki/" + city.replace(" ", "_") + ",_Texas"}],
        "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Fence Services",
                            "itemListElement": [{"@type": "Offer", "itemOffered": {
                                "@type": "Service",
                                "name": "Fence Staining & Sealing",
                                "description": "Professional fence staining, sealing, and power washing protection for wood fences in " + city + ", TX."}}]},
    }
    faqpage = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q,
                        "acceptedAnswer": {"@type": "Answer", "text": a}}
                       for q, a in faqs],
    }

    comm_intro = (f"F13 LLC stains and seals fences throughout {c['communities']} and across "
                  f"the {c['zips']} zip codes — bringing the same professional prep-and-stain "
                  f"process to every {city} neighborhood we serve.")
    chips = "".join(
        f'<span class="bg-white border border-gray-200 rounded-full px-4 py-2 text-sm font-semibold text-navy-900 shadow-sm">{n}</span>'
        for n in [s.strip() for s in c["communities"].split(",")])

    faq_items = "".join(
        FAQ_ITEM.format(open='open' if i == 0 else '', q=q, a=a)
        for i, (q, a) in enumerate(faqs))

    html = PAGE.format(
        city=city, zips=c["zips"], communities=c["communities"],
        communities_intro=comm_intro, blurb=c["blurb"], slug=slug, site=SITE,
        phone_href=PHONE_HREF, phone_txt=PHONE_TXT,
        localbusiness_json=json.dumps(localbusiness, indent=2),
        faq_json=json.dumps(faqpage, indent=2),
        faq_items=faq_items,
    )
    outdir = os.path.join(PUB, slug)
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "index.html"), "w") as f:
        f.write(html)
    print("wrote", outdir + "/index.html", len(html), "bytes")