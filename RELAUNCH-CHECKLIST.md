# 🚀 UNIKAT WEBSITE RELAUNCH - CHECKLISTE FÜR IT-DIENSTLEISTER

## 📋 REDIRECT-MAPPING (301 - KRITISCH!)

### Alte Live-URLs → Neue Ziel-URLs

| Alte URL (live) | Neue URL (Ziel) | Status | Notiz |
|----------------|-----------------|--------|-------|
| `/gewerbekunden/` | `/unternehmen.html` | 301 | Hauptseite Gewerbe |
| `/gewerbekunden/immobilienwirtschaft/` | `/unternehmen-immobilien.html` | 301 | |
| `/gewerbekunden/kfz-flotten/` | `/unternehmen-logistik.html` | 301 | Thematisch beste Übereinstimmung |
| `/gewerbekunden/firmen-gewerbe-handel/` | `/unternehmen-mittelstand.html` | 301 | |
| `/gewerbekunden/betriebliche-altersversorgung/` | `/unternehmen-versorgung.html` | 301 | |
| `/gewerbekunden/langzeitarbeitskonten/` | `/unternehmen-versorgung.html` | 301 | Zusammengelegt |
| `/privatkunden/` | `/privat.html` | 301 | Hauptseite Privat |
| `/unternehmen/` | `/ueber-unikat.html` | 301 | Alte "Über uns" Sektion |
| `/unternehmen/historie/` | `/ueber-unikat.html` | 301 | |
| `/unternehmen/wirueberuns/` | `/ueber-unikat.html` | 301 | |
| `/unternehmen/wirueberuns/arbeitsweise/` | `/ueber-unikat.html` | 301 | |
| `/unternehmen/wirueberuns/team/` | `/ueber-unikat.html` | 301 | |
| `/unternehmen/wirueberuns/zertifizierte-qualitaet/` | `/ueber-unikat.html` | 301 | |
| `/schadenmeldung/` | `/schaden.html` | 301 | |
| `/erstinformationen/` | `/erstinformation.html` | 301 | Singular! |
| `/impressum/` | `/impressum.html` | 301 | |
| `/datenschutz/` | `/datenschutz.html` | 301 | |
| `/Wechsel/` | `/unternehmen.html` | 301 | Großschreibung beachten! |
| `/kontakt/` | `/` | 301 | ⚠️ Keine Kontaktseite vorhanden |

### ⚠️ WICHTIG: Redirect-Regeln
- **Case-insensitive**: `/Gewerbekunden/` = `/gewerbekunden/`
- **Trailing Slash**: Mit UND ohne `/` abfangen
- **Keine Redirect-Ketten**: Direkt von alt → neu
- **Nur 301**: Keine 302 oder 307

### 📁 Bereitgestellte Dateien
1. **`_redirects`** → Für Netlify/Vercel/Cloudflare Pages
2. **`.htaccess`** → Für Apache Server
3. **`nginx.conf` Snippet** → Muss noch erstellt werden (siehe unten)

---

## 🔴 KRITISCHE ÄNDERUNGEN VOR GO-LIVE

### 1. ❌ NOINDEX/NOFOLLOW ENTFERNEN
**Aktueller Stand:** Alle HTML-Seiten haben:
```html
<meta name="robots" content="noindex, nofollow">
```

**AKTION:** Diese Zeile in **ALLEN** HTML-Dateien löschen oder ändern zu:
```html
<meta name="robots" content="index, follow">
```

**Betroffene Dateien:**
- index.html
- unternehmen.html
- privat.html
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
- kundenportal.html
- ueber-unikat.html
- schaden.html
- impressum.html
- datenschutz.html
- erstinformation.html

---

### 2. 🔗 CANONICAL URLS PRÜFEN
**Problem:** Aktuell zeigen alle Canonicals auf die Startseite:
```html
<link rel="canonical" href="https://www.unikat-versicherungsmakler.de/">
```

**AKTION:** Jede Seite muss ihren eigenen Canonical haben:
```html
<!-- index.html -->
<link rel="canonical" href="https://www.unikat-versicherungsmakler.de/">

<!-- unternehmen.html -->
<link rel="canonical" href="https://www.unikat-versicherungsmakler.de/unternehmen.html">

<!-- unternehmen-immobilien.html -->
<link rel="canonical" href="https://www.unikat-versicherungsmakler.de/unternehmen-immobilien.html">

<!-- etc. für alle Seiten -->
```

---

### 3. 📄 TITLE & META-DESCRIPTION
**Status:** ✅ Bereits individuell pro Seite vorhanden
**Aktion:** Nochmal prüfen, ob alle Seiten unique Titles haben

---

### 4. 🗺️ SITEMAP.XML
**Status:** ✅ Vorhanden und korrekt
**Aktion:** 
- Nach Go-Live bei Google Search Console einreichen
- URL: `https://www.unikat-versicherungsmakler.de/sitemap.xml`

