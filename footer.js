(function () {
  'use strict';

  var LI_SVG = '<svg viewBox="0 0 24 24" fill="currentColor" width="20" height="20" aria-hidden="true">'
             + '<path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 0 1-2.063-2.065 2.064 2.064 0 1 1 2.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/>'
             + '</svg>';

  function buildHTML() {
    return (
      '<footer class="footer">\n'
    + '  <div class="inner">\n'
    + '    <div class="footer-content">\n'
    + '      <div class="footer-brand">\n'
    + '        <img src="assets/0_logo/mik-logo-light-no-est-bolder.png" alt="MIK Projekt" class="footer-brand-logo" />\n'
    + '        <p>Prodaja, monta\u017ea i odr\u017eavanje kotlova, termoenergetskih postrojenja i industrijskih energetskih sistema.</p>\n'
    + '      </div>\n'
    + '      <div class="footer-cols">\n'
    + '        <div class="footer-col">\n'
    + '          <span class="footer-col-title">KOMPANIJA</span>\n'
    + '          <a href="o-nama.html">O nama</a>\n'
    + '          <a href="projekti.html">Projekti</a>\n'
    + '          <a href="dokumentacija.html">Dokumentacija</a>\n'
    + '          <a href="kontakt.html">Kontakt</a>\n'
    + '          <a href="karijera.html">Karijera</a>\n'
    + '        </div>\n'
    + '        <div class="footer-col">\n'
    + '          <span class="footer-col-title">USLUGE</span>\n'
    + '          <a href="inzenjerstvo.html">In\u017eenjerstvo</a>\n'
    + '          <a href="kotlovski-sistemi.html">Kotlovski sistemi</a>\n'
    + '          <a href="proizvodnja.html">Proizvodnja</a>\n'
    + '          <a href="instalacija-montaza.html">Instalacija i monta\u017ea</a>\n'
    + '          <a href="usluge-i-odrzavanje.html">Servis i odr\u017eavanje</a>\n'
    + '        </div>\n'
    + '        <div class="footer-col">\n'
    + '          <span class="footer-col-title">KONTAKT</span>\n'
    + '          <a href="#">Beograd, Srbija</a>\n'
    + '          <a href="mailto:office@mikprojekt.com">office@mikprojekt.com</a>\n'
    + '          <a href="tel:+381113065106">+381 11 306 51 06</a>\n'
    + '          <a href="https://www.linkedin.com/company/mikprojekt/" target="_blank" rel="noopener noreferrer" aria-label="LinkedIn" class="footer-social-link">' + LI_SVG + '/mikprojekt</a>\n'
    + '        </div>\n'
    + '      </div>\n'
    + '    </div>\n'
    + '  </div>\n'
    + '  <div class="footer-bottom">\n'
    + '    <div class="inner">\n'
    + '      <span>\u00a9 2026 MIK Projekt. Sva prava zadr\u017eana.</span>\n'
    + '      <div class="footer-bottom-right">\n'
    + '        <a href="pravne-napomene.html">Pravne napomene</a>\n'
    + '        <a href="https://www.linkedin.com/company/mikprojekt/" target="_blank" rel="noopener noreferrer" class="footer-bottom-li" aria-label="LinkedIn">' + LI_SVG + '</a>\n'
    + '      </div>\n'
    + '    </div>\n'
    + '  </div>\n'
    + '</footer>\n'
    );
  }

  function init() {
    var root = document.getElementById('footer-root');
    if (!root) { console.warn('MikFooter: #footer-root not found'); return; }
    root.outerHTML = buildHTML();
  }

  window.MikFooter = { init: init };
})();
