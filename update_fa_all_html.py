#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script zum Ersetzen von fontawesome.css durch all.min.css in allen HTML-Dateien
"""

import os
from pathlib import Path

def update_fa_css_in_html():
    """
    Ersetzt <link rel="stylesheet" href="css/fontawesome.css"> 
    durch <link rel="stylesheet" href="css/all.min.css"> in allen HTML-Dateien.
    """
    
    directory_path = Path('.')
    html_files = list(directory_path.glob("*.html"))
    
    total_files = 0
    
    print(f"🔍 Gefundene HTML-Dateien: {len(html_files)}\n")
    
    for html_file in html_files:
        try:
            # Lese Datei
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Prüfe, ob fontawesome.css vorhanden ist
            if 'css/fontawesome.css' in content:
                # Ersetze durch all.min.css
                modified_content = content.replace('css/fontawesome.css', 'css/all.min.css')
                
                # Schreibe zurück
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(modified_content)
                
                print(f"✅ {html_file.name}: fontawesome.css → all.min.css")
                total_files += 1
            else:
                print(f"⏭️  {html_file.name}: Keine Änderung nötig")
        
        except Exception as e:
            print(f"❌ Fehler bei {html_file.name}: {str(e)}")
    
    print(f"\n{'='*60}")
    print(f"✨ Fertig!")
    print(f"📊 Dateien aktualisiert: {total_files}")
    print(f"{'='*60}")

if __name__ == "__main__":
    print("="*60)
    print("🔄 Ersetze fontawesome.css durch all.min.css")
    print("="*60)
    print()
    
    update_fa_css_in_html()
