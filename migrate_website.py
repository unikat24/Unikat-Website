#!/usr/bin/env python3
"""
Website Migration Script für Unikat Versicherungsmakler
Automatisiert Header/Footer Inlining, WebP-Migration und Head-Synchronisation
"""

import os
import re
import shutil
from pathlib import Path
from datetime import datetime

# Konfiguration
BASE_DIR = Path(__file__).parent
BACKUP_DIR = BASE_DIR / f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

# Header und Footer aus index.html extrahieren
HEADER_HTML = '''<!-- HEADER INLINE (kein JavaScript-Loading mehr) -->
    <div class="top-bar">
        <div class="container top-bar-inner">
            
            <div class="top-contact">
                <a href="tel:+493816691930" class="contact-link" aria-label="Telefonnummer anrufen">
                    <i class="fa-solid fa-phone"></i> 0381 669193 0
                </a>

                <a href="https://wa.me/493816691930" class="contact-link whatsapp-link" target="_blank" rel="noopener noreferrer" aria-label="Nachricht per WhatsApp senden">
                    <i class="fa-brands fa-whatsapp"></i> WhatsApp
                </a>
            </div>

            <div class="top-actions">
                <a href="https://outlook.office365.com/owa/calendar/UnikatVersicherungsmaklerGmbH@unikat24.de/bookings/" target="_blank" rel="noopener noreferrer" class="top-link-accent">
                    <i class="fa-regular fa-calendar-check"></i> Termin buchen
                </a>
                
                <a href="schaden.html" class="btn-signal-small">
                    <i class="fa-solid fa-triangle-exclamation"></i> Schaden melden
                </a>
            </div>
        </div>
    </div>

    <header class="site-header">
        <div class="container nav-container">
            
            <div class="logo-group">
                <a href="/">
                    <img src="img/logo.png" alt="Unikat Versicherungsmakler Rostock Logo" class="logo-main" width="200" height="60" loading="eager">
                </a>
            </div>
            
            <div class="burger-menu" aria-label="Menü öffnen">
                <i class="fa-solid fa-bars"></i>
            </div>

            <nav class="nav-menu">
                <div class="nav-item"><a href="/" class="nav-link">Start</a></div>
                
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

                <div class="nav-item dropdown">
                    <a href="unternehmen.html" class="nav-link">Unternehmen <i class="fa-solid fa-chevron-down dropdown-icon"></i></a>
                    <div class="dropdown-menu">
                        <a href="unternehmen-logistik.html" class="dropdown-link">Logistik & Flotten</a>
                        <a href="unternehmen-immobilien.html" class="dropdown-link">Immobilien & Verwalter</a>
                        <a href="unternehmen-versorgung.html" class="dropdown-link">Betriebliche Versorgung</a>
                        <a href="unternehmen-sozialwirtschaft.html" class="dropdown-link">Sozialwirtschaft & Pflege</a>
                        <a href="unternehmen-mittelstand.html" class="dropdown-link">Mittelstand & Gewerbe</a>
                        <a href="unternehmen-cyber.html" class="dropdown-link">Cyber & IT-Schutz</a>
                    </div>
                </div>

                <div class="nav-item"><a href="ueber-unikat.html" class="nav-link">Über Unikat</a></div>
                
                <div class="nav-item">
                    <a href="kundenportal.html" class="btn btn-primary btn-sm">Kundenportal</a>
                </div>
            </nav>
        </div>
    </header>'''

