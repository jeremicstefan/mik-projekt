#!/usr/bin/env python3
"""
Restructure nav across all pages:
  - O nama → plain link (no dropdown)
  - Dokumentacija → removed from main nav
  - New "Ostalo" dropdown (after Projekti) with:
      Karijera, Česta pitanja, Dokumentacija, Održivost, Pravne napomene
  - Mobile drawer updated to match
"""

import re, os, glob

FILES = sorted(glob.glob(os.path.join(os.path.dirname(__file__), '*.html')))

# ─── Pages where O nama link should be active ───────────────────────────────
ONAME_ACTIVE_PAGES = {'o-nama.html'}

# ─── Pages where Ostalo trigger should be active (sub-pages) ────────────────
OSTALO_ACTIVE_PAGES = {
    'karijera.html', 'cesta-pitanja.html', 'dokumentacija.html',
    'odrzivost.html', 'pravne-napomene.html', 'kontakt.html'
}

# ─── Chevron SVG (reusable) ─────────────────────────────────────────────────
CHEVRON = '''<svg class="nav-mega-chevron" viewBox="0 0 10 10" xmlns="http://www.w3.org/2000/svg">
              <polyline points="1,3 5,7 9,3" stroke="currentColor" stroke-width="1.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>'''

# ─── O nama replacements ─────────────────────────────────────────────────────
# Regex: match entire <li class="nav-mega-item" id="aboutItem"> ... </li> block
ONAME_BLOCK_RE = re.compile(
    r'<li class="nav-mega-item" id="aboutItem">.*?</li>',
    re.DOTALL
)

def oname_replacement(basename):
    active = ' class="active"' if basename in ONAME_ACTIVE_PAGES else ''
    return f'<li><a href="o-nama.html"{active}>O nama</a></li>'

# ─── Ostalo dropdown ─────────────────────────────────────────────────────────
def ostalo_block(basename):
    active = ' active' if basename in OSTALO_ACTIVE_PAGES else ''
    return f'''\
<li class="nav-mega-item" id="aboutItem">
          <a href="#" class="nav-mega-trigger{active}">
            Ostalo
            {CHEVRON}
          </a>
          <div class="about-dropdown" id="aboutDropdown">
            <a href="karijera.html">Karijera</a>
            <a href="cesta-pitanja.html">&#268;esta pitanja</a>
            <a href="dokumentacija.html">Dokumentacija</a>
            <a href="odrzivost.html">Odr&#382;ivost</a>
            <a href="pravne-napomene.html">Pravne napomene</a>
          </div>
        </li>'''

# ─── Dokumentacija nav li (may or may not have active) ──────────────────────
DOK_LI_RE = re.compile(
    r'\s*<li><a href="dokumentacija\.html"[^>]*>Dokumentacija</a></li>'
)

# Match Projekti li so we can insert Ostalo after it
PROJEKTI_LI_RE = re.compile(
    r'(<li><a href="projekti\.html"[^>]*>Projekti</a></li>)'
)

# ─── Drawer ──────────────────────────────────────────────────────────────────
# Old: O nama + drawer-sub block
DRAWER_ONAME_BLOCK_RE = re.compile(
    r'(<a href="o-nama\.html"[^>]*>O nama</a>)\s*<div class="drawer-sub">.*?</div>',
    re.DOTALL
)

# Old: Dokumentacija drawer link
DRAWER_DOK_RE = re.compile(
    r'\s*<a href="dokumentacija\.html" onclick="closeDrawer\(\)">[^<]+</a>'
)

# New Ostalo drawer-sub to insert after Projekti drawer link
DRAWER_PROJEKTI_RE = re.compile(
    r'(<a href="projekti\.html" onclick="closeDrawer\(\)">[^<]+</a>)'
)

DRAWER_OSTALO_SUB = '''
    <span class="drawer-label">Ostalo</span>
    <div class="drawer-sub">
      <a href="karijera.html" onclick="closeDrawer()">Karijera</a>
      <a href="cesta-pitanja.html" onclick="closeDrawer()">&#268;esta pitanja</a>
      <a href="dokumentacija.html" onclick="closeDrawer()">Dokumentacija</a>
      <a href="odrzivost.html" onclick="closeDrawer()">Odr&#382;ivost</a>
      <a href="pravne-napomene.html" onclick="closeDrawer()">Pravne napomene</a>
    </div>'''

# ─── CSS: add drawer-label style ─────────────────────────────────────────────
DRAWER_SUB_CSS_RE = re.compile(
    r'(\.drawer-sub a\s*\{[^}]+\})'
)
DRAWER_LABEL_CSS = '''
      .drawer-label { display: block; font-size: 11px; font-weight: 600; color: var(--text-dim); letter-spacing: 0.08em; padding: 14px 0 4px; border-bottom: 1px solid var(--border); }'''

# ────────────────────────────────────────────────────────────────────────────

def patch(html, basename):
    changed = False

    # 1. Replace O nama mega-item with plain link
    if 'id="aboutItem"' in html and 'O nama' in html:
        new_html = ONAME_BLOCK_RE.sub(oname_replacement(basename), html, count=1)
        if new_html != html:
            html = new_html
            changed = True

    # 2. Remove Dokumentacija from main nav li
    new_html = DOK_LI_RE.sub('', html, count=1)
    if new_html != html:
        html = new_html
        changed = True

    # 3. Insert Ostalo dropdown after Projekti li (only if not already there)
    if 'Ostalo' not in html:
        repl = r'\1\n        ' + ostalo_block(basename).replace('\\', '\\\\')
        new_html = PROJEKTI_LI_RE.sub(repl, html, count=1)
        if new_html != html:
            html = new_html
            changed = True

    # 4. Drawer: remove old drawer-sub from O nama, keep plain O nama link
    new_html = DRAWER_ONAME_BLOCK_RE.sub(r'\1', html, count=1)
    if new_html != html:
        html = new_html
        changed = True

    # 5. Drawer: remove old Dokumentacija link
    new_html = DRAWER_DOK_RE.sub('', html, count=1)
    if new_html != html:
        html = new_html
        changed = True

    # 6. Drawer: insert Ostalo sub after Projekti (only if not already there)
    if 'drawer-label' not in html:
        repl = r'\1' + DRAWER_OSTALO_SUB.replace('\\', '\\\\')
        new_html = DRAWER_PROJEKTI_RE.sub(repl, html, count=1)
        if new_html != html:
            html = new_html
            changed = True

    # 7. CSS: add .drawer-label style (only once)
    if 'drawer-label' in html and '.drawer-label' not in html:
        new_html = DRAWER_SUB_CSS_RE.sub(r'\1' + DRAWER_LABEL_CSS, html, count=1)
        if new_html != html:
            html = new_html
            changed = True

    if changed:
        print(f'  OK : {basename}')
    else:
        print(f'  -- : {basename} (no changes)')
    return html


for path in FILES:
    basename = os.path.basename(path)
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    patched = patch(html, basename)
    if patched != html:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(patched)

print('\nDone.')
