# DATENSCHUTZ-FAKTENPAKET - Unikat Website

**Erstellt:** 2026-03-06  
**Basis:** Technische Analyse aller HTML/JS/CSS Dateien

---

## OUTPUT 1: DRITTANBIETER/EXTERNE DOMAINS

| Seite | Element | Vollständige URL | Domain | Art | Geladen/Verlinkt |
|-------|---------|------------------|--------|-----|------------------|
| Alle Seiten | Link | `https://wa.me/493816691930` | wa.me | a (Link) | Nur verlinkt |
| Alle Seiten | Link | `https://outlook.office365.com/owa/calendar/UnikatVersicherungsmaklerGmbH@unikat24.de/bookings/` | outlook.office365.com | a (Link) | Nur verlinkt |
| Alle Seiten | Link | `https://www.linkedin.com/company/unikat-versicherungsmakler-gmbh/` | linkedin.com | a (Link) | Nur verlinkt |
| Alle Seiten | Link | `https://www.facebook.com/unikatversicherungsmaklergmbh/` | facebook.com | a (Link) | Nur verlinkt |
| Alle Seiten | Link | `https://share.google/hpFKiHGfPf8xHQE2K` | share.google | a (Link) | Nur verlinkt |
| Alle Seiten | Script | `https://www.googletagmanager.com/gtag/js?id=G-JXEPQLWPY4` | googletagmanager.com | script | Geladen (nach Consent) |
| kontakt.html | Form | `https://formspree.io/f/mjgavvwa` | formspree.io | form action | Nur bei Submit |
| kontakt.html | Link | `https://www.google.com/maps?q=August-Bebel-Straße+11,+18055+Rostock` | google.com | a (Link) | Nur verlinkt |
| unternehmen-logistik.html | Form | `https://formspree.io/f/xykdklwz` | formspree.io | form action | Nur bei Submit |
| unternehmen-immobilien.html | Form | `https://formspree.io/f/mnjbpaar` | formspree.io | form action | Nur bei Submit |
| unternehmen-immobilien.html | Form | `https://formspree.io/f/xykdklwz` | formspree.io | form action | Nur bei Submit |
| unternehmen-cyber.html | Form | `https://formspree.io/f/xykdklwz` | formspree.io | form action | Nur bei Submit |
| unternehmen-mittelstand.html | Form | `https://formspree.io/f/xykdklwz` | formspree.io | form action | Nur bei Submit |
| unternehmen-sozialwirtschaft.html | Form | `https://formspree.io/f/xykdklwz` | formspree.io | form action | Nur bei Submit |
| privat.html | Form | `https://formspree.io/f/xykgzala` | formspree.io | form action | Nur bei Submit |
| Footer (alle Seiten) | Link | `https://apps.nafi.de/NOVA/login/nafi_ndo_1021141198_20210112145536/V3N0eqh6J` | apps.nafi.de | a (Link) | Nur verlinkt |
| Footer (alle Seiten) | Link | `https://ts.thinksurance.de/p/151f048b5b35cb35` | ts.thinksurance.de | a (Link) | Nur verlinkt |
| Footer (alle Seiten) | Link | `https://www.vema-eg.de` | vema-eg.de | a (Link) | Nur verlinkt |

**WICHTIG:** Backup-Ordner enthält alte Versionen mit Cloudflare CDN und Google Fonts - diese sind NICHT aktiv!

---

## OUTPUT 2: TRACKING/ANALYTICS

### Google Analytics Implementation

**Datei:** `js/cookie-consent.js`  
**Zeilen:** 6, 35-48