FOOTER_HTML = '''<!-- FOOTER INLINE (kein JavaScript-Loading mehr) -->
    <footer class="footer-section">
        <div class="container">
            <div class="footer-grid">
                
                <div class="footer-col">
                    <a href="/">
                        <img src="img/logo.png" alt="Unikat Versicherungsmakler Logo" width="150" height="45" loading="lazy" style="height: 45px; margin-bottom: 20px; opacity: 0.95; filter: brightness(0) invert(1);">
                    </a>
                    
                    <p style="font-size: 0.95rem; line-height: 1.6; color: #cbd5e1;">
                        <strong>Unikat Versicherungsmakler GmbH</strong><br>
                        Ihr Partner vor Ort in der August-Bebel-Straße 11,<br>
                        <strong>18055 Rostock</strong>.
                    </p>
                    
                    <ul class="contact-list">
                        <li><i class="fa-solid fa-phone"></i> <a href="tel:+493816691930">0381 669193 0</a></li>
                        <li><i class="fa-solid fa-envelope"></i> <a href="mailto:info@unikat24.de">info@unikat24.de</a></li>
                    </ul>

                    <div style="margin-top: 25px; display: flex; gap: 15px; align-items: center; flex-wrap: wrap;">
                        <a href="https://www.linkedin.com/company/unikat-versicherungsmakler-gmbh/" target="_blank" rel="noopener noreferrer" aria-label="LinkedIn" title="Folgen Sie uns auf LinkedIn" style="color: white; font-size: 1.4rem; transition: 0.3s;">
                            <i class="fa-brands fa-linkedin"></i>
                        </a>
                        <a href="https://www.facebook.com/unikatversicherungsmaklergmbh/" target="_blank" rel="noopener noreferrer" aria-label="Facebook" title="Besuchen Sie uns auf Facebook" style="color: white; font-size: 1.4rem; transition: 0.3s;">
                            <i class="fa-brands fa-facebook"></i>
                        </a>
                        <a href="https://share.google/hpFKiHGfPf8xHQE2K" target="_blank" rel="noopener" aria-label="Google Bewertungen" title="Direkt zu unserem Google-Profil" style="color: white; font-size: 1.4rem; transition: 0.3s;">
                            <i class="fa-brands fa-google"></i>
                        </a>
                        <a href="https://wa.me/493816691930" target="_blank" rel="noopener noreferrer" aria-label="WhatsApp" title="Schreiben Sie uns auf WhatsApp" style="color: var(--whatsapp-green); font-size: 1.5rem; transition: 0.3s;">
                            <i class="fa-brands fa-whatsapp"></i>
                        </a>
                        
                        <a href="mailto:info@unikat24.de?subject=Initiativbewerbung" class="career-badge">
                            <i class="fa-solid fa-briefcase"></i> Karriere / Jobs
                        </a>
                    </div>
                </div>

                <div class="footer-col">
                    <h2 style="font-size: 1.2rem; margin-bottom: 1rem;">Service & Recht</h2>
                    <ul class="footer-links">
                        <li><a href="impressum.html">Impressum</a></li>
                        <li><a href="datenschutz.html">Datenschutz</a></li>
                        <li><a href="erstinformation.html">Erstinformation</a> <a href="erstinformation.pdf" target="_blank" rel="noopener noreferrer" aria-label="Erstinformation als PDF laden" style="font-size: 0.8em; opacity: 0.7;"><i class="fa-solid fa-file-pdf"></i> (PDF)</a></li>
                        <li><a href="#" id="open-cookie-settings">Cookie-Einstellungen</a></li>
                        <li><a href="schaden.html" style="color: #ef4444; font-weight: 700;"><i class="fa-solid fa-triangle-exclamation" style="margin-right: 5px;"></i> Schaden melden</a></li>
                    </ul>

                    <h3 style="margin-top: 25px; font-size: 1rem; opacity: 0.8;">Online Rechner</h3>
                    <ul class="footer-links" style="font-size: 0.9rem;">
                        <li>
                            <a href="https://apps.nafi.de/NOVA/login/nafi_ndo_1021141198_20210112145536/V3N0eqh6J" target="_blank" rel="noopener noreferrer">
                                Vergleichsrechner Privat <i class="fa-solid fa-arrow-up-right-from-square" style="font-size: 0.7em;"></i>
                            </a>
                        </li>
                        <li>
                            <a href="https://ts.thinksurance.de/p/151f048b5b35cb35" target="_blank" rel="noopener noreferrer">
                                Gewerbe Rechner <i class="fa-solid fa-arrow-up-right-from-square" style="font-size: 0.7em;"></i>
                            </a>
                        </li>
                    </ul>
                </div>

                <div class="footer-col trust-col">
                    <h2 style="font-size: 1.2rem; margin-bottom: 1rem;">Geprüfte Qualität</h2>
                    
                    <div class="trust-primary">
                        <a href="img/iso-zertifikat.pdf" target="_blank" rel="noopener noreferrer" aria-label="ISO 9001 Zertifikat ansehen" class="iso-badge" style="text-decoration: none; color: inherit;">
                            <img src="img/zertifikat.jpg" alt="ISO 9001 Zertifikat" width="120" height="120" loading="lazy">
                            <span>Zertifiziert nach<br><strong>DIN EN ISO 9001</strong></span>
                        </a>
                        
                        <a href="https://share.google/hpFKiHGfPf8xHQE2K" target="_blank" rel="noopener" class="google-badge" title="Direkt zu unserem Google-Profil">
                            <div class="stars">★★★★★</div>
                            <span>5,0 bei 80 Bewertungen</span>
                        </a>
                    </div>

                    <div class="trust-secondary">
                        <a href="https://www.vema-eg.de" target="_blank" rel="noopener noreferrer" style="text-decoration: none; opacity: 0.9;">
                            <img src="img/vema.png" alt="Partner der VEMA eG" class="vema-logo" width="120" height="80" loading="lazy">
                        </a>
                        <span>Starker Partner im VEMA-Verbund</span>
                    </div>
                </div>

            </div>

            <div class="footer-bottom">
                <p>&copy; 2025 Unikat Versicherungsmakler GmbH | <span style="opacity: 0.7;">Aus Rostock für den Norden.</span></p>
            </div>
        </div>
    </footer>

    <a href="https://wa.me/493816691930" class="whatsapp-float" target="_blank" rel="noopener noreferrer" aria-label="WhatsApp Chat starten">
        <i class="fa-brands fa-whatsapp"></i>
    </a>'''

