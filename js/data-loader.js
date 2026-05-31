/**
 * DataLoader.js - Utility for fetching JSON data with simple caching
 */

const DataLoader = {
  cache: {},

  async fetch(endpoint) {
    const lang = App.lang || 'en';
    const url = `data/${lang}/${endpoint}.json`;
    
    // Cache busting is not strictly needed for local files but good for practice
    // For now we'll just cache per session
    if (this.cache[url]) {
      return this.cache[url];
    }

    try {
      const response = await fetch(url);
      if (!response.ok) throw new Error(`Network response was not ok: ${response.statusText}`);
      const data = await response.json();
      this.cache[url] = data;
      return data;
    } catch (error) {
      console.error(`DataLoader failed to fetch ${endpoint}:`, error);
      return null;
    }
  },

  clearCache() {
    this.cache = {};
  }
};

// Listen to language changes to clear cache and reload data if needed
document.addEventListener('languageChanged', () => {
  DataLoader.clearCache();
});
