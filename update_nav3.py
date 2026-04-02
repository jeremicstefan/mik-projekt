#!/usr/bin/env python3
"""
Replace duplicated nav HTML + JS in every page with a single nav.js call.
Each page gets:
  <div id="nav-root"></div>
  <script src="nav.js"></script>
  <script>MikNav.init('PAGE_ID');</script>
and the inline nav HTML + nav JS are removed.
"""

import re, os, glob

FILES = sorted(glob.glob(os.path.join(os.path.dirname(__file__), '*.html')))
FILES = [f for f in FILES if os.path.basename(f) != 'logo-variants.html']

# Page-id is the filename without .html
def page_id(basename):
    return os.path.splitext(basename)[0]

# ── Regex: entire nav block (nav + mega-panel + drawer) ──────────────────────
# Matches from <nav class="nav" id="nav"> through the closing </div> of navDrawer
NAV_BLOCK_RE = re.compile(
    r'[ \t]*<nav class="nav" id="nav">.*?</div>\s*(?=\n\s*<!--)',
    re.DOTALL
)
# Fallback: match just up to end of navDrawer </div>
NAV_BLOCK_RE2 = re.compile(
    r'[ \t]*<nav class="nav" id="nav">.*?id="navDrawer"[^>]*>.*?</div>',
    re.DOTALL
)

# ── Nav JS blocks to strip from <script> ─────────────────────────────────────
NAV_JS_PATTERNS = [
    # var declarations
    re.compile(r"\s*const nav\s*=\s*document\.getElementById\('nav'\);\s*\n"),
    re.compile(r"\s*const hamburger\s*=\s*document\.getElementById\('hamburger'\);\s*\n"),
    re.compile(r"\s*const drawer\s*=\s*document\.getElementById\('navDrawer'\);\s*\n"),
    # scroll listener
    re.compile(r"\s*window\.addEventListener\('scroll'[^\n]+\n"),
    # hamburger click
    re.compile(r"\s*hamburger\.addEventListener\('click'[^\n]+\n"),
    # closeDrawer
    re.compile(r"\s*function closeDrawer\(\)[^\n]+\n"),
    # document click (nav close)
    re.compile(r"\s*document\.addEventListener\('click'[^\n]+closeDrawer[^\n]+\n"),
    # megaItem/megaPanel block
    re.compile(
        r"\s*const megaItem\s*=\s*document\.getElementById\('megaItem'\);.*?"
        r"megaPanel\.addEventListener\('mouseleave', close\);\s*\n\s*\}",
        re.DOTALL
    ),
    # aboutItem block (old and new versions)
    re.compile(
        r"\s*(?:// ─── About dropdown[^\n]*\n)?"
        r"\s*const aboutItem\s*=\s*document\.getElementById\('aboutItem'\);.*?"
        r"\}\s*\n\s*\}",
        re.DOTALL
    ),
]

# ── Replacement nav-root + scripts ───────────────────────────────────────────
def nav_replacement(pid):
    return (
        '  <div id="nav-root"></div>\n'
        f'  <script src="nav.js"></script>\n'
        f'  <script>MikNav.init(\'{pid}\');</script>\n'
    )

def patch(html, basename):
    pid = page_id(basename)
    changed = False

    # 1. Replace the nav HTML block
    m = NAV_BLOCK_RE2.search(html)
    if m:
        html = html[:m.start()] + nav_replacement(pid) + html[m.end():]
        changed = True
    else:
        print(f'  WARN: nav block not found in {basename}')

    # 2. Strip nav JS from script blocks
    for pat in NAV_JS_PATTERNS:
        new = pat.sub('', html)
        if new != html:
            html = new
            changed = True

    # 3. Clean up any leftover blank lines at top of <script> blocks
    html = re.sub(r'(<script>)\n(\s*\n)+', r'\1\n', html)

    if changed:
        print(f'  OK : {basename}')
    else:
        print(f'  -- : {basename}')
    return html


for path in FILES:
    basename = os.path.basename(path)
    with open(path, 'r', encoding='utf-8') as f:
        original = f.read()
    patched = patch(original, basename)
    if patched != original:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(patched)

print('\nDone.')