FONT_PRELOADS = '''    <!-- Preload kritischer Fonts für besseren CLS -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="preload" href="https://fonts.gstatic.com/s/inter/v13/UcCO3FwrK3iLTeHuS_fvQtMwCp50KnMw2boKoduKmMEVuLyfAZ9hiA.woff2" as="font" type="font/woff2" crossorigin>
    '''

FONT_DISPLAY_CSS = '''    <style>
        /* Font-display swap für besseren CLS */
        @font-face {
            font-family: 'Inter';
            font-display: swap;
        }
    </style>'''

MOBILE_NAV_SCRIPT = '''    <!-- Navigation JavaScript (nur für Mobile-Menü, kein Header/Footer-Loading mehr) -->
    <script>
        // Mobile Burger Menü
        const burger = document.querySelector('.burger-menu');
        const nav = document.querySelector('.nav-menu');
        
        if (burger && nav) {
            burger.addEventListener('click', () => {
                nav.classList.toggle('active');
            });
        }

        // Dropdown für Mobile/Tablet
        const dropdownTriggers = document.querySelectorAll('.nav-item > a i.fa-chevron-down');
        
        dropdownTriggers.forEach(trigger => {
            const parentLink = trigger.parentElement;
            
            parentLink.addEventListener('click', (e) => {
                if (window.innerWidth <= 1024) {
                    e.preventDefault();
                    const navItem = parentLink.parentElement;
                    navItem.classList.toggle('open');
                }
            });
        });
    </script>'''


def create_backup():
    """Erstellt Backup aller HTML-Dateien"""
    print(f"📦 Erstelle Backup in: {BACKUP_DIR}")
    BACKUP_DIR.mkdir(exist_ok=True)
    
    for html_file in BASE_DIR.glob("*.html"):
        shutil.copy2(html_file, BACKUP_DIR / html_file.name)
    
    print(f"✅ Backup erstellt: {len(list(BACKUP_DIR.glob('*.html')))} Dateien")


