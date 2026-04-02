#!/usr/bin/env python3
"""
Remove all inline nav CSS from every HTML page and add <link rel="stylesheet" href="nav.css">.
Nav styles now live exclusively in nav.css.
"""

import re, os, glob

FILES = sorted(glob.glob(os.path.join(os.path.dirname(__file__), '*.html')))
FILES = [f for f in FILES if os.path.basename(f) != 'logo-variants.html']

# ── CSS selector prefixes that belong to nav.css ────────────────────────────
# We'll match any CSS rule whose selector starts with one of these.
NAV_SELECTORS = [
    r'\.nav\b', r'\.nav-', r'\.hamburger', r'\.mega-', r'\.drawer-',
    r'\.about-dropdown', r'#nav\b', r'#megaItem', r'#megaPanel',
    r'#aboutItem', r'#aboutDropdown', r'#hamburger', r'#navDrawer',
]

# ── Patterns to remove wholesale (single-line or multi-line CSS rules) ───────
# Build a pattern that matches any CSS rule block starting with a nav selector.
# This handles both inline (single-line) and multi-line blocks.

def remove_nav_css_rules(style_text):
    """Remove CSS rules that belong to nav.css from a <style> block's content."""

    # 1. Remove multi-line blocks: selector { ... }
    #    Walk through and remove blocks whose selector matches nav selectors.
    result = style_text

    # Match: optional whitespace + nav-selector-start + anything + { ... }
    # We do multiple passes until stable (handles nested/adjacent rules)
    sel_pattern = '|'.join(NAV_SELECTORS)
    # Match a rule: (optional comment line) + selector(s) + { body }
    block_re = re.compile(
        r'[ \t]*(?:(?:' + sel_pattern + r')[^{]*)\{[^{}]*\}\n?',
        re.MULTILINE
    )
    # Also match multi-line blocks (body spans multiple lines)
    block_ml_re = re.compile(
        r'[ \t]*(?:' + sel_pattern + r')[^\{]*\{[^{}]*\}[ \t]*\n?',
        re.DOTALL
    )

    # Remove @media blocks that are ONLY nav rules (like @media(max-width:900px){.nav-links,...})
    # These are single-line media queries containing only nav selectors
    media_nav_re = re.compile(
        r'[ \t]*@media[^{]+\{[ \t]*(?:\.nav-links|\.nav-cta|\.hamburger|\.nav-drawer|\.mega-panel|\.about-dropdown|\.nav-linkedin)[^}]*\}[ \t]*\n?'
    )
    result = media_nav_re.sub('', result)

    # Remove single-line nav rules
    prev = None
    while prev != result:
        prev = result
        result = block_re.sub('', result)

    # Remove leftover inline hacks (like the !important one-liners)
    inline_hack_re = re.compile(
        r'[ \t]*(?:\.nav-links \.about-dropdown|#aboutItem)[^\n]+\n?'
    )
    result = inline_hack_re.sub('', result)

    # Clean up excess blank lines
    result = re.sub(r'\n{3,}', '\n\n', result)
    return result


def patch(html, basename):
    changed = False

    # 1. Add <link rel="stylesheet" href="nav.css"> if not already present
    if 'href="nav.css"' not in html:
        # Insert before </head> or before first <style>
        insert_re = re.compile(r'([ \t]*<link[^>]+stylesheet[^>]+>\n)', re.MULTILINE)
        m = list(insert_re.finditer(html))
        if m:
            # Insert after the last existing <link> stylesheet
            last = m[-1]
            html = html[:last.end()] + '  <link rel="stylesheet" href="nav.css">\n' + html[last.end():]
        else:
            html = html.replace('</head>', '  <link rel="stylesheet" href="nav.css">\n</head>', 1)
        changed = True

    # 2. Strip nav CSS from every <style> block
    def clean_style(m):
        content = m.group(1)
        cleaned = remove_nav_css_rules(content)
        if cleaned != content:
            return '<style>' + cleaned + '</style>'
        return m.group(0)

    new_html = re.sub(r'<style>(.*?)</style>', clean_style, html, flags=re.DOTALL)
    if new_html != html:
        html = new_html
        changed = True

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