```javascript
// Zeile 6:
const ANALYTICS_ID = 'G-JXEPQLWPY4';

// Zeilen 35-48:
function loadAnalytics() {
    if (typeof gtag !== 'undefined') return; // Already loaded

    // Create script tag
    const script = document.createElement('script');
    script.async = true;
    script.src = `https://www.googletagmanager.com/gtag/js?id=${ANALYTICS_ID}`;
    document.head.appendChild(script);

    // Initialize gtag
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    window.gtag = gtag;
    gtag('js', new Date());
    gtag('config', ANALYTICS_ID, {
        'anonymize_ip': true,
        'cookie_flags': 'SameSite=None;Secure'
    });
}
```

### Consent-Mechanismus

**Datei:** `js/cookie-consent.js`  
**Zeilen:** 115-125

```javascript
function init() {
    const consent = getConsent();

    if (consent === null) {
        // No consent yet - show banner
        showBanner();
    } else if (consent.analytics) {
        // Analytics accepted - load it
        loadAnalytics();
    }
    // ...
}
```

**BEWEIS:** Google Analytics wird **NUR nach Consent** geladen (Zeile 122: `else if (consent.analytics)`).

### Google Analytics Cookies

| Cookie Name | Gesetzt durch | Zweck | Lebensdauer |
|-------------|---------------|-------|-------------|
| `_ga` | Google Analytics | User-ID | 2 Jahre |
| `_ga_<container-id>` | Google Analytics | Session-Daten | 2 Jahre |
| `_gid` | Google Analytics | User-ID | 24 Stunden |

**Konfiguration:** IP-Anonymisierung aktiv (`anonymize_ip: true`)

---

## OUTPUT 3: COOKIE/STORAGE INVENTAR

### Cookies

| Name | Zweck | Gesetzt durch | Lebensdauer |
|------|-------|---------------|-------------|
| `_ga` | Google Analytics User-ID | Google Analytics (nach Consent) | 2 Jahre |
| `_ga_G-JXEPQLWPY4` | Google Analytics Session | Google Analytics (nach Consent) | 2 Jahre |
| `_gid` | Google Analytics User-ID | Google Analytics (nach Consent) | 24 Stunden |

**KEINE weiteren Cookies** werden von der Website selbst gesetzt.

### LocalStorage

| Key | Wert-Struktur | Zweck | Gesetzt durch |
|-----|---------------|-------|---------------|
| `unikat_cookie_consent` | `{"analytics": true/false, "timestamp": "ISO-Date"}` | Speichert Cookie-Consent-Entscheidung | cookie-consent.js |

**Datei:** `js/cookie-consent.js`  
**Zeilen:** 5, 18-26

```javascript
// Zeile 5:
const STORAGE_KEY = 'unikat_cookie_consent';

// Zeilen 18-26:
function saveConsent(analytics) {
    const consent = {
        analytics: analytics,
        timestamp: new Date().toISOString()
    };
    try {
        localStorage.setItem(STORAGE_KEY, JSON.stringify(consent));
    } catch (e) {
        console.error('Could not save consent:', e);
    }
}
```

### SessionStorage

**KEINE** sessionStorage-Nutzung gefunden.

---

## OUTPUT 4: FORMULARE

### Formspree Endpoints

| Seite | Form-ID | Endpoint | Felder (name=) |
|-------|---------|----------|----------------|
| kontakt.html | `contact-form` | `https://formspree.io/f/mjgavvwa` | `_gotcha`, `_subject`, `page`, `source`, `name`, `firma`, `email`, `telefon`, `anliegen`, `nachricht` |
| unternehmen-logistik.html | `logistik-form` | `https://formspree.io/f/xykdklwz` | `_gotcha`, `_subject`, `firma`, `name`, `email`, `telefon`, `datenschutz` |
| unternehmen-logistik.html | `logistik-audit-form` | `https://formspree.io/f/xykdklwz` | `_gotcha`, `_subject`, `firma`, `name`, `email`, `telefon`, `fuhrpark`, `anliegen`, `datenschutz` |
| unternehmen-immobilien.html | `hausverwaltung-form` | `https://formspree.io/f/mnjbpaar` | `_gotcha`, `_subject`, `firma`, `name`, `email`, `telefon`, `datenschutz` |
| unternehmen-immobilien.html | `immo-form` | `https://formspree.io/f/xykdklwz` | `_gotcha`, `_subject`, `firma`, `name`, `email`, `telefon`, `objekte`, `anliegen`, `datenschutz` |
| unternehmen-cyber.html | `cyber-form` | `https://formspree.io/f/xykdklwz` | `_gotcha`, `_subject`, `firma`, `name`, `email`, `telefon`, `anliegen`, `datenschutz` |
| unternehmen-mittelstand.html | `mittelstand-form` | `https://formspree.io/f/xykdklwz` | `_gotcha`, `_subject`, `firma`, `name`, `email`, `telefon`, `anliegen`, `datenschutz` |
| unternehmen-sozialwirtschaft.html | `sozial-form` | `https://formspree.io/f/xykdklwz` | `_gotcha`, `_subject`, `firma`, `name`, `email`, `telefon`, `anliegen`, `datenschutz` |
| privat.html | (kein ID) | `https://formspree.io/f/xykgzala` | Felder nicht im aktuellen Code sichtbar |

### Honeypot-Felder