---

### 5. 🤖 ROBOTS.TXT
**Status:** ✅ Vorhanden
**Aktion:** Prüfen, dass nichts Wichtiges geblockt wird

---

## 🟡 TECHNISCHE SETUP-ANFORDERUNGEN

### SSL/HTTPS
- [ ] SSL-Zertifikat installiert (Let's Encrypt empfohlen)
- [ ] HTTP → HTTPS Redirect (301)
- [ ] HSTS Header aktivieren (optional, aber empfohlen)

### Performance
- [ ] Gzip/Brotli Kompression aktiviert
- [ ] Browser-Caching konfiguriert (Cache-Control Headers)
- [ ] CDN für statische Assets (optional)

### Security Headers
```
X-Frame-Options: SAMEORIGIN
X-Content-Type-Options: nosniff
Referrer-Policy: strict-origin-when-cross-origin
```

---

## 📧 FORMULARE & LEAD-FLOWS

### Aktueller Stand
**Problem:** Formulare sind nur HTML, kein Backend!

### Betroffene Formulare
1. **Kontaktformulare** (falls vorhanden)
2. **Lead-Magnets** (Download-Formulare)
3. **Newsletter-Anmeldung** (falls vorhanden)

### AKTION ERFORDERLICH
- [ ] Backend für Formular-Verarbeitung einrichten
- [ ] E-Mail-Versand konfigurieren (SMTP)
- [ ] Spam-Schutz implementieren (Honeypot bevorzugt, kein reCAPTCHA wegen DSGVO)
- [ ] Danke-Seiten erstellen/verlinken
- [ ] Fehlerbehandlung implementieren

**Empfehlung:** Formspree, Netlify Forms oder eigenes PHP-Script

---

## 🍪 COOKIE-CONSENT & TRACKING

### Aktueller Stand
✅ Cookie-Consent-Banner implementiert (`js/cookie-consent.js`)

### AKTION VOR GO-LIVE
- [ ] Prüfen: Welche Tracking-Tools sollen eingebunden werden?
  - Google Analytics?
  - Google Tag Manager?
  - Matomo (DSGVO-konform)?
- [ ] Tracking-Skripte dürfen **erst nach Consent** laden
- [ ] Cookie-Banner rechtlich prüfen lassen

**Wichtig:** Aktuell lädt kein Tracking-Tool → DSGVO-konform, aber keine Analytics!

---

## 🔍 SEO POST-LAUNCH

### Sofort nach Go-Live
- [ ] Google Search Console einrichten
- [ ] Sitemap einreichen
- [ ] Alle Redirects testen (siehe Testliste unten)
- [ ] Google My Business Profil aktualisieren (neue URL)

### Erste Woche
- [ ] 404-Fehler in Search Console prüfen
- [ ] Indexierung überwachen
- [ ] PageSpeed Insights Test

---

## ✅ REDIRECT-TESTLISTE

Nach Go-Live diese URLs manuell testen:

```
https://www.unikat-versicherungsmakler.de/gewerbekunden/
→ Sollte 301 zu /unternehmen.html

https://www.unikat-versicherungsmakler.de/Gewerbekunden
→ Sollte 301 zu /unternehmen.html (Case-insensitive!)

https://www.unikat-versicherungsmakler.de/gewerbekunden/immobilienwirtschaft/
→ Sollte 301 zu /unternehmen-immobilien.html

https://www.unikat-versicherungsmakler.de/privatkunden/
→ Sollte 301 zu /privat.html

https://www.unikat-versicherungsmakler.de/unternehmen/
→ Sollte 301 zu /ueber-unikat.html

https://www.unikat-versicherungsmakler.de/schadenmeldung
→ Sollte 301 zu /schaden.html

https://www.unikat-versicherungsmakler.de/Wechsel/
→ Sollte 301 zu /unternehmen.html

https://www.unikat-versicherungsmakler.de/kontakt/
→ Sollte 301 zu /
```

**Tool-Empfehlung:** https://httpstatus.io/ oder Browser DevTools (Network Tab)

---

## 🚨 OFFENE PUNKTE / ENTSCHEIDUNGEN NÖTIG

### 1. ⚠️ KONTAKT-SEITE FEHLT
**Problem:** Alte URL `/kontakt/` existiert, neue Seite hat keine dedizierte Kontaktseite

**Optionen:**
- **A)** Kontaktseite erstellen (`kontakt.html`) mit Formular
- **B)** Redirect zu Startseite mit Kontakt-Sektion (`/#kontakt`)
- **C)** Redirect zu `/unternehmen.html` (dort ist Termin-Buchung)

**Empfehlung:** Option A - Dedizierte Kontaktseite erstellen

---

### 2. 📧 FORMULAR-BACKEND
**Status:** Nicht implementiert
**Aktion:** IT-Dienstleister muss entscheiden:
- Netlify Forms?
- Formspree?
- Eigenes PHP-Script?
- WordPress-Integration?