def migrate_html_file(filepath):
    """Migriert eine einzelne HTML-Datei"""
    print(f"🔄 Bearbeite: {filepath.name}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Header Placeholder ersetzen
    content = re.sub(
        r'<div id="header-placeholder"></div>',
        HEADER_HTML,
        content
    )
    
    # 2. Footer Placeholder ersetzen
    content = re.sub(
        r'<div id="footer-placeholder"></div>',
        FOOTER_HTML,
        content
    )
    
    # 3. main.js Script-Tag entfernen (aber cookie-consent.js behalten)
    content = re.sub(
        r'\s*<script src="main\.js"></script>\s*',
        '\n',
        content
    )
    
    # 4. Mobile Nav Script vor cookie-consent.js einfügen
    if MOBILE_NAV_SCRIPT not in content:
        content = content.replace(
            '<script src="js/cookie-consent.js"></script>',
            f'{MOBILE_NAV_SCRIPT}\n    \n    <script src="js/cookie-consent.js"></script>'
        )
    
    # 5. Font Preloads einfügen (nach <meta> Tags, vor <link rel="stylesheet">)
    if 'Preload kritischer Fonts' not in content:
        content = re.sub(
            r'(\s*<link rel="stylesheet" href="styles\.css">)',
            f'{FONT_PRELOADS}\n\\1',
            content
        )
    
    # 6. Font-display CSS einfügen (nach Font Awesome, vor </head>)
    if 'Font-display swap' not in content:
        content = re.sub(
            r'(<link rel="stylesheet" href="https://cdnjs\.cloudflare\.com/ajax/libs/font-awesome/.*?">)',
            f'\\1\n{FONT_DISPLAY_CSS}',
            content
        )
    
    # 7. WebP-Migration
    webp_replacements = {
        'hero-rostock-bg.jpg': 'hero-rostock-bg.webp',
        'unikat-buero-aussen.jpg': 'unikat-buero-aussen.webp',
        'strand_familie.jpg': 'strand_familie.webp',
        'zertifikat.jpg': 'zertifikat.webp',
        'favicon.png': 'favicon.webp',
    }
    
    for old, new in webp_replacements.items():
        content = content.replace(old, new)
    
    # 8. rel="noopener noreferrer" bei target="_blank" ergänzen (falls noch nicht vorhanden)
    content = re.sub(
        r'target="_blank"(?!\s+rel=)',
        'target="_blank" rel="noopener noreferrer"',
        content
    )
    
    # Datei speichern
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ {filepath.name} migriert")


def update_main_js():
    """Entfernt Header/Footer-Loading aus main.js"""
    main_js_path = BASE_DIR / "main.js"
    
    if not main_js_path.exists():
        print("⚠️  main.js nicht gefunden")
        return
    
    print("🔄 Aktualisiere main.js...")
    
    # Backup
    shutil.copy2(main_js_path, BACKUP_DIR / "main.js")
    
    # Neue main.js (nur Mobile-Menü-Logik)
    new_content = '''/* DATEI: main.js - Nur Mobile Navigation (Header/Footer sind jetzt inline) */

function initNavigation() {
    // 1. Burger Menü Logik
    const burger = document.querySelector('.burger-menu');
    const nav = document.querySelector('.nav-menu');
    
    if (burger && nav) {
        burger.addEventListener('click', () => {
            nav.classList.toggle('active');
        });
    }

    // 2. Dropdown Logik für Tablet/Mobile (Klick statt Hover)
    const dropdownTriggers = document.querySelectorAll('.nav-item > a i.fa-chevron-down');
    
    dropdownTriggers.forEach(trigger => {
        const parentLink = trigger.parentElement;
        
        parentLink.addEventListener('click', (e) => {
            if (window.innerWidth <= 1024) {
                e.preventDefault();
                const navItem = parentLink.parentElement;
                navItem.classList.toggle('open');
            }
        });
    });
}

// Initialisiere Navigation wenn DOM bereit ist
document.addEventListener("DOMContentLoaded", () => {
    initNavigation();
});
'''
    
    with open(main_js_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print("✅ main.js aktualisiert")


def main():
    """Hauptfunktion"""
    print("=" * 60)
    print("🚀 Unikat Website Migration Script")
    print("=" * 60)
    
    # 1. Backup erstellen
    create_backup()
    
    # 2. Alle HTML-Dateien migrieren (außer index.html, die ist schon fertig)
    html_files = [f for f in BASE_DIR.glob("*.html") if f.name != "index.html"]
    
    print(f"\n📝 Migriere {len(html_files)} HTML-Dateien...")
    
    for html_file in html_files:
        try:
            migrate_html_file(html_file)
        except Exception as e:
            print(f"❌ Fehler bei {html_file.name}: {e}")
    
    # 3. main.js aktualisieren
    update_main_js()
    
    print("\n" + "=" * 60)
    print("✅ Migration abgeschlossen!")
    print(f"📦 Backup gespeichert in: {BACKUP_DIR}")
    print("=" * 60)
    print("\n📋 Nächste Schritte:")
    print("1. Öffne eine HTML-Datei im Browser und teste")
    print("2. Führe Lighthouse-Audit durch")
    print("3. Bei Problemen: Backup wiederherstellen")


if __name__ == "__main__":
    main()
