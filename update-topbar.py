#!/usr/bin/env python3
"""
Script to update the top-bar structure across all HTML files.
Replaces old top-bar with the new optimized version from privat-tiere.html
"""

import os
import re
from pathlib import Path

# Define the new top-bar HTML structure with inline styles
NEW_TOPBAR = '''    <!-- HEADER INLINE (kein JavaScript-Loading mehr) -->
    <div class="top-bar" style="background: white; border-bottom: 1px solid #e2e8f0;">
        <div class="container top-bar-inner" style="display: flex; justify-content: space-between; align-items: center; padding: 10px 20px;">
            
            <div class="top-contact" style="display: flex; gap: 20px; align-items: center;">
                <a href="tel:+493816691930" class="contact-link" aria-label="Telefonnummer anrufen">
                    <i class="fa-solid fa-phone"></i> 0381 669193 0
                </a>

                <a href="https://wa.me/493816691930" class="contact-link whatsapp-link" target="_blank" rel="noopener noreferrer" aria-label="Nachricht per WhatsApp senden">
                    <i class="fa-brands fa-whatsapp"></i> WhatsApp
                </a>
            </div>

            <div class="top-actions" style="display: flex; gap: 15px; align-items: center;">
                <a href="https://outlook.office365.com/owa/calendar/UnikatVersicherungsmaklerGmbH@unikat24.de/bookings/" target="_blank" rel="noopener noreferrer" class="top-link-accent">
                    <i class="fa-regular fa-calendar-check"></i> Termin buchen
                </a>
                
                <a href="schaden.html" class="btn-signal-small">
                    <i class="fa-solid fa-triangle-exclamation"></i> Schaden melden
                </a>
            </div>
        </div>
    </div>'''

def update_topbar_in_file(filepath):
    """Update the top-bar in a single HTML file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Pattern to match the entire top-bar section
        # Matches from <!-- HEADER INLINE --> to </div> (end of top-bar)
        pattern = r'(    <!-- HEADER INLINE.*?-->.*?<div class="top-bar">.*?</div>\s*</div>)'
        
        # Check if the file has a top-bar
        if not re.search(pattern, content, re.DOTALL):
            print(f"⚠️  Keine Top-Bar gefunden in: {filepath.name}")
            return False
        
        # Replace the old top-bar with the new one
        new_content = re.sub(pattern, NEW_TOPBAR, content, flags=re.DOTALL)
        
        # Only write if content changed
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"✅ Aktualisiert: {filepath.name}")
            return True
        else:
            print(f"ℹ️  Bereits aktuell: {filepath.name}")
            return False
            
    except Exception as e:
        print(f"❌ Fehler bei {filepath.name}: {str(e)}")
        return False

def main():
    """Main function to update all HTML files."""
    # Get current directory
    current_dir = Path.cwd()
    
    # Find all HTML files in the root directory
    html_files = list(current_dir.glob('*.html'))
    
    if not html_files:
        print("❌ Keine HTML-Dateien gefunden!")
        return
    
    print(f"🔍 {len(html_files)} HTML-Dateien gefunden\n")
    
    updated_count = 0
    skipped_count = 0
    
    for html_file in sorted(html_files):
        # Skip privat-tiere.html as it's already updated
        if html_file.name == 'privat-tiere.html':
            print(f"⏭️  Übersprungen (Vorlage): {html_file.name}")
            skipped_count += 1
            continue
        
        if update_topbar_in_file(html_file):
            updated_count += 1
        else:
            skipped_count += 1
    
    print(f"\n{'='*50}")
    print(f"✅ Erfolgreich aktualisiert: {updated_count} Dateien")
    print(f"⏭️  Übersprungen: {skipped_count} Dateien")
    print(f"{'='*50}")

if __name__ == "__main__":
    main()
