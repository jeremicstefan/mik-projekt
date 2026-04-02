#!/usr/bin/env python3
"""Batch-update all existing HTML files to add O nama dropdown."""

import re, os, glob

FILES = glob.glob(os.path.join(os.path.dirname(__file__), '*.html'))
FILES = [f for f in FILES if os.path.basename(f) not in
         ('kontakt.html','karijera.html','cesta-pitanja.html',
          'odrzivost.html','pravne-napomene.html','logo-variants.html')]

# ── 1. Nav <li> replacement ─────────────────────────────────────────────────

LI_PLAIN = '<li><a href="o-nama.html">O nama</a></li>'
LI_ACTIVE = '<li><a href="o-nama.html" class="active">O nama</a></li>'

DROPDOWN_PLAIN = '''\
<li class="nav-mega-item" id="aboutItem">
          <a href="o-nama.html" class="nav-mega-trigger">
            O nama
            <svg class="nav-mega-chevron" viewBox="0 0 10 10" xmlns="http://www.w3.org/2000/svg">
              <polyline points="1,3 5,7 9,3" stroke="currentColor" stroke-width="1.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </a>
          <div class="about-dropdown" id="aboutDropdown">
            <a href="kontakt.html">Kontakt</a>
            <a href="karijera.html">Karijera</a>
            <a href="cesta-pitanja.html">&#268;esta pitanja</a>
            <a href="odrzivost.html">Odr&#382;ivost</a>
            <a href="pravne-napomene.html">Pravne napomene</a>
          </div>
        </li>'''

DROPDOWN_ACTIVE = '''\
<li class="nav-mega-item" id="aboutItem">
          <a href="o-nama.html" class="nav-mega-trigger active">
            O nama
            <svg class="nav-mega-chevron" viewBox="0 0 10 10" xmlns="http://www.w3.org/2000/svg">
              <polyline points="1,3 5,7 9,3" stroke="currentColor" stroke-width="1.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </a>
          <div class="about-dropdown" id="aboutDropdown">
            <a href="kontakt.html">Kontakt</a>
            <a href="karijera.html">Karijera</a>
            <a href="cesta-pitanja.html">&#268;esta pitanja</a>
            <a href="odrzivost.html">Odr&#382;ivost</a>
            <a href="pravne-napomene.html">Pravne napomene</a>
          </div>
        </li>'''

# ── 2. CSS to inject ────────────────────────────────────────────────────────

CSS_ANCHOR = '.mega-open .nav-mega-chevron { transform: rotate(180deg); }'

CSS_INJECT = '''
    .about-dropdown {
      position: absolute;
      top: calc(100% + 8px);
      left: 50%;
      transform: translateX(-50%) translateY(4px);
      background: #fff;
      border: 1px solid var(--border);
      border-radius: 8px;
      box-shadow: 0 8px 32px rgba(0,0,0,0.12);
      min-width: 200px;
      padding: 6px;
      display: flex;
      flex-direction: column;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.18s, transform 0.18s;
      z-index: 200;
    }
    .nav-mega-item.mega-open .about-dropdown {
      opacity: 1;
      pointer-events: auto;
      transform: translateX(-50%) translateY(0);
    }
    .about-dropdown a {
      font-size: 14px;
      color: var(--dark);
      text-decoration: none;
      padding: 8px 12px;
      border-radius: 5px;
      transition: background 0.15s;
      white-space: nowrap;
    }
    .about-dropdown a:hover { background: var(--gray-bg); }
    @media (max-width: 860px) {
      .about-dropdown { display: none; }
      .drawer-sub { display: flex; flex-direction: column; }
      .drawer-sub a { font-size: 13px; color: var(--text-muted); padding: 6px 16px 6px 28px; text-decoration: none; display: block; }
      .drawer-sub a:hover { color: var(--dark); }
    }'''

# ── 3. JS to inject ─────────────────────────────────────────────────────────

# Inject before the reveals querySelectorAll line (present in all files)
JS_ANCHOR_PAT = re.compile(
    r"(    const reveals\s+=\s+document\.querySelectorAll\('\.reveal'\);)",
    re.MULTILINE
)

JS_INJECT = """
    // ─── About dropdown ──────────────────────────────────────────
    const aboutItem = document.getElementById('aboutItem');
    if (aboutItem) {
      let aboutTimer;
      const openAbout  = () => { clearTimeout(aboutTimer); aboutItem.classList.add('mega-open'); };
      const closeAbout = () => { aboutTimer = setTimeout(() => aboutItem.classList.remove('mega-open'), 120); };
      aboutItem.addEventListener('mouseenter', openAbout);
      aboutItem.addEventListener('mouseleave', closeAbout);
      const aboutDrop = document.getElementById('aboutDropdown');
      if (aboutDrop) {
        aboutDrop.addEventListener('mouseenter', openAbout);
        aboutDrop.addEventListener('mouseleave', closeAbout);
      }
    }"""

# ── 4. Drawer replacement ───────────────────────────────────────────────────

DRAWER_PLAIN  = '<a href="o-nama.html" onclick="closeDrawer()">O nama</a>'
DRAWER_ACTIVE = '<a href="o-nama.html" class="active" onclick="closeDrawer()">O nama</a>'

DRAWER_SUB = '''
    <div class="drawer-sub">
      <a href="kontakt.html" onclick="closeDrawer()">Kontakt</a>
      <a href="karijera.html" onclick="closeDrawer()">Karijera</a>
      <a href="cesta-pitanja.html" onclick="closeDrawer()">&#268;esta pitanja</a>
      <a href="odrzivost.html" onclick="closeDrawer()">Odr&#382;ivost</a>
      <a href="pravne-napomene.html" onclick="closeDrawer()">Pravne napomene</a>
    </div>'''

# ────────────────────────────────────────────────────────────────────────────

def patch(html, path):
    changed = False

    # Skip if already fully patched
    if 'aboutDropdown' in html and 'openAbout' in html:
        print(f'  SKIP (already patched): {os.path.basename(path)}')
        return html

    # 1. Nav li
    if LI_ACTIVE in html:
        html = html.replace(LI_ACTIVE, DROPDOWN_ACTIVE, 1)
        changed = True
    elif LI_PLAIN in html:
        html = html.replace(LI_PLAIN, DROPDOWN_PLAIN, 1)
        changed = True
    else:
        print(f'  WARN: O nama li not found in {os.path.basename(path)}')

    # 2. CSS
    if CSS_ANCHOR in html and '.about-dropdown' not in html:
        html = html.replace(CSS_ANCHOR, CSS_ANCHOR + CSS_INJECT, 1)
        changed = True

    # 3. JS
    m = JS_ANCHOR_PAT.search(html)
    if m and 'openAbout' not in html:
        insert_pos = m.start()
        html = html[:insert_pos] + JS_INJECT + '\n' + html[insert_pos:]
        changed = True
    elif 'openAbout' not in html:
        print(f'  WARN: JS anchor not found in {os.path.basename(path)}')

    # 4. Drawer
    if DRAWER_ACTIVE in html and DRAWER_SUB.strip() not in html:
        html = html.replace(DRAWER_ACTIVE, DRAWER_ACTIVE + DRAWER_SUB, 1)
        changed = True
    elif DRAWER_PLAIN in html and DRAWER_SUB.strip() not in html:
        html = html.replace(DRAWER_PLAIN, DRAWER_PLAIN + DRAWER_SUB, 1)
        changed = True

    if changed:
        print(f'  OK: {os.path.basename(path)}')
    return html


for path in sorted(FILES):
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    patched = patch(html, path)
    if patched != html:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(patched)

print('Done.')
