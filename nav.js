(function () {
  'use strict';

  var SERVICE_PAGES = ['usluge', 'kotlovski-sistemi', 'inzenjerstvo', 'proizvodnja',
                       'instalacija-montaza', 'usluge-i-odrzavanje', 'poslovne-oblasti'];
  var OSTALO_PAGES  = ['karijera', 'cesta-pitanja', 'dokumentacija',
                       'odrzivost', 'pravne-napomene', 'kontakt'];

  function buildHTML(page) {
    var idx = page === 'index';
    var ona = page === 'o-nama';
    var usl = SERVICE_PAGES.indexOf(page) !== -1;
    var prj = page === 'projekti';
    var ost = OSTALO_PAGES.indexOf(page) !== -1;

    var a  = function (f) { return f ? ' class="active"' : ''; };
    var ta = function (f) { return f ? ' active' : ''; };

    var chevron = '<svg class="nav-mega-chevron" viewBox="0 0 10 10" xmlns="http://www.w3.org/2000/svg">'
                + '<polyline points="1,3 5,7 9,3" stroke="currentColor" stroke-width="1.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
                + '</svg>';

    return (
      '<nav class="nav" id="nav">\n'
    + '  <div class="inner">\n'
    + '    <a class="nav-logo" href="index.html"><img src="assets/0_logo/mik-logo-light-no-est-bolder.png" alt="MIK Projekt" /></a>\n'
    + '    <ul class="nav-links">\n'
    + '      <li><a href="index.html"'   + a(idx) + '>Po\u010detna</a></li>\n'
    + '      <li><a href="o-nama.html"'  + a(ona) + '>O nama</a></li>\n'
    + '      <li class="nav-mega-item" id="megaItem">'
    +          '<a href="usluge.html" class="nav-mega-trigger' + ta(usl) + '" id="megaTrigger">'
    +          'Na\u0161e usluge' + chevron + '</a></li>\n'
    + '      <li><a href="projekti.html"' + a(prj) + '>Projekti</a></li>\n'
    + '      <li class="nav-mega-item" id="aboutItem">'
    +          '<a href="#" class="nav-mega-trigger' + ta(ost) + '">Ostalo' + chevron + '</a>'
    +          '<div class="about-dropdown" id="aboutDropdown">'
    +          '<a href="karijera.html">Karijera</a>'
    +          '<a href="cesta-pitanja.html">&#268;esta pitanja</a>'
    +          '<a href="dokumentacija.html">Dokumentacija</a>'
    +          '<a href="odrzivost.html">Odr&#382;ivost</a>'
    +          '<a href="pravne-napomene.html">Pravne napomene</a>'
    +          '</div></li>\n'
    + '    </ul>\n'
    + '    <div class="nav-right">'
    +      '<a class="nav-cta" href="kontakt.html">Kontakt</a>'
    +      '<a class="nav-linkedin" href="https://www.linkedin.com/company/mikprojekt/" target="_blank" rel="noopener noreferrer" aria-label="LinkedIn">'
    +      '<svg viewBox="0 0 24 24" fill="currentColor" width="20" height="20" aria-hidden="true"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 0 1-2.063-2.065 2.064 2.064 0 1 1 2.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>'
    +      '</a>'
    +    '</div>\n'
    + '    <button class="hamburger" id="hamburger" aria-label="Meni">'
    +        '<span></span><span></span><span></span></button>\n'
    + '  </div>\n'
    + '</nav>\n'

    + '<div class="mega-panel" id="megaPanel"><div class="inner mega-inner-wrap">'
    +   '<div class="mega-top">'
    +     '<span class="mega-label">POSLOVNE OBLASTI</span>'
    +     '<a href="usluge.html" class="mega-all-link">Sve usluge \u2192</a>'
    +   '</div>'
    +   '<div class="mega-grid">'
    +     '<a class="mega-item" href="kotlovski-sistemi.html">'
    +       '<div class="mega-item-img" style="background-image:url(\'assets/1_navigation/nav_kotlovski-sistem.png\');background-position:calc(50% - 5px) calc(50% + 5%);"></div>'
    +       '<span class="mega-item-name">Kotlovski sistemi</span>'
    +       '<span class="mega-item-desc">Industrijska kotlovska postrojenja za razli\u010dita goriva</span>'
    +     '</a>'
    +     '<a class="mega-item" href="inzenjerstvo.html">'
    +       '<div class="mega-item-img" style="background-image:url(\'assets/1_navigation/nav_inzenjerstvo.png\');background-size:110%;background-repeat:no-repeat;"></div>'
    +       '<span class="mega-item-name">In\u017eenjerstvo</span>'
    +       '<span class="mega-item-desc">Projektovanje energetskih i termotehni\u010dkih sistema</span>'
    +     '</a>'
    +     '<a class="mega-item" href="proizvodnja.html">'
    +       '<div class="mega-item-img" style="background-image:url(\'assets/1_navigation/nav_proizvodnja.png\');"></div>'
    +       '<span class="mega-item-name">Proizvodnja</span>'
    +       '<span class="mega-item-desc">Precizna izrada komponenti i kompleksnih sistema</span>'
    +     '</a>'
    +     '<a class="mega-item" href="instalacija-montaza.html">'
    +       '<div class="mega-item-img" style="background-image:url(\'assets/1_navigation/nav_instalacija-sistem.png\');"></div>'
    +       '<span class="mega-item-name">Instalacija sistema</span>'
    +       '<span class="mega-item-desc">Stru\u010dna monta\u017ea i pu\u0161tanje u rad postrojenja</span>'
    +     '</a>'
    +     '<a class="mega-item" href="usluge-i-odrzavanje.html">'
    +       '<div class="mega-item-img" style="background-image:url(\'assets/1_navigation/nav_servis_i_odrzavanje.png\');background-size:70%;background-repeat:no-repeat;background-color:#fff;"></div>'
    +       '<span class="mega-item-name">Servis i odr\u017eavanje</span>'
    +       '<span class="mega-item-desc">Dugoro\u010dna tehni\u010dka podr\u0161ka i optimizacija sistema</span>'
    +     '</a>'
    +   '</div>'
    + '</div></div>\n'

    + '<div class="nav-drawer" id="navDrawer">'
    +   '<a href="index.html" onclick="closeDrawer()"'   + a(idx) + '>Po\u010detna</a>'
    +   '<a href="o-nama.html" onclick="closeDrawer()"'  + a(ona) + '>O nama</a>'

    +   '<div class="drawer-accordion' + (usl ? ' open' : '') + '" id="drawerUsluge">'
    +     '<button class="drawer-accordion-trigger' + (usl ? ' active' : '') + '">'
    +       'Na\u0161e usluge' + chevron
    +     '</button>'
    +     '<div class="drawer-accordion-body">'
    +       '<a href="kotlovski-sistemi.html" onclick="closeDrawer()">Kotlovski sistemi</a>'
    +       '<a href="inzenjerstvo.html" onclick="closeDrawer()">In\u017eenjerstvo</a>'
    +       '<a href="proizvodnja.html" onclick="closeDrawer()">Proizvodnja</a>'
    +       '<a href="instalacija-montaza.html" onclick="closeDrawer()">Instalacija sistema</a>'
    +       '<a href="usluge-i-odrzavanje.html" onclick="closeDrawer()">Servis i odr\u017eavanje</a>'
    +       '<a href="usluge.html" class="drawer-accordion-all" onclick="closeDrawer()">Sve usluge \u2192</a>'
    +     '</div>'
    +   '</div>'

    +   '<a href="projekti.html" onclick="closeDrawer()"' + a(prj) + '>Projekti</a>'

    +   '<div class="drawer-accordion' + (ost ? ' open' : '') + '" id="drawerOstalo">'
    +     '<button class="drawer-accordion-trigger' + (ost ? ' active' : '') + '">'
    +       'Ostalo' + chevron
    +     '</button>'
    +     '<div class="drawer-accordion-body">'
    +       '<a href="karijera.html" onclick="closeDrawer()">Karijera</a>'
    +       '<a href="cesta-pitanja.html" onclick="closeDrawer()">&#268;esta pitanja</a>'
    +       '<a href="dokumentacija.html" onclick="closeDrawer()">Dokumentacija</a>'
    +       '<a href="odrzivost.html" onclick="closeDrawer()">Odr&#382;ivost</a>'
    +       '<a href="pravne-napomene.html" onclick="closeDrawer()">Pravne napomene</a>'
    +     '</div>'
    +   '</div>'

    +   '<a href="kontakt.html" class="nav-cta" onclick="closeDrawer()">Kontakt</a>'
    + '</div>\n'
    );
  }

  function init(page) {
    var root = document.getElementById('nav-root');
    if (!root) { console.warn('MikNav: #nav-root not found'); return; }

    root.outerHTML = buildHTML(page);

    var nav       = document.getElementById('nav');
    var hamburger = document.getElementById('hamburger');
    var drawer    = document.getElementById('navDrawer');

    window.addEventListener('scroll', function () {
      nav.classList.toggle('scrolled', window.scrollY > 10);
    });

    hamburger.addEventListener('click', function () {
      var o = hamburger.classList.toggle('open');
      drawer.classList.toggle('open', o);
    });

    window.closeDrawer = function () {
      hamburger.classList.remove('open');
      drawer.classList.remove('open');
    };

    document.addEventListener('click', function (e) {
      if (!nav.contains(e.target) && !drawer.contains(e.target)) closeDrawer();
    });

    // Drawer accordions (mobile)
    drawer.querySelectorAll('.drawer-accordion-trigger').forEach(function (btn) {
      btn.addEventListener('click', function () {
        var acc = btn.parentElement;
        var isOpen = acc.classList.contains('open');
        drawer.querySelectorAll('.drawer-accordion').forEach(function (a) { a.classList.remove('open'); });
        if (!isOpen) acc.classList.add('open');
      });
    });

    // Naše usluge mega panel
    var megaItem  = document.getElementById('megaItem');
    var megaPanel = document.getElementById('megaPanel');
    if (megaItem && megaPanel) {
      var mt;
      function openMega()  { clearTimeout(mt); megaItem.classList.add('mega-open'); megaPanel.classList.add('mega-visible'); }
      function closeMega() { mt = setTimeout(function () { megaItem.classList.remove('mega-open'); megaPanel.classList.remove('mega-visible'); }, 120); }
      megaItem.addEventListener('mouseenter', openMega);
      megaItem.addEventListener('mouseleave', closeMega);
      megaPanel.addEventListener('mouseenter', openMega);
      megaPanel.addEventListener('mouseleave', closeMega);
    }

    // Ostalo dropdown
    var aboutItem = document.getElementById('aboutItem');
    if (aboutItem) {
      var at;
      function openAbout()  { clearTimeout(at); aboutItem.classList.add('mega-open'); }
      function closeAbout() { at = setTimeout(function () { aboutItem.classList.remove('mega-open'); }, 120); }
      aboutItem.addEventListener('mouseenter', openAbout);
      aboutItem.addEventListener('mouseleave', closeAbout);
      var aboutDrop = document.getElementById('aboutDropdown');
      if (aboutDrop) {
        aboutDrop.addEventListener('mouseenter', openAbout);
        aboutDrop.addEventListener('mouseleave', closeAbout);
      }
    }
  }

  window.MikNav = { init: init };
})();
