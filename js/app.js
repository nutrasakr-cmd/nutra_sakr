/**
 * App.js - Core application logic, routing, translation, and theme management
 */

const App = {
  lang: localStorage.getItem('nutra_lang') || 'en',
  theme: localStorage.getItem('nutra_theme') || 'light',
  translations: {},

  init() {
    this.applyTheme();
    this.setupThemeToggle();
    this.setupLangToggle();
    this.setupHamburger();
    this.loadTranslations().then(() => {
      this.updateUI();
      document.dispatchEvent(new Event('translationsLoaded'));
    });
  },

  async loadTranslations() {
    try {
      const response = await fetch(`data/${this.lang}/ui.json`);
      this.translations = await response.json();
    } catch (e) {
      console.error("Failed to load translations:", e);
    }
  },

  updateUI() {
    document.documentElement.setAttribute('dir', this.lang === 'ar' ? 'rtl' : 'ltr');
    document.documentElement.lang = this.lang;

    document.body.classList.add('lang-updating');

    setTimeout(() => {
      document.querySelectorAll('[data-i18n]').forEach(el => {
        const key = el.getAttribute('data-i18n');
        const val = this.translations[key];
        if (!val) return;

        const tag = el.tagName;
        if (tag === 'INPUT' || tag === 'TEXTAREA') {
          el.placeholder = val;
        } else {
          el.textContent = val;
        }
      });
      document.body.classList.remove('lang-updating');
    }, 150);

    // Sync mobile lang toggle label
    const mobileLangBtn = document.getElementById('mobile-lang-toggle');
    if (mobileLangBtn) {
      mobileLangBtn.textContent = this.lang === 'en' ? 'عربي' : 'English';
    }
  },

  applyTheme() {
    document.documentElement.setAttribute('data-theme', this.theme);
    const icon = this.theme === 'light' ? '🌙' : '☀️';
    const btn = document.getElementById('theme-toggle');
    const mobileBtn = document.getElementById('mobile-theme-toggle');
    if (btn) btn.textContent = icon;
    if (mobileBtn) mobileBtn.textContent = icon;
  },

  setupThemeToggle() {
    const toggle = () => {
      this.theme = this.theme === 'light' ? 'dark' : 'light';
      localStorage.setItem('nutra_theme', this.theme);
      this.applyTheme();
    };

    const btn = document.getElementById('theme-toggle');
    const mobileBtn = document.getElementById('mobile-theme-toggle');
    if (btn) btn.addEventListener('click', toggle);
    if (mobileBtn) mobileBtn.addEventListener('click', toggle);
  },

  setupLangToggle() {
    const switchLang = (btn, mobileBtn) => {
      this.lang = this.lang === 'en' ? 'ar' : 'en';
      localStorage.setItem('nutra_lang', this.lang);

      const label = this.lang === 'en' ? 'عربي' : 'English';
      if (btn) btn.textContent = label;
      if (mobileBtn) mobileBtn.textContent = label;

      DataLoader.clearCache();
      this.loadTranslations().then(() => {
        this.updateUI();
        document.dispatchEvent(new Event('languageChanged'));
      });
    };

    const btn = document.getElementById('lang-toggle');
    const mobileBtn = document.getElementById('mobile-lang-toggle');

    const label = this.lang === 'en' ? 'عربي' : 'English';
    if (btn) { btn.textContent = label; btn.addEventListener('click', () => switchLang(btn, mobileBtn)); }
    if (mobileBtn) { mobileBtn.textContent = label; mobileBtn.addEventListener('click', () => switchLang(btn, mobileBtn)); }
  },

  setupHamburger() {
    const hamburger = document.getElementById('hamburger-btn');
    const mobileNav = document.getElementById('mobile-nav');
    const overlay = document.getElementById('mobile-nav-overlay');
    const closeBtn = document.getElementById('mobile-nav-close');

    if (!hamburger || !mobileNav || !overlay) return;

    const openMenu = () => {
      mobileNav.classList.add('is-active');
      overlay.style.display = 'block';
      setTimeout(() => overlay.classList.add('is-active'), 10);
      hamburger.classList.add('is-active');
      hamburger.setAttribute('aria-expanded', 'true');
      document.body.style.overflow = 'hidden';
    };

    const closeMenu = () => {
      mobileNav.classList.remove('is-active');
      overlay.classList.remove('is-active');
      setTimeout(() => { overlay.style.display = 'none'; }, 300);
      hamburger.classList.remove('is-active');
      hamburger.setAttribute('aria-expanded', 'false');
      document.body.style.overflow = '';
    };

    hamburger.addEventListener('click', openMenu);
    if (closeBtn) closeBtn.addEventListener('click', closeMenu);
    overlay.addEventListener('click', closeMenu);

    // Close on nav link click
    mobileNav.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', closeMenu);
    });

    // Close on Escape key
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') closeMenu();
    });
  }
};

document.addEventListener('DOMContentLoaded', () => {
  App.init();
});
