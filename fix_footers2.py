#!/usr/bin/env python3
import os, re

PUBLIC = '/root/f13-work-seo/public'
CANONICAL = open(os.path.join(PUBLIC, 'footer-canonical.html')).read()

files = [
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
    
    # Find old footer: <footer class="bg-navy-950 text-white pt-12 pb-8"> ... </footer>
    start = content.find('<footer class="bg-navy-950 text-white pt-12 pb-8">')
    if start == -1:
        print(f"SKIP: {f} - no old footer found")
        continue
    end = content.find('</footer>', start)
    if end == -1:
        print(f"SKIP: {f} - no closing footer")
        continue
    end += len('</footer>')
    
    old_footer = content[start:end]
    new_content = content.replace(old_footer, CANONICAL)
    with open(path, 'w') as fh:
        fh.write(new_content)
    print(f"OK: {f} (replaced {len(old_footer)} bytes)")