**Alle Formulare** nutzen `_gotcha` als Honeypot-Feld (Spam-Schutz).

### Hidden Fields

- `_subject`: E-Mail-Betreff für Formspree
- `page`: Tracking welche Seite (nur kontakt.html)
- `source`: Tracking-Quelle "website" (nur kontakt.html)

---

## OUTPUT 5: KARTEN/TERMINE/MESSENGER/SOCIAL

### Google Maps

| Seite | URL | Art | Embed? |
|-------|-----|-----|--------|
| kontakt.html | `https://www.google.com/maps?q=August-Bebel-Straße+11,+18055+Rostock` | Link (a href) | **NEIN** - nur Link |

**BEWEIS:** Zeile in kontakt.html:
```html
<a href="https://www.google.com/maps?q=August-Bebel-Straße+11,+18055+Rostock" target="_blank" rel="noopener noreferrer" class="btn btn-outline">
    <i class="fa-solid fa-route"></i> Route planen (Google Maps)
</a>
```

**KEIN** iframe, **KEIN** Embed, **KEINE** Google Maps API.

### Microsoft Outlook Bookings

| Seite | URL | Art | Embed? |
|-------|-----|-----|--------|
| Alle Seiten | `https://outlook.office365.com/owa/calendar/UnikatVersicherungsmaklerGmbH@unikat24.de/bookings/` | Link (a href) | **NEIN** - nur Link |

**BEWEIS:** Beispiel aus index.html:
```html
<a href="https://outlook.office365.com/owa/calendar/UnikatVersicherungsmaklerGmbH@unikat24.de/bookings/" target="_blank" rel="noopener noreferrer" class="btn btn-primary btn-hero">
    <i class="fa-solid fa-briefcase"></i> Erstgespräch buchen
</a>
```

**KEIN** iframe, **KEIN** Embed.

### WhatsApp

| Seite | URL | Art | Embed? |
|-------|-----|-----|--------|
| Alle Seiten | `https://wa.me/493816691930` | Link (a href) | **NEIN** - nur Link |

**BEWEIS:** Beispiel aus index.html:
```html
<a href="https://wa.me/493816691930" class="contact-link whatsapp-link" target="_blank" rel="noopener noreferrer">
    <i class="fa-brands fa-whatsapp"></i> WhatsApp
</a>
```

**KEIN** WhatsApp Widget, **KEIN** Embed.

### Social Media Links

| Platform | URL | Art | Embed? |
|----------|-----|-----|--------|
| LinkedIn | `https://www.linkedin.com/company/unikat-versicherungsmakler-gmbh/` | Link (a href) | **NEIN** - nur Link |
| Facebook | `https://www.facebook.com/unikatversicherungsmaklergmbh/` | Link (a href) | **NEIN** - nur Link |
| Google Reviews | `https://share.google/hpFKiHGfPf8xHQE2K` | Link (a href) | **NEIN** - nur Link |

**BEWEIS:** Beispiel aus Footer:
```html
<a href="https://www.linkedin.com/company/unikat-versicherungsmakler-gmbh/" target="_blank" rel="noopener noreferrer" aria-label="LinkedIn">
    <i class="fa-brands fa-linkedin"></i>
</a>
```

**KEINE** Social Media Plugins, **KEINE** Like-Buttons, **KEINE** Embeds.

---

## ZUSAMMENFASSUNG

### Was wird GELADEN (Datenübertragung):
1. ✅ Google Analytics (nur nach Consent)
2. ✅ Formspree (nur bei Formular-Submit)

### Was wird NUR VERLINKT (keine automatische Datenübertragung):
1. ✅ WhatsApp (wa.me)
2. ✅ Outlook Bookings
3. ✅ Google Maps
4. ✅ LinkedIn, Facebook, Google Reviews
5. ✅ VEMA, Nafi, Thinksurance Rechner

### Was wird NICHT genutzt:
- ❌ YouTube
- ❌ reCAPTCHA
- ❌ Cloudflare CDN
- ❌ Google Fonts (lokal gehostet)
- ❌ Bing Maps
- ❌ Facebook Pixel
- ❌ LinkedIn Insight Tag

### Lokale Assets (DSGVO-konform):
- ✅ Fonts (lokal in /fonts/)
- ✅ FontAwesome (lokal in /css/fontawesome.css)
- ✅ Bilder (lokal in /img/)
- ✅ CSS (lokal in styles.css)
- ✅ JavaScript (lokal in /js/)

---

**Ende des Faktenpakets**
