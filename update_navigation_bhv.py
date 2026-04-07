#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script zum Hinzufügen des BHV-Links in die Navigation aller HTML-Dateien
"""

import os
import re
from pathlib import Path

def add_bhv_to_navigation(content):
    """
    Fügt den BHV-Link in die Unternehmen-Navigation ein.
    """
    
    # Pattern: Suche nach dem Cyber-Link und füge BHV danach ein
    pattern = r'(<a href="unternehmen-cyber" class="dropdown-link">Cyber & IT-Schutz</a>\s*</div>)'
    
    # Prüfe, ob BHV bereits vorhanden ist
    if 'unternehmen-betriebshaftpflicht' in content:
        return content, False
    
    # Ersetze und füge BHV-Link hinzu
    replacement = r'<a href="unternehmen-cyber" class="dropdown-link">Cyber & IT-Schutz</a>\n                        <a href="unternehmen-betriebshaftpflicht" class="dropdown-link">Betriebshaftpflicht (BHV)</a>\n                    </div>'
    
    modified_content = re.sub(pattern, replacement, content)
    
    # Prüfe, ob Änderung erfolgt ist
    changed = modified_content != content
    
    return modified_content, changed

def process_html_files(directory):
    """
    Verarbeitet alle HTML-Dateien im angegebenen Verzeichnis.
    """
    
    directory_path = Path(directory)
    html_files = [f for f in directory_path.glob("*.html") if f.name != 'unternehmen-betriebshaftpflicht.html']
    
    total_files = 0
    
    print(f"🔍 Gefundene HTML-Dateien: {len(html_files)}\n")
    
    for html_file in html_files:
        try:
            # Lese Datei
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Füge BHV-Link hinzu
            modified_content, changed = add_bhv_to_navigation(content)
            
            if changed:
                # Schreibe modifizierte Datei zurück
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(modified_content)
                
                print(f"✅ {html_file.name}: BHV-Link hinzugefügt")
                total_files += 1
            else:
                print(f"⏭️  {html_file.name}: Bereits aktuell oder keine Navigation gefunden")
        
        except Exception as e:
            print(f"❌ Fehler bei {html_file.name}: {str(e)}")
    
    print(f"\n{'='*60}")
    print(f"✨ Fertig!")
    print(f"📊 Dateien aktualisiert: {total_files}")
    print(f"{'='*60}")

if __name__ == "__main__":
    # Aktuelles Verzeichnis
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    print("="*60)
    print("🚀 Füge BHV-Link zur Navigation hinzu")
    print("="*60)
    print(f"📁 Verzeichnis: {current_dir}\n")
    
    # Verarbeite alle HTML-Dateien
    process_html_files(current_dir)
