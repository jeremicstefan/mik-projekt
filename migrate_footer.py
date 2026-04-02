#!/usr/bin/env python3
"""
Replace inline footer HTML + CSS in every page with footer.js + footer.css.
"""
import re, os, glob

FILES = sorted(glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)), '*.html')))
FILES = [f for f in FILES if os.path.basename(f) != 'logo-variants.html']

FOOTER_REPLACEMENT = (
    '  <div id="footer-root"></div>\n'
    '  <script src="footer.js"></script>\n'
    '  <script>MikFooter.init();</script>\n'
)

FOOTER_CSS_SELECTORS = [
    r'\.footer\b', r'\.footer-', r'\.footer-brand', r'\.footer-cols',
    r'\.footer-col\b', r'\.footer-col-', r'\.footer-bottom', r'\.footer-social',
]

def remove_footer_css(style_text):
    sel = '|'.join(FOOTER_CSS_SELECTORS)
    # Remove multi-line blocks
    block_re = re.compile(
        r'[ \t]*(?:' + sel + r')[^{]*\{[^{}]*\}[ \t]*\n?',
        re.DOTALL
    )
    prev = None
    result = style_text
    while prev != result:
        prev = result
        result = block_re.sub('', result)
    # Remove responsive footer rules inside @media blocks
    # Replace footer lines inside media queries
    result = re.sub(r'[ \t]*(?:' + sel + r')[^\n]*\n?', '', result)
    result = re.sub(r'\n{3,}', '\n\n', result)
    return result

def patch(html, basename):
    changed = False

    # 1. Add footer.css link if not present
    if 'href="footer.css"' not in html:
        html = re.sub(
            r'([ \t]*<link rel="stylesheet" href="nav\.css">)',
            r'\1\n  <link rel="stylesheet" href="footer.css">',
            html
        )
        changed = True

    # 2. Replace <footer>...</footer> with footer-root div + scripts
    new_html = re.sub(r'[ \t]*<footer[\s\S]*?</footer>\n?', FOOTER_REPLACEMENT, html)
    if new_html != html:
        html = new_html
        changed = True

    # 3. Strip footer CSS from <style> blocks
    def clean_style(m):
        content = m.group(1)
        cleaned = remove_footer_css(content)
        if cleaned != content:
            return '<style>' + cleaned + '</style>'
        return m.group(0)
    new_html = re.sub(r'<style>(.*?)</style>', clean_style, html, flags=re.DOTALL)
    if new_html != html:
        html = new_html
        changed = True

    print(f'  {"OK" if changed else "--"} : {basename}')
    return html

for path in FILES:
    basename = os.path.basename(path)
    original = open(path, encoding='utf-8').read()
    patched = patch(original, basename)
    if patched != original:
        open(path, 'w', encoding='utf-8').write(patched)

print('\nDone.')
