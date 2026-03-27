#!/usr/bin/env python3
"""
Script to fix navigation on all HTML files:
- Restore complete Privat dropdown
- Ensure correct order (Unternehmen before Privat)
"""

import os
import re

# Correct navigation template
CORRECT_NAV = '''            <nav class="nav-menu">
                <div class="nav-item dropdown">
                    <a href="unternehmen.html" class="nav-link">Unternehmen <i class="fa-solid fa-chevron-down dropdown-icon"></i></a>
                    <div class="dropdown-menu">
                        <a href="unternehmen-immobilien.html" class="dropdown-link">Immobilien & Verwalter</a>
                        <a href="unternehmen-logistik.html" class="dropdown-link">Logistik & Flotten</a>
                        <a href="unternehmen-versorgung.html" class="dropdown-link">Betriebliche Versorgung</a>
                        <a href="unternehmen-sozialwirtschaft.html" class="dropdown-link">Sozialwirtschaft & Pflege</a>
                        <a href="unternehmen-mittelstand.html" class="dropdown-link">Mittelstand & Gewerbe</a>
                        <a href="unternehmen-cyber.html" class="dropdown-link">Cyber & IT-Schutz</a>
                    </div>
                </div>
                
                <div class="nav-item dropdown">
                    <a href="privat.html" class="nav-link">Privat <i class="fa-solid fa-chevron-down dropdown-icon"></i></a>
                    <div class="dropdown-menu">
                        <a href="privat.html#wohnen" class="dropdown-link">Wohnen & Eigentum</a>
                        <a href="privat.html#beruf" class="dropdown-link">Beruf & Familie</a>
                        <a href="privat.html#gesundheit" class="dropdown-link">Gesundheit & Pflege</a>
                        <a href="privat.html#tiere" class="dropdown-link">Tiere & Pferde</a>
                        <a href="privat-betriebliche-vorsorge.html" class="dropdown-link">Betriebsrente (für Arbeitnehmer)</a>
                    </div>
                </div>

                <div class="nav-item"><a href="ueber-unikat.html" class="nav-link">Über Unikat</a></div>
                <div class="nav-item"><a href="kontakt.html" class="nav-link">Kontakt</a></div>
                
                <div class="nav-item">
                    <a href="kundenportal.html" class="btn btn-primary btn-sm">Kundenportal</a>
                </div>
            </nav>'''

# List of HTML files to update
files_to_update = [
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

def fix_navigation(filename):
    """Fix navigation in a single HTML file"""
    if not os.path.exists(filename):
        print(f"⚠️  Datei nicht gefunden: {filename}")
        return False
    
    try:
        # Read file
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Pattern to find the nav-menu section
        pattern = r'<nav class="nav-menu">.*?</nav>'
        
        # Check if nav-menu exists
        if not re.search(pattern, content, re.DOTALL):
            print(f"⚠️  Keine Navigation gefunden: {filename}")
            return False
        
        # Replace navigation
        new_content = re.sub(pattern, CORRECT_NAV, content, flags=re.DOTALL)
        
        # Check if changes were made
        if new_content == content:
            print(f"✅ Bereits korrekt: {filename}")
            return True
        
        # Write back
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"✅ Repariert: {filename}")
        return True
        
    except Exception as e:
        print(f"❌ Fehler bei {filename}: {e}")
        return False

def main():
    """Main function"""
    print("🚀 Starte Navigation-Reparatur...\n")
    
    fixed = 0
    already_ok = 0
    errors = 0
    
    for filename in files_to_update:
        result = fix_navigation(filename)
        if result:
            if 'Bereits korrekt' in str(result):
                already_ok += 1
            else:
                fixed += 1
        else:
            errors += 1
    
    print(f"\n📊 Zusammenfassung:")
    print(f"   ✅ Repariert: {fixed}")
    print(f"   ✓  Bereits korrekt: {already_ok}")
    print(f"   ❌ Fehler: {errors}")
    print(f"   📝 Gesamt: {len(files_to_update)}")

if __name__ == '__main__':
    main()