---

### 3. 📊 TRACKING/ANALYTICS
**Status:** Nicht konfiguriert
**Frage:** Welche Tools sollen eingebunden werden?
- Google Analytics 4?
- Matomo (DSGVO-konform, selbst gehostet)?
- Keine Analytics?

---

### 4. 🌐 HOSTING-PLATTFORM
**Frage:** Wo wird die Seite gehostet?
- **Netlify/Vercel:** `_redirects` Datei verwenden
- **Apache:** `.htaccess` verwenden
- **Nginx:** Snippet muss noch erstellt werden (siehe unten)

---

### 5. 🔄 WARTUNG & UPDATES
**Frage:** Wer kümmert sich um:
- Inhaltliche Änderungen?
- Technische Updates?
- Backup-Management?

---

## 📝 NGINX REDIRECT-SNIPPET (Falls Nginx Server)

```nginx
# In nginx.conf oder site-config einfügen

# GEWERBEKUNDEN -> UNTERNEHMEN
rewrite ^/[Gg]ewerbekunden/?$ /unternehmen.html permanent;
rewrite ^/[Gg]ewerbekunden/immobilienwirtschaft/?$ /unternehmen-immobilien.html permanent;
rewrite ^/[Gg]ewerbekunden/kfz-flotten/?$ /unternehmen-logistik.html permanent;
rewrite ^/[Gg]ewerbekunden/firmen-gewerbe-handel/?$ /unternehmen-mittelstand.html permanent;
rewrite ^/[Gg]ewerbekunden/betriebliche-altersversorgung/?$ /unternehmen-versorgung.html permanent;
rewrite ^/[Gg]ewerbekunden/langzeitarbeitskonten/?$ /unternehmen-versorgung.html permanent;

# PRIVATKUNDEN -> PRIVAT
rewrite ^/[Pp]rivatkunden/?$ /privat.html permanent;

# UNTERNEHMEN -> UEBER-UNIKAT
rewrite ^/[Uu]nternehmen/?$ /ueber-unikat.html permanent;
rewrite ^/[Uu]nternehmen/historie/?$ /ueber-unikat.html permanent;
rewrite ^/[Uu]nternehmen/wirueberuns/?$ /ueber-unikat.html permanent;
rewrite ^/[Uu]nternehmen/wirueberuns/arbeitsweise/?$ /ueber-unikat.html permanent;
rewrite ^/[Uu]nternehmen/wirueberuns/team/?$ /ueber-unikat.html permanent;
rewrite ^/[Uu]nternehmen/wirueberuns/zertifizierte-qualitaet/?$ /ueber-unikat.html permanent;

# PFLICHTSEITEN
rewrite ^/[Ss]chadenmeldung/?$ /schaden.html permanent;
rewrite ^/[Ee]rstinformationen/?$ /erstinformation.html permanent;
rewrite ^/[Ii]mpressum/?$ /impressum.html permanent;
rewrite ^/[Dd]atenschutz/?$ /datenschutz.html permanent;

# WECHSEL & KONTAKT
rewrite ^/[Ww]echsel/?$ /unternehmen.html permanent;
rewrite ^/[Kk]ontakt/?$ / permanent;
```

---

## 🎯 ZUSAMMENFASSUNG: WAS MUSS VOR GO-LIVE PASSIEREN?

### ✅ BEREITS ERLEDIGT
- Responsive Design
- Lokale Fonts (DSGVO)
- Cookie-Consent-Banner
- SEO-Grundlagen (Schema.org, Meta-Tags)
- Sitemap.xml
- Redirect-Dateien erstellt

### 🔴 KRITISCH - MUSS VOR GO-LIVE
1. **NOINDEX/NOFOLLOW entfernen** (alle HTML-Dateien)
2. **Canonical URLs korrigieren** (jede Seite eigene URL)
3. **Redirects konfigurieren** (je nach Server: .htaccess, _redirects oder nginx.conf)
4. **SSL-Zertifikat** installieren
5. **Redirect-Tests** durchführen

### 🟡 WICHTIG - SOLLTE VOR GO-LIVE
1. **Formular-Backend** einrichten
2. **Kontakt-Seite** erstellen oder Redirect-Ziel festlegen
3. **Tracking** entscheiden und konfigurieren
4. **Performance-Optimierung** (Gzip, Caching)

### 🟢 NICE-TO-HAVE - KANN NACH GO-LIVE
1. Google Search Console einrichten
2. Google My Business aktualisieren
3. 404-Seite erstellen
4. Monitoring einrichten

---

## 📞 KONTAKT FÜR RÜCKFRAGEN
Bei technischen Fragen zu dieser Checkliste:
→ Entwickler kontaktieren oder IT-Dienstleister

**Letzte Aktualisierung:** 05.03.2026
