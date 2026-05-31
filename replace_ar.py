import os
import json

def replace_in_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace("نوترا صقر", "نيوترا صقر")
    content = content.replace("نوترا", "نيوترا")
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

replace_in_file('data/ar/ui.json')
replace_in_file('data/ar/products.json')
replace_in_file('generate_site.py')
