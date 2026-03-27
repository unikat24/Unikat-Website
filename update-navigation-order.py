#!/usr/bin/env python3
"""
Script to update navigation order across all HTML files:
1. Unternehmen before Privat
2. Immobilien & Verwalter first in Unternehmen dropdown
"""

import os
import re

# List of HTML files to update
files_to_update = [
    'index.html',
    'kontakt.html',
    'privat.html',
    'ueber-unikat.html',
    'schaden.html',
    'kundenportal.html',
    'unternehmen.html',
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
    'erstinformation.html',
    'wertpapierdienstleistungen.html',
    'danke.html',
    'danke-immo.html',
    'danke-logistik-download.html'
]

def update_dropdown_order(content):
    """Update Unternehmen dropdown order: Immobilien first"""
    # Pattern to find the dropdown menu
    dropdown_pattern = r'(<div class="dropdown-menu">)(.*?)(</div>\s*</div>)'
    
    def reorder_dropdown(match):
        opening = match.group(1)
        items = match.group(2)
        closing = match.group(3)
        
        # Extract all dropdown links
        logistik = re.search(r'<a href="unternehmen-logistik\.html"[^>]*>.*?</a>', items)
        immobilien = re.search(r'<a href="unternehmen-immobilien\.html"[^>]*>.*?</a>', items)
        versorgung = re.search(r'<a href="unternehmen-versorgung\.html"[^>]*>.*?</a>', items)
        sozial = re.search(r'<a href="unternehmen-sozialwirtschaft\.html"[^>]*>.*?</a>', items)
        mittelstand = re.search(r'<a href="unternehmen-mittelstand\.html"[^>]*>.*?</a>', items)
        cyber = re.search(r'<a href="unternehmen-cyber\.html"[^>]*>.*?</a>', items)
        
        # Rebuild in correct order
        new_items = '\n                        '
        if immobilien:
            new_items += immobilien.group(0) + '\n                        '
        if logistik:
            new_items += logistik.group(0) + '\n                        '
        if versorgung:
            new_items += versorgung.group(0) + '\n                        '
        if sozial:
            new_items += sozial.group(0) + '\n                        '
        if mittelstand:
            new_items += mittelstand.group(0) + '\n                        '
        if cyber:
            new_items += cyber.group(0) + '\n                    '
        
        return opening + new_items + closing
    
    return re.sub(dropdown_pattern, reorder_dropdown, content, flags=re.DOTALL)

def update_main_nav_order(content):
    """Swap Privat and Unternehmen if needed"""
    # Check if Privat comes before Unternehmen
    privat_pos = content.find('href="privat.html"')
    unternehmen_pos = content.find('href="unternehmen.html"')
    
    if privat_pos == -1 or unternehmen_pos == -1:
        return content  # One of them not found, skip
    
    if privat_pos < unternehmen_pos:
        # Need to swap - find the nav-item blocks
        # Pattern for Privat dropdown
        privat_pattern = r'(<div class="nav-item dropdown">\s*<a href="privat\.html".*?</div>\s*</div>\s*</div>)'
        # Pattern for Unternehmen dropdown  
        unternehmen_pattern = r'(<div class="nav-item dropdown">\s*<a href="unternehmen\.html".*?</div>\s*</div>\s*</div>)'
        
        privat_match = re.search(privat_pattern, content, re.DOTALL)
        unternehmen_match = re.search(unternehmen_pattern, content, re.DOTALL)
        
        if privat_match and unternehmen_match:
            privat_block = privat_match.group(1)
            unternehmen_block = unternehmen_match.group(1)
            
            # Remove both blocks
            content = content.replace(privat_block, '<<<PRIVAT_PLACEHOLDER>>>')
            content = content.replace(unternehmen_block, '<<<UNTERNEHMEN_PLACEHOLDER>>>')
            
            # Swap them
            content = content.replace('<<<PRIVAT_PLACEHOLDER>>>', unternehmen_block)
            content = content.replace('<<<UNTERNEHMEN_PLACEHOLDER>>>', privat_block)
    
    return content

def update_file(filename):
    """Update a single HTML file"""
    if not os.path.exists(filename):
        print(f"⚠️  Datei nicht gefunden: {filename}")
        return False
    
    try:
        # Read file
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Apply updates
        content = update_main_nav_order(content)
        content = update_dropdown_order(content)
        
        # Check if changes were made
        if content == original_content:
            print(f"✅ Keine Änderungen nötig: {filename}")
            return True
        
        # Write back
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Aktualisiert: {filename}")
        return True
        
    except Exception as e:
        print(f"❌ Fehler bei {filename}: {e}")
        return False

def main():
    """Main function"""
    print("🚀 Starte Navigation-Reihenfolge-Update...\n")
    
    updated = 0
    skipped = 0
    errors = 0
    
    for filename in files_to_update:
        result = update_file(filename)
        if result:
            if 'Keine Änderungen' in str(result):
                skipped += 1
            else:
                updated += 1
        else:
            errors += 1
    
    print(f"\n📊 Zusammenfassung:")
    print(f"   ✅ Aktualisiert: {updated}")
    print(f"   ⏭️  Keine Änderungen: {skipped}")
    print(f"   ❌ Fehler: {errors}")
    print(f"   📝 Gesamt: {len(files_to_update)}")

if __name__ == '__main__':
    main()
