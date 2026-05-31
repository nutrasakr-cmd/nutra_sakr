# NutraSakr Corporate Website

This is the source code for the NutraSakr bilingual corporate website.

## Architecture
- HTML5, CSS3, Vanilla JS
- Dynamic JSON data loading for multi-language support (English/Arabic)
- Fully responsive, SEO optimized without external frameworks

## Local Development
Since this project uses AJAX (`fetch()`) to load JSON files, you must run a local web server to view it without encountering CORS errors. 

If you have Python installed, you can simply run:
```bash
python -m http.server 8000
```
Then navigate to `http://localhost:8000`.

## Deployment
This project is configured as a static site and is ready to be deployed to Hostinger (or any other static host like GitHub Pages, Vercel, Netlify) by simply uploading the root directory files.
