#!/usr/bin/env python3
"""
Font Self-Hosting Migration Script
Entfernt externe Font-Links und aktualisiert auf lokale Fonts
"""

import os
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent

# Neue lokale Font-Preloads
LOCAL_FONT_PRELOADS = '''    <!-- Lokale Fonts (DSGVO-konform) -->
    <link rel="preload" href="fonts/inter-v20-latin-regular.woff2" as="font" type="font/woff2" crossorigin>
    <link rel="preload" href="fonts/inter-v20-latin-700.woff2" as="font" type="font/woff2" crossorigin>
    <link rel="preload" href="fonts/fa-solid-900.woff2" as="font" type="font/woff2" crossorigin>'''

def update_html_files():
    """Entfernt externe Font-Links aus allen HTML-Dateien"""
    html_files = list(BASE_DIR.glob("*.html"))
    
    print(f"🔄 Bearbeite {len(html_files)} HTML-Dateien...")
    
    for html_file in html_files:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 1. Entferne Google Fonts Link
        content = re.sub(
            r'<link href="https://fonts\.googleapis\.com/css2\?family=Inter.*?" rel="stylesheet">\s*',
            '',
            content
        )
        
        # 2. Entferne FontAwesome CDN Link
        content = re.sub(
            r'<link rel="stylesheet" href="https://cdnjs\.cloudflare\.com/ajax/libs/font-awesome/.*?">\s*',
            '<link rel="stylesheet" href="css/fontawesome.css">\n',
            content
        )
        
        # 3. Ersetze alte Preloads durch lokale
        content = re.sub(
            r'<!-- Preload kritischer Fonts.*?crossorigin>\s*',
            LOCAL_FONT_PRELOADS + '\n',
            content,
            flags=re.DOTALL
        )
        
        # 4. Entferne preconnect zu Google Fonts
        content = re.sub(
            r'<link rel="preconnect" href="https://fonts\.googleapis\.com">\s*',
            '',
            content
        )
        content = re.sub(
            r'<link rel="preconnect" href="https://fonts\.gstatic\.com" crossorigin>\s*',
            '',
            content
        )
        
        # 5. Entferne alten Google Fonts Preload
        content = re.sub(
            r'<link rel="preload" href="https://fonts\.gstatic\.com.*?" as="font".*?>\s*',
            '',
            content
        )
        
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ {html_file.name}")

def create_fontawesome_css():
    """Erstellt lokale FontAwesome CSS"""
    css_dir = BASE_DIR / "css"
    css_dir.mkdir(exist_ok=True)
    
    fontawesome_css = '''/* FontAwesome Local (DSGVO-konform) */
@font-face {
    font-family: "Font Awesome 6 Free";
    font-style: normal;
    font-weight: 900;
    font-display: swap;
    src: url("../fonts/fa-solid-900.woff2") format("woff2");
}

@font-face {
    font-family: "Font Awesome 6 Free";
    font-style: normal;
    font-weight: 400;
    font-display: swap;
    src: url("../fonts/fa-regular-400.woff2") format("woff2");
}

@font-face {
    font-family: "Font Awesome 6 Brands";
    font-style: normal;
    font-weight: 400;
    font-display: swap;
    src: url("../fonts/fa-brands-400.woff2") format("woff2");
}

.fa, .fas, .fa-solid {
    font-family: "Font Awesome 6 Free";
    font-weight: 900;
}

.far, .fa-regular {
    font-family: "Font Awesome 6 Free";
    font-weight: 400;
}

.fab, .fa-brands {
    font-family: "Font Awesome 6 Brands";
    font-weight: 400;
}

.fa, .fas, .far, .fab, .fa-solid, .fa-regular, .fa-brands {
    -moz-osx-font-smoothing: grayscale;
    -webkit-font-smoothing: antialiased;
    display: inline-block;
    font-style: normal;
    font-variant: normal;
    line-height: 1;
    text-rendering: auto;
}
'''
    
    with open(css_dir / "fontawesome.css", 'w', encoding='utf-8') as f:
        f.write(fontawesome_css)
    
    print("✅ css/fontawesome.css erstellt")

def main():
    print("=" * 60)
    print("🚀 Font Self-Hosting Migration")
    print("=" * 60)
    
    # 1. HTML-Dateien aktualisieren
    update_html_files()
    
    # 2. FontAwesome CSS erstellen
    create_fontawesome_css()
    
    print("\n" + "=" * 60)
    print("✅ Migration abgeschlossen!")
    print("=" * 60)
    print("\n📋 Nächste Schritte:")
    print("1. Aktualisiere styles.css mit lokalen @font-face Regeln")
    print("2. Teste die Website im Browser")
    print("3. Führe Lighthouse-Audit durch")

if __name__ == "__main__":
    main()
