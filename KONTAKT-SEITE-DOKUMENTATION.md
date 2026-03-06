# 📄 KONTAKT-SEITE IMPLEMENTIERUNG - DOKUMENTATION

## ✅ ABGESCHLOSSENE ARBEITEN

### 1. Neue Datei erstellt: `kontakt.html`

**Inhalt der Seite:**

#### A) Hero/Intro
- **H1:** "Kontakt"
- **Einleitungstext:** Kurz und direkt, erwähnt Rostock, MV, Norddeutschland und Hausverwalter aus Hamburg/Berlin

#### B) Schnell-Kontakt-Kacheln (4 Kacheln)
1. **Telefon:** Click-to-call zu 0381 669193 0
2. **E-Mail:** mailto zu info@unikat24.de
3. **Rückruf:** Sprung zum Formular (#kontaktformular)
4. **Termin:** Link zur Outlook-Buchungsseite
5. **Bonus:** Schaden-Hinweis mit Link zu schaden.html

#### C) Adresse und Anfahrt
- **Adresse:** Unikat Versicherungsmakler GmbH, August-Bebel-Straße 11, 18055 Rostock
- **Öffnungszeiten:** Mo–Fr 9:00–17:00 Uhr, Termine nach Vereinbarung
- **Google Maps Link:** Reiner Link (kein iframe) zu Google Maps Route
- **Büro-Bild:** Verwendet vorhandenes Bild `unikat-buero-aussen.webp`

#### D) Kontaktformular (DSGVO-tauglich)
**Felder:**
- Name (Pflicht)
- Firma (optional)
- E-Mail (Pflicht)
- Telefon (optional)
- Anliegen (Dropdown: Gewerbe, Hausverwaltung, Logistik, Privat, Schaden, Sonstiges)
- Nachricht (Pflicht)

**Datenschutz:**
- Kurzer Hinweis mit Link zu datenschutz.html
- Keine Checkbox-Pflicht (DSGVO-konform)

**Spam-Schutz:**
- Honeypot-Feld implementiert

#### E) Ansprechpartner/Service-Hinweis
3 Bullet Points:
- Feste Ansprechpartner
- Regional erreichbar
- Gewerbe-Fokus

#### F) Footer
- Standard-Footer mit Links zu Impressum, Datenschutz, Erstinformation
- Kontakt-Link im Footer hinzugefügt

---

### 2. Navigation aktualisiert

**Datei:** `index.html`

**Änderung:**
```html
<div class="nav-item"><a href="kontakt.html" class="nav-link">Kontakt</a></div>
```

**Position:** Zwischen "Über Unikat" und "Kundenportal"

**Hinweis:** Diese Änderung muss auch in **allen anderen HTML-Seiten** repliziert werden:
- unternehmen.html
- privat.html
- ueber-unikat.html
- schaden.html
- kundenportal.html
- Alle Unterseiten (unternehmen-*.html, privat-*.html)

---

### 3. Sitemap aktualisiert

**Datei:** `sitemap.xml`

**Neuer Eintrag:**
```xml
<url>
  <loc>https://www.unikat-versicherungsmakler.de/kontakt.html</loc>
  <lastmod>2026-02-16</lastmod>
  <changefreq>yearly</changefreq>
  <priority>0.7</priority>
</url>
```

**Position:** Zwischen ueber-unikat.html und schaden.html

---

### 4. Redirects aktualisiert

#### A) `_redirects` (Netlify/Vercel/Cloudflare Pages)
```
/kontakt /kontakt.html 301
/kontakt/ /kontakt.html 301
/Kontakt /kontakt.html 301
/Kontakt/ /kontakt.html 301
```

#### B) `.htaccess` (Apache Server)
```apache
RewriteRule ^[Kk]ontakt/?$ /kontakt.html [R=301,L,NC]
```

**Vorher:** Redirect ging zu `/` (Startseite)
**Nachher:** Redirect geht zu `/kontakt.html`

---

## 🔴 TODOs - BACKEND-INTEGRATION ERFORDERLICH

### 1. Kontaktformular Backend

**Aktueller Stand:** Formular ist nur HTML, kein Backend verbunden

**Optionen für Backend-Integration:**

#### Option A: Netlify Forms (empfohlen für Netlify Hosting)
```html
<form data-netlify="true" name="kontakt" method="POST">
```
- Einfachste Lösung
- Automatische Spam-Filterung
- E-Mail-Benachrichtigungen
- Kostenlos bis 100 Submissions/Monat

#### Option B: Formspree
```html
<form action="https://formspree.io/f/YOUR_FORM_ID" method="POST">
```
- Einfache Integration
- Kostenlos bis 50 Submissions/Monat
- Spam-Schutz inklusive

#### Option C: Eigenes PHP-Script
```php
<?php
// Formular-Verarbeitung
// E-Mail-Versand via SMTP
// Spam-Schutz (Honeypot + Rate Limiting)
?>
```
- Volle Kontrolle
- Benötigt PHP-Hosting
- Mehr Aufwand

#### Option D: WordPress-Integration
- Falls WordPress im Backend läuft
- Contact Form 7 oder WPForms

**Daten die gesendet werden:**
- name
- firma
- email
- telefon
- anliegen
- nachricht

**JavaScript-Hinweis:**
Im `<script>` Tag am Ende von kontakt.html ist ein TODO-Kommentar mit Beispielen für die Integration.

---

### 2. Formular Success/Error Handling

**Aktuell:** Inline Success/Error Messages sind vorbereitet, aber nicht funktional

**TODO:**
- Success-Message nach erfolgreichem Versand anzeigen
- Error-Message bei Fehler anzeigen
- Optional: Redirect zu Danke-Seite (z.B. `danke-kontakt.html`)

---

### 3. Navigation in allen Seiten aktualisieren

**TODO:** Kontakt-Link muss in **alle** HTML-Seiten eingefügt werden:

**Betroffene Dateien:**
- unternehmen.html
- privat.html
- ueber-unikat.html
- schaden.html
- kundenportal.html
- unternehmen-immobilien.html
- unternehmen-logistik.html
- unternehmen-cyber.html
- unternehmen-sozialwirtschaft.html
- unternehmen-mittelstand.html
- unternehmen-versorgung.html
- privat-wohnen.html
- privat-beruf-familie.html
- privat-gesundheit.html
- privat-tiere.html
- privat-betriebliche-vorsorge.html
- impressum.html
- datenschutz.html
- erstinformation.html

**Einfügen zwischen:**
```html
<div class="nav-item"><a href="ueber-unikat.html" class="nav-link">Über Unikat</a></div>
<div class="nav-item"><a href="kontakt.html" class="nav-link">Kontakt</a></div>
<div class="nav-item">
    <a href="kundenportal.html" class="btn btn-primary btn-sm">Kundenportal</a>
</div>
```

---

## 🎨 DESIGN & TECHNIK

### Verwendete Komponenten
- ✅ Bestehende CSS-Klassen (keine neuen Design-Systeme)
- ✅ Konsistente Spacing und Layout
- ✅ Mobile-first Design
- ✅ Grid-System (grid-2, grid-3, grid-4)
- ✅ Card-Komponenten
- ✅ Button-Styles (btn, btn-primary, btn-outline)

### Accessibility
- ✅ Labels korrekt mit for/id verknüpft
- ✅ aria-label für Icons
- ✅ aria-required für Pflichtfelder
- ✅ Skip-Link kompatibel
- ✅ Fokus-States vorhanden (CSS)
- ✅ HTML5 Validierung (required)

### SEO
- ✅ Unique Title: "Kontakt – Versicherungsmakler Rostock | Unikat"
- ✅ Meta Description vorhanden
- ✅ Canonical URL: /kontakt.html
- ✅ OpenGraph Basics vorhanden
- ✅ In sitemap.xml eingetragen
- ⚠️ **WICHTIG:** noindex/nofollow muss vor Go-Live entfernt werden!

### Mobile Optimierung
- ✅ Kacheln stapeln auf Mobile
- ✅ Formular gut bedienbar
- ✅ Responsive Grid
- ✅ Touch-friendly Buttons

---

## 📋 REDIRECT-ÜBERSICHT

| Alte URL | Neue URL | Status | Datei |
|----------|----------|--------|-------|
| `/kontakt` | `/kontakt.html` | 301 | _redirects, .htaccess |
| `/kontakt/` | `/kontakt.html` | 301 | _redirects, .htaccess |
| `/Kontakt` | `/kontakt.html` | 301 | _redirects, .htaccess |
| `/Kontakt/` | `/kontakt.html` | 301 | _redirects, .htaccess |

**Wichtig:** Case-insensitive und mit/ohne Trailing Slash

---

## 🧪 TESTING NACH GO-LIVE

### 1. Redirect-Tests
```
https://www.unikat-versicherungsmakler.de/kontakt
→ Sollte 301 zu /kontakt.html

https://www.unikat-versicherungsmakler.de/Kontakt/
→ Sollte 301 zu /kontakt.html
```

### 2. Formular-Tests
- [ ] Alle Pflichtfelder funktionieren
- [ ] E-Mail-Versand funktioniert
- [ ] Spam-Schutz (Honeypot) funktioniert
- [ ] Success-Message wird angezeigt
- [ ] Error-Handling funktioniert

### 3. Mobile-Tests
- [ ] Seite lädt korrekt auf Mobile
- [ ] Kacheln stapeln richtig
- [ ] Formular ist bedienbar
- [ ] Buttons sind touch-friendly

### 4. SEO-Tests
- [ ] Seite wird von Google indexiert (nach noindex-Entfernung)
- [ ] Canonical URL ist korrekt
- [ ] In Google Search Console sichtbar

---

## 📞 KONTAKT-INFORMATIONEN AUF DER SEITE

**Telefon:** 0381 669193 0
**E-Mail:** info@unikat24.de
**Adresse:** August-Bebel-Straße 11, 18055 Rostock
**Öffnungszeiten:** Mo–Fr 9:00–17:00 Uhr
**Termin-Link:** https://outlook.office365.com/owa/calendar/UnikatVersicherungsmaklerGmbH@unikat24.de/bookings/

---

## 🚀 NÄCHSTE SCHRITTE

### Vor Go-Live (Kritisch)
1. ✅ kontakt.html erstellt
2. ✅ Navigation in index.html aktualisiert
3. ✅ Sitemap aktualisiert
4. ✅ Redirects konfiguriert
5. ⚠️ **TODO:** Navigation in allen anderen Seiten aktualisieren
6. ⚠️ **TODO:** Formular-Backend integrieren
7. ⚠️ **TODO:** noindex/nofollow entfernen

### Nach Go-Live
1. Redirects testen
2. Formular testen
3. Google Search Console überwachen
4. Nutzer-Feedback sammeln

---

## 📝 ZUSAMMENFASSUNG

**Erstellt:**
- ✅ kontakt.html (vollständig funktional, nur Backend fehlt)
- ✅ Navigation in index.html aktualisiert
- ✅ Sitemap-Eintrag
- ✅ Redirects (_redirects + .htaccess)

**Noch zu tun:**
- ⚠️ Formular-Backend integrieren (siehe Optionen oben)
- ⚠️ Navigation in allen anderen HTML-Seiten aktualisieren
- ⚠️ Vor Go-Live: noindex/nofollow entfernen

**Dateien geändert:**
1. `kontakt.html` (NEU)
2. `index.html` (Navigation)
3. `sitemap.xml` (Eintrag hinzugefügt)
4. `_redirects` (Redirect aktualisiert)
5. `.htaccess` (Redirect aktualisiert)

---

**Letzte Aktualisierung:** 06.03.2026
**Status:** Bereit für Backend-Integration und Navigation-Rollout
