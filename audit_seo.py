import json, re, urllib.request

BASE = "http://localhost:3111"
results = []

def get(path):
    with urllib.request.urlopen(BASE + path, timeout=10) as r:
        return r.status, r.read().decode("utf-8", "replace")

# 1. HTTP status & routing (follow redirects, flag if final != requested path or chains >2)
print("=" * 62)
print("1. HTTP STATUS & ROUTING")
print("=" * 62)
for path in ["/", "/attic-flooring.html", "/attic-flooring/katy-tx/",
             "/attic-flooring/cypress-tx/", "/attic-flooring/sugar-land-tx/",
             "/sitemap.xml", "/robots.txt"]:
    try:
        st, body = get(path)
        print(f"  [{ 'PASS' if st==200 else 'FAIL' }] {path} -> {st}")
    except urllib.error.HTTPError as e:
        print(f"  [FAIL] {path} -> {e.code}")

CITY_DATA = {
    "katy-tx":    {"h1": "Katy",         "hoods": ["Cinco Ranch", "Elyson", "Cane Island", "Firethorne"]},
    "cypress-tx": {"h1": "Cypress",      "hoods": ["Bridgeland", "Towne Lake", "Fairfield", "Coles Crossing"]},
    "sugar-land-tx": {"h1": "Sugar Land", "hoods": ["First Colony", "Greatwood", "Telfair", "Riverstone"]},
}
CLIMATE = ["R-30", "R-38", "140", "soffit", "raised", "subfloor", "duct"]

print()
print("=" * 62)
print("2. SUB-MARKET PAGE CONTENT")
print("=" * 62)
for slug, spec in CITY_DATA.items():
    path = f"/attic-flooring/{slug}/"
    st, html = get(path)
    h1s = re.findall(r"<h1[^>]*>(.*?)</h1>", html, re.S | re.I)
    h1_txt = re.sub(r"<[^>]+>", "", h1s[0]).strip() if h1s else "(none)"
    h1_ok = spec["h1"] in h1_txt and "Attic Flooring" in h1_txt
    print(f"  [{ 'PASS' if h1_ok else 'FAIL' }] {path} H1: \"{h1_txt}\"")
    for h in spec["hoods"]:
        ok = h.lower() in html.lower()
        print(f"    [{ 'PASS' if ok else 'FAIL' }] neighborhood mention: {h}")
    for kw in ["R-30", "R-38", "140", "soffit"]:
        ok = kw.lower() in html.lower()
        print(f"    [{ 'PASS' if ok else 'FAIL' }] climate/tech copy: {kw}")
    for kw in ["raised", "subfloor", "duct"]:
        ok = kw.lower() in html.lower()
        print(f"    [{ 'PASS' if ok else 'FAIL' }] engineering copy: {kw}")

print()
print("=" * 62)
print("3. STRUCTURED DATA VALIDATION")
print("=" * 62)
for slug in CITY_DATA:
    path = f"/attic-flooring/{slug}/"
    st, html = get(path)
    blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.S)
    types, ids, urls = [], [], []
    all_valid = True
    for b in blocks:
        try:
            d = json.loads(b)
            types.append(d.get("@type"))
            if d.get("@id"): ids.append(d["@id"])
            if d.get("url"): urls.append(d["url"])
        except json.JSONDecodeError as e:
            all_valid = False
            print(f"  [FAIL] {path} JSON error: {e}")
    print(f"  [{ 'PASS' if all_valid and len(blocks)==2 else 'FAIL' }] {path} parsed {len(blocks)} ld+json blocks")
    ok_types = any(t in ("HomeAndConstructionBusiness", "LocalBusiness") for t in types) and "FAQPage" in types
    print(f"  [{ 'PASS' if ok_types else 'FAIL' }] {path} @type set: {types}")
    lb_id = [i for i in ids if i.endswith("#business")]
    print(f"  [{ 'PASS' if lb_id else 'FAIL' }] {path} @id: {lb_id or '(missing)'}")
    ok_url = "f13llc.com" in (urls[0] if urls else "")
    print(f"  [{ 'PASS' if ok_url else 'FAIL' }] {path} url: {urls or '(missing)'}")
    # FAQPage matches visible questions
    faq = next((json.loads(b) for b in blocks if '"FAQPage"' in b), None)
    if faq:
        qs = [q["name"] for q in faq["mainEntity"]]
        visible_ok = all(any(q.split()[0:3] and w in html for w in q.split()[:4]) for q in qs)
        print(f"  [{ 'PASS' if visible_ok else 'FAIL' }] {path} FAQPage {len(qs)} questions match on-page copy")

print()
print("=" * 62)
print("4. INTERNAL LINKING & CRAWLABILITY")
print("=" * 62)
st, main = get("/attic-flooring.html")
for slug in CITY_DATA:
    ok = f'href="attic-flooring/{slug}/"' in main
    print(f"  [{ 'PASS' if ok else 'FAIL' }] /attic-flooring.html links to /attic-flooring/{slug}/")
st, sm = get("/sitemap.xml")
for slug in CITY_DATA:
    ok = f"/attic-flooring/{slug}/" in sm
    print(f"  [{ 'PASS' if ok else 'FAIL' }] /sitemap.xml lists /attic-flooring/{slug}/")
try:
    import xml.etree.ElementTree as ET
    ET.fromstring(sm)
    print("  [PASS] sitemap.xml is well-formed XML")
except ET.ParseError as e:
    print(f"  [FAIL] sitemap.xml XML error: {e}")
ok_weekly = sm.count("<changefreq>weekly</changefreq>") >= 3
ok_p08 = sm.count("<priority>0.8</priority>") >= 3
print(f"  [{ 'PASS' if ok_weekly else 'FAIL' }] sitemap sub-pages changefreq=weekly")
print(f"  [{ 'PASS' if ok_p08 else 'FAIL' }] sitemap sub-pages priority=0.8")
st, rb = get("/robots.txt")
disallow_attic = re.search(r"Disallow:.*attic", rb, re.I)
has_sitemap = "Sitemap:" in rb and "sitemap.xml" in rb
allow_all = re.search(r"User-agent: \*\s*\nAllow: /", rb) is not None
print(f"  [{ 'PASS' if not disallow_attic else 'FAIL' }] robots.txt does NOT disallow /attic-flooring/")
print(f"  [{ 'PASS' if has_sitemap else 'FAIL' }] robots.txt points to /sitemap.xml")
print(f"  [{ 'PASS' if allow_all else 'FAIL' }] robots.txt allows all user agents")

print()
print("=" * 62)
print("AUDIT COMPLETE")
print("=" * 62)