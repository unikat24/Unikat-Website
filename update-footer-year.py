#!/usr/bin/env python3
"""
Footer Year Update Script
Aktualisiert das Copyright-Jahr im Footer von 2025 auf 2026 in allen HTML-Dateien.
"""

import os
import re
from pathlib import Path

def update_footer_year(file_path):
    """
    Aktualisiert das Jahr im Footer einer HTML-Datei von 2025 auf 2026.
    
    Args:
        file_path: Pfad zur HTML-Datei
        
    Returns:
        True wenn Änderungen vorgenommen wurden, False sonst
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Suche nach dem Copyright-Jahr im Footer
        # Pattern: &copy; 2025 oder © 2025
        pattern = r'(&copy;|©)\s*2025\s+Unikat'
        replacement = r'\g<1> 2026 Unikat'
        
        new_content = re.sub(pattern, replacement, content)
        
        # Prüfen ob Änderungen vorgenommen wurden
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True
        
        return False
        
    except Exception as e:
        print(f"❌ Fehler bei {file_path}: {e}")
        return False

def main():
    """Hauptfunktion: Durchsucht alle HTML-Dateien und aktualisiert das Jahr."""
    
    # Aktuelles Verzeichnis
    base_dir = Path(__file__).parent
    
    # Zähler
    updated_files = []
    skipped_files = []
    
    print("🔍 Suche nach HTML-Dateien mit Footer-Jahr 2025...\n")
    
    # Alle HTML-Dateien im Hauptverzeichnis durchsuchen
    for html_file in base_dir.glob('*.html'):
        file_name = html_file.name
        
        # Backup-Ordner überspringen
        if 'backup' in str(html_file).lower():
            continue
        
        print(f"📄 Prüfe: {file_name}...", end=' ')
        
        if update_footer_year(html_file):
            updated_files.append(file_name)
            print("✅ Aktualisiert")
        else:
            skipped_files.append(file_name)
            print("⏭️  Übersprungen (kein 2025 gefunden)")
    
    # Zusammenfassung
    print("\n" + "="*60)
    print("📊 ZUSAMMENFASSUNG")
    print("="*60)
    print(f"✅ Aktualisiert: {len(updated_files)} Dateien")
    if updated_files:
        for file in updated_files:
            print(f"   - {file}")
    
    print(f"\n⏭️  Übersprungen: {len(skipped_files)} Dateien")
    if skipped_files and len(skipped_files) <= 5:
        for file in skipped_files:
            print(f"   - {file}")
    elif skipped_files:
        print(f"   (Liste zu lang, {len(skipped_files)} Dateien)")
    
    print("\n✨ Fertig!")

if __name__ == "__main__":
    main()
