#!/usr/bin/env python3
import os, re

PUBLIC = '/root/f13-work-seo/public'
CANONICAL = open(os.path.join(PUBLIC, 'footer-canonical.html')).read()

# files still with old footer
files = [
    'gallery.html',
    'concrete/driveway-extensions/cypress-tx/index.html',
    'concrete/driveway-extensions/index.html',
    'concrete/driveway-extensions/katy-tx/index.html',
    'concrete/patio-slabs/cypress-tx/index.html',
    'concrete/patio-slabs/index.html',
    'concrete/patio-slabs/katy-tx/index.html',
    'concrete/trash-can-pad-installation/cypress-tx/index.html',
    'concrete/trash-can-pad-installation/index.html',
    'concrete/trash-can-pad-installation/katy-tx/index.html',
    'concrete/trash-can-pad-installation/sugar-land-tx/index.html',
]

for f in files:
    path = os.path.join(PUBLIC, f)
    content = open(path).read()
    
    # Find old footer: from <!-- FOOTER --> to </footer> followed by newline and optional whitespace
    # The old footer pattern is: <!-- FOOTER -->\n  <footer class="bg-navy-950 text-white pt-12 pb-8...
    old_match = re.search(
        r'<!-- FOOTER -->\s*<footer class="bg-navy-950 text-white pt-12 pb-8[^>]*>.*?</footer>',
        content, re.DOTALL
    )
    if old_match:
        old_footer = old_match.group(0)
        new_content = content.replace(old_footer, CANONICAL)
        with open(path, 'w') as fh:
            fh.write(new_content)
        print(f"OK: {f}")
    else:
        print(f"SKIP: {f} - no old footer found")
