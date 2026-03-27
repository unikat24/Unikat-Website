import os
import re

# Alle HTML-Dateien im aktuellen Verzeichnis
html_files = [f for f in os.listdir('.') if f.endswith('.html')]

replacements = {
    'privat.html#wohnen': 'privat-wohnen.html',
    'privat.html#beruf': 'privat-beruf-familie.html',
    'privat.html#gesundheit': 'privat-gesundheit.html',
    'privat.html#tiere': 'privat-tiere.html'
}

for filename in html_files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = content
    for old, new in replacements.items():
        modified = modified.replace(old, new)
    
    if modified != content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(modified)
        print(f"✓ {filename}")

print("\nFertig!")
