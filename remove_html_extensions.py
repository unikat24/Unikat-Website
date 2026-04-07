#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script zum Entfernen von .html-Endungen aus internen Links
für GitHub Pages mit Jekyll Pretty URLs
"""

import os
import re
from pathlib import Path

def remove_html_from_links(content):
    """
    Entfernt .html-Endungen aus href-Attributen in HTML-Dateien.
    Behält externe Links und PDF-Links bei.
    """
    
    # Pattern für interne Links mit .html
    # Matcht: href="datei.html" oder href="pfad/datei.html"
    # Aber NICHT: href="http..." oder href="mailto:" oder href="#"
    
    patterns = [
        # Standard href mit .html (ohne Anführungszeichen am Ende)
        (r'href="([^"]*?)\.html"', r'href="\1"'),
        
        # href mit .html gefolgt von Anker
        (r'href="([^"#]*?)\.html(#[^"]*?)"', r'href="\1\2"'),
        
        # Canonical Links
        (r'<link rel="canonical" href="([^"]*?)\.html"', r'<link rel="canonical" href="\1"'),
    ]
    
    modified_content = content
    changes_made = 0
    
    for pattern, replacement in patterns:
        # Zähle Änderungen
        matches = re.findall(pattern, modified_content)
        if matches:
            changes_made += len(matches)
        
        # Ersetze Pattern
        modified_content = re.sub(pattern, replacement, modified_content)
    
    return modified_content, changes_made

def process_html_files(directory):
    """
    Verarbeitet alle HTML-Dateien im angegebenen Verzeichnis.
    """
    
    directory_path = Path(directory)
    html_files = list(directory_path.glob("*.html"))
    
    total_files = 0
    total_changes = 0
    
    print(f"🔍 Gefundene HTML-Dateien: {len(html_files)}\n")
    
    for html_file in html_files:
        try:
            # Lese Datei
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Entferne .html aus Links
            modified_content, changes = remove_html_from_links(content)
            
            if changes > 0:
                # Schreibe modifizierte Datei zurück
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(modified_content)
                
                print(f"✅ {html_file.name}: {changes} Links aktualisiert")
                total_files += 1
                total_changes += changes
            else:
                print(f"⏭️  {html_file.name}: Keine Änderungen nötig")
        
        except Exception as e:
            print(f"❌ Fehler bei {html_file.name}: {str(e)}")
    
    print(f"\n{'='*60}")
    print(f"✨ Fertig!")
    print(f"📊 Dateien bearbeitet: {total_files}")
    print(f"🔗 Links aktualisiert: {total_changes}")
    print(f"{'='*60}")

if __name__ == "__main__":
    # Aktuelles Verzeichnis
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    print("="*60)
    print("🚀 Entferne .html-Endungen aus internen Links")
    print("="*60)
    print(f"📁 Verzeichnis: {current_dir}\n")
    
    # Verarbeite alle HTML-Dateien
    process_html_files(current_dir)
