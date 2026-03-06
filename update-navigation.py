#!/usr/bin/env python3
"""
Script to add Kontakt link to navigation in all HTML files
"""

import os
import re

# List of HTML files to update
files_to_update = [
    'privat.html',
    'ueber-unikat.html',
    'schaden.html',
    'kundenportal.html',
    'unternehmen-immobilien.html',
    'unternehmen-logistik.html',
    'unternehmen-cyber.html',
    'unternehmen-sozialwirtschaft.html',
    'unternehmen-mittelstand.html',
    'unternehmen-versorgung.html',
    'privat-wohnen.html',
    'privat-beruf-familie.html',
    'privat-gesundheit.html',
    'privat-tiere.html',
    'privat-betriebliche-vorsorge.html',
    'impressum.html',
    'datenschutz.html',
    'erstinformation.html'
]

# Pattern to find (navigation section before Kundenportal)
pattern = r'(<div class="nav-item"><a href="ueber-unikat\.html" class="nav-link">Über Unikat</a></div>)\s*(\n\s*<div class="nav-item">\s*\n\s*<a href="kundenportal\.html")'

# Replacement (adds Kontakt link)
replacement = r'\1\n                <div class="nav-item"><a href="kontakt.html" class="nav-link">Kontakt</a></div>\2'

def update_file(filename):
    """Update a single HTML file"""
    if not os.path.exists(filename):
        print(f"⚠️  Datei nicht gefunden: {filename}")
        return False
    
    try:
        # Read file
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if already updated
        if 'href="kontakt.html"' in content:
            print(f"✅ Bereits aktualisiert: {filename}")
            return True
        
        # Apply replacement
        new_content = re.sub(pattern, replacement, content, flags=re.MULTILINE)
        
        # Check if replacement was made
        if new_content == content:
            print(f"⚠️  Kein Match gefunden: {filename}")
            return False
        
        # Write back
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"✅ Aktualisiert: {filename}")
        return True
        
    except Exception as e:
        print(f"❌ Fehler bei {filename}: {e}")
        return False

def main():
    """Main function"""
    print("🚀 Starte Navigation-Update...\n")
    
    updated = 0
    skipped = 0
    errors = 0
    
    for filename in files_to_update:
        result = update_file(filename)
        if result:
            if 'Bereits aktualisiert' in str(result):
                skipped += 1
            else:
                updated += 1
        else:
            errors += 1
    
    print(f"\n📊 Zusammenfassung:")
    print(f"   ✅ Aktualisiert: {updated}")
    print(f"   ⏭️  Übersprungen: {skipped}")
    print(f"   ❌ Fehler: {errors}")
    print(f"   📝 Gesamt: {len(files_to_update)}")

if __name__ == '__main__':
    main()
