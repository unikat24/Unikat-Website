#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script zum Hinzufügen von .html-Endungen zu allen internen Links in der BHV-Seite
"""

import re

def fix_links_in_bhv():
    """
    Fügt .html-Endungen zu allen internen Links in der BHV-Seite hinzu.
    """
    
    file_path = 'unternehmen-betriebshaftpflicht.html'
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Liste der internen Seiten (ohne .html)
    internal_pages = [
        'unternehmen', 'schaden', 'kontakt', 'ueber-unikat', 'privat',
        'unternehmen-immobilien', 'unternehmen-logistik', 'unternehmen-mittelstand',
        'unternehmen-versorgung', 'unternehmen-sozialwirtschaft', 'unternehmen-cyber',
        'unternehmen-betriebshaftpflicht', 'kundenportal', 'impressum', 'datenschutz',
        'erstinformation', 'privat-wohnen', 'privat-beruf-familie', 'privat-gesundheit',
        'privat-tiere', 'privat-betriebliche-vorsorge'
    ]
    
    changes = 0
    
    for page in internal_pages:
        # Pattern: href="page" (ohne .html, ohne http, ohne mailto, ohne #)
        pattern = f'href="{page}"'
        replacement = f'href="{page}.html"'
        
        if pattern in content:
            content = content.replace(pattern, replacement)
            count = content.count(replacement)
            changes += count
            print(f"✅ {page}: {count} Links aktualisiert")
    
    # Schreibe zurück
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"\n{'='*60}")
    print(f"✨ Fertig! {changes} Links mit .html-Endung versehen")
    print(f"{'='*60}")

if __name__ == "__main__":
    print("="*60)
    print("🔧 Füge .html-Endungen zu BHV-Links hinzu")
    print("="*60)
    fix_links_in_bhv()
