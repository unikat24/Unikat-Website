#!/usr/bin/env python3
"""
WebP Conversion Script
Ersetzt alle .jpg Referenzen durch .webp in HTML und CSS Dateien
"""

import os
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent

def convert_html_files():
    """Ersetzt .jpg durch .webp in allen HTML-Dateien"""
    html_files = [f for f in BASE_DIR.glob("*.html") if not f.name.startswith("backup")]
    
    print(f"🔄 Bearbeite {len(html_files)} HTML-Dateien...")
    
    for html_file in html_files:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Ersetze alle .jpg durch .webp
        content = content.replace('.jpg', '.webp')
        
        if content != original_content:
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ {html_file.name}")
        else:
            print(f"⏭️  {html_file.name} (keine Änderungen)")

def convert_css_files():
    """Ersetzt .jpg durch .webp in CSS-Dateien"""
    css_file = BASE_DIR / "styles.css"
    
    print(f"\n🔄 Bearbeite styles.css...")
    
    with open(css_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Ersetze alle .jpg durch .webp
    content = content.replace('.jpg', '.webp')
    
    if content != original_content:
        with open(css_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ styles.css")
    else:
        print(f"⏭️  styles.css (keine Änderungen)")

def main():
    print("=" * 60)
    print("🚀 WebP Conversion Script")
    print("=" * 60)
    
    # 1. HTML-Dateien konvertieren
    convert_html_files()
    
    # 2. CSS-Dateien konvertieren
    convert_css_files()
    
    print("\n" + "=" * 60)
    print("✅ Konvertierung abgeschlossen!")
    print("=" * 60)
    print("\n📋 Alle .jpg Referenzen wurden durch .webp ersetzt")
    print("🔍 Teste die Website im Browser")
    print("📊 Führe Lighthouse-Audit durch")

if __name__ == "__main__":
    main()
