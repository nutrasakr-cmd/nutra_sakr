/**
 * Pages.js - Logic for specific page rendering (Products, Home, FAQs)
 */

document.addEventListener('translationsLoaded', initPages);
document.addEventListener('languageChanged', initPages);

function initPages() {
  const path = window.location.pathname;
  
  if (path.includes('products.html')) {
    renderProductsPage();
  } else if (path.includes('index.html') || path === '/' || path.endsWith('/')) {
    renderHomePage();
  } else if (path.includes('faq.html')) {
    renderFAQPage();
  }
}

async function renderHomePage() {
  const container = document.getElementById('featured-products');
  if (!container) return;
  
  const products = await DataLoader.fetch('products');
  if (!products) return;
  
  container.innerHTML = '';
  
  // Show first 3 products
  products.slice(0, 3).forEach(p => {
    const card = document.createElement('div');
    card.className = 'card';
    card.innerHTML = `
      <div class="card-image">
        <img src="${p.image}" alt="${p.name}" onerror="this.src='assets/images/laboratory.jpg'">
      </div>
      <h3 class="mb-1">${p.name}</h3>
      <p class="text-muted mb-2" style="font-size: 0.9rem;">${p.description}</p>
      <a href="product-details.html?id=${p.id}" style="font-weight: 600; text-decoration: none;" data-i18n="view_details">
        ${App.translations['view_details'] || 'View Details'} &rarr;
      </a>
    `;
    container.appendChild(card);
  });
}

async function renderProductsPage() {
  const grid = document.getElementById('products-grid');
  const filters = document.getElementById('category-filters');
  const searchInput = document.getElementById('product-search');
  
  if (!grid || !filters) return;
  
  const [products, categories] = await Promise.all([
    DataLoader.fetch('products'),
    DataLoader.fetch('categories')
  ]);
  
  if (!products || !categories) return;

  // Render Categories
  filters.innerHTML = `
    <div style="margin-bottom: 8px;">
      <label style="cursor:pointer; display:flex; gap:10px; align-items:center;">
        <input type="radio" name="cat" value="all" checked>
        <span data-i18n="all_categories">${App.translations['all_categories'] || 'All Categories'}</span>
      </label>
    </div>
  `;
  categories.forEach(cat => {
    filters.innerHTML += `
      <div style="margin-bottom: 8px;">
        <label style="cursor:pointer; display:flex; gap:10px; align-items:center;">
          <input type="radio" name="cat" value="${cat.id}">
          <span>${cat.name}</span>
        </label>
      </div>
    `;
  });

  // Render Products Function
  const renderGrid = (filterCat, searchTerm) => {
    grid.innerHTML = '';
    const filtered = products.filter(p => {
      const matchCat = filterCat === 'all' || p.category === filterCat;
      const matchSearch = p.name.toLowerCase().includes(searchTerm.toLowerCase()) || 
                          p.description.toLowerCase().includes(searchTerm.toLowerCase());
      return matchCat && matchSearch;
    });
    
    if (filtered.length === 0) {
      grid.innerHTML = `<p class="text-muted">No products found.</p>`;
      return;
    }
    
    filtered.forEach(p => {
      const card = document.createElement('div');
      card.className = 'card';
      card.innerHTML = `
        <div class="card-image">
          <img src="${p.image}" alt="${p.name}" onerror="this.src='assets/images/laboratory.jpg'">
        </div>
        <h3 class="mb-1">${p.name}</h3>
        <p class="text-muted mb-2" style="font-size: 0.9rem;">${p.description}</p>
        <a href="product-details.html?id=${p.id}" class="btn btn-primary" style="width: 100%;">
          ${App.translations['view_details'] || 'View Details'}
        </a>
      `;
      grid.appendChild(card);
    });
  };

  // Initial render
  renderGrid('all', '');

  // Event Listeners
  filters.addEventListener('change', (e) => {
    if (e.target.name === 'cat') {
      renderGrid(e.target.value, searchInput.value);
    }
  });

  searchInput.addEventListener('input', (e) => {
    const selectedCat = document.querySelector('input[name="cat"]:checked').value;
    renderGrid(selectedCat, e.target.value);
  });
}

async function renderFAQPage() {
  const container = document.getElementById('faq-container');
  if (!container) return;
  
  const faqs = await DataLoader.fetch('faqs');
  if (!faqs) return;
  
  container.innerHTML = '';
  
  faqs.forEach(faq => {
    const el = document.createElement('details');
    el.style.cssText = 'background: var(--bg-color); padding: 20px; border-radius: var(--radius-sm); border: 1px solid var(--border-color); box-shadow: var(--shadow-sm); cursor: pointer;';
    el.innerHTML = `
      <summary style="font-weight: 600; font-family: var(--font-heading); color: var(--primary-blue); font-size: 1.1rem; list-style: none; display: flex; justify-content: space-between;">
        ${faq.question}
        <span style="color: var(--secondary-green);">+</span>
      </summary>
      <p style="margin-top: 16px; color: var(--text-muted); line-height: 1.7;">${faq.answer}</p>
    `;
    container.appendChild(el);
  });
}
