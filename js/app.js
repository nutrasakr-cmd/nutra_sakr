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
    this.loadTranslations().then(() => {
      this.updateUI();
      // Dispatch event to let other scripts know translations are ready
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
        if (this.translations[key]) {
          if (el.tagName === 'INPUT' || el.tagName === 'TEXTAREA') {
            el.placeholder = this.translations[key];
          } else {
            el.textContent = this.translations[key];
          }
        }
      });
      document.body.classList.remove('lang-updating');
    }, 150);
  },

  setupThemeToggle() {
    const btn = document.getElementById('theme-toggle');
    if (btn) {
      btn.addEventListener('click', () => {
        this.theme = this.theme === 'light' ? 'dark' : 'light';
        localStorage.setItem('nutra_theme', this.theme);
        this.applyTheme();
      });
    }
  },

  applyTheme() {
    document.documentElement.setAttribute('data-theme', this.theme);
    const btn = document.getElementById('theme-toggle');
    if (btn) {
      btn.textContent = this.theme === 'light' ? '🌙' : '☀️';
    }
  },

  setupLangToggle() {
    const btn = document.getElementById('lang-toggle');
    if (btn) {
      btn.textContent = this.lang === 'en' ? 'عربي' : 'English';
      btn.addEventListener('click', () => {
        this.lang = this.lang === 'en' ? 'ar' : 'en';
        localStorage.setItem('nutra_lang', this.lang);
        btn.textContent = this.lang === 'en' ? 'عربي' : 'English';
        
        // Reload translations and refresh page data
        this.loadTranslations().then(() => {
          this.updateUI();
          document.dispatchEvent(new Event('languageChanged'));
        });
      });
    }
  }
};

document.addEventListener('DOMContentLoaded', () => {
  App.init();
});
