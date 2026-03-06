# DATENSCHUTZ-TEXTBAUSTEINE für datenschutz.html

**Erstellt:** 2026-03-06  
**Basis:** DATENSCHUTZ-FAKTEN.md

---

## BLOCK 1: Hosting & Server-Logfiles
**Ersetze Abschnitt:** "Erfassung allgemeiner Informationen"

```html
<h2>Hosting & Server-Logfiles</h2>
<p>Diese Website wird bei [Hosting-Anbieter] gehostet. Die Server befinden sich in [Serverstandort EU]. Mit dem Hosting-Anbieter besteht ein Auftragsverarbeitungsvertrag (AVV) gemäß Art. 28 DSGVO.</p>

<p>Beim Besuch unserer Website werden automatisch folgende Informationen in Server-Logfiles erfasst:</p>
<ul>
    <li>IP-Adresse des anfragenden Rechners</li>
    <li>Datum und Uhrzeit des Zugriffs</li>
    <li>Name und URL der abgerufenen Datei</li>
    <li>Website, von der aus der Zugriff erfolgt (Referrer-URL)</li>
    <li>Verwendeter Browser und ggf. das Betriebssystem Ihres Rechners</li>
</ul>

<p><strong>Zweck:</strong> Technische Bereitstellung der Website, Systemsicherheit und Fehleranalyse.<br>
<strong>Rechtsgrundlage:</strong> Art. 6 Abs. 1 lit. f DSGVO (berechtigtes Interesse an sicherer und funktionsfähiger Website).<br>
<strong>Speicherdauer:</strong> 14 Tage, danach automatische Löschung (außer bei sicherheitsrelevanten Vorfällen).</p>
```

---

## BLOCK 2: Cookie-Consent & Eigene Lösung
**Ersetze Abschnitt:** "Cookies und Analyse (Google Analytics)" - Teil 1

```html
<h2>Cookie-Consent & Einwilligung</h2>
<p>Beim ersten Besuch unserer Website erscheint ein Cookie-Banner. Sie können wählen, ob Sie alle Cookies akzeptieren oder nur technisch notwendige Cookies zulassen möchten.</p>

<p><strong>Speicherung Ihrer Entscheidung:</strong> Ihre Consent-Entscheidung wird lokal in Ihrem Browser gespeichert (localStorage, Key: <code>unikat_cookie_consent</code>). Diese Speicherung enthält Ihre Wahl (Analytics ja/nein) und einen Zeitstempel.</p>

<p><strong>Widerruf:</strong> Sie können Ihre Einwilligung jederzeit ändern oder widerrufen. Klicken Sie dazu auf den Link "Cookie-Einstellungen" im Footer unserer Website oder <a href="#" id="open-cookie-settings-inline">hier</a>.</p>

<p><strong>Rechtsgrundlage:</strong> Art. 6 Abs. 1 lit. f DSGVO (technisch notwendige Speicherung der Consent-Entscheidung).</p>
```

---

## BLOCK 3: Google Analytics (GA4)
**Ersetze Abschnitt:** "Cookies und Analyse (Google Analytics)" - Teil 2

```html
<h2>Google Analytics (GA4)</h2>
<p>Wir nutzen Google Analytics, einen Webanalysedienst der Google Ireland Limited, Gordon House, Barrow Street, Dublin 4, Irland ("Google").</p>

<p><strong>Zweck:</strong> Analyse der Website-Nutzung zur Optimierung unseres Angebots (z.B. welche Seiten werden besucht, wie lange bleiben Nutzer, woher kommen sie).</p>

<p><strong>Erfasste Daten:</strong> Aufgerufene Seiten, Verweildauer, Herkunftsquelle (Referrer), ungefährer Standort (Land/Region), technische Informationen (Browser, Betriebssystem, Bildschirmauflösung), pseudonyme Nutzer-ID.</p>

<p><strong>IP-Anonymisierung:</strong> Die IP-Adresse wird gekürzt, bevor sie gespeichert wird (IP-Anonymisierung aktiv).</p>

<p><strong>Cookies:</strong> Google Analytics setzt folgende Cookies:
<ul>
    <li><code>_ga</code> – Nutzer-ID (Lebensdauer: 2 Jahre)</li>
    <li><code>_ga_G-JXEPQLWPY4</code> – Session-Daten (Lebensdauer: 2 Jahre)</li>
    <li><code>_gid</code> – Nutzer-ID (Lebensdauer: 24 Stunden)</li>
</ul>
</p>

<p><strong>Rechtsgrundlage:</strong> Art. 6 Abs. 1 lit. a DSGVO (Einwilligung über Cookie-Banner).</p>

<p><strong>Drittlandtransfer:</strong> Google verarbeitet Daten auch in den USA. Die Übermittlung erfolgt auf Basis von Standardvertragsklauseln der EU-Kommission.</p>

<p><strong>Speicherdauer:</strong> [MISSING INFO: Bitte bestätigen, ob 14 Monate konfiguriert sind]. Nutzerbezogene Daten werden nach dieser Frist automatisch gelöscht.</p>

<p><strong>Widerspruch/Opt-out:</strong>
<ul>
    <li>Über unsere <a href="#" id="open-cookie-settings-inline2">Cookie-Einstellungen</a></li>
    <li>Browser-Add-on: <a href="https://tools.google.com/dlpage/gaoptout" target="_blank" rel="noopener noreferrer">Google Analytics Opt-out Browser Add-on</a></li>
</ul>
</p>

<p><strong>Weitere Informationen:</strong> <a href="https://policies.google.com/privacy" target="_blank" rel="noopener noreferrer">Datenschutzerklärung von Google</a></p>
```

---

## BLOCK 4: Formspree (Kontaktformulare)
**Neu einfügen nach:** "Google Analytics"

```html
<h2>Kontaktformulare (Formspree)</h2>
<p>Auf unserer Website nutzen wir Kontaktformulare zur Bearbeitung von Anfragen. Die Übermittlung erfolgt über den Dienst Formspree, Inc., USA.</p>

<p><strong>Zweck:</strong> Entgegennahme und Bearbeitung Ihrer Anfragen (z.B. Beratungsanfragen, Terminwünsche, Schadensmeldungen).</p>

<p><strong>Erfasste Daten:</strong>
<ul>
    <li>Pflichtfelder: Name, E-Mail-Adresse, Anliegen/Nachricht</li>
    <li>Optional: Firma, Telefonnummer, weitere Angaben je nach Formular</li>
    <li>Technische Metadaten: IP-Adresse, Zeitstempel (durch Formspree erfasst)</li>
    <li>Tracking-Felder: Seite (z.B. "kontakt.html"), Quelle ("website")</li>
</ul>
</p>

<p><strong>Spam-Schutz:</strong> Wir nutzen ein Honeypot-Feld (unsichtbar für echte Nutzer), um automatisierte Spam-Anfragen zu verhindern. Es werden keine Daten an Dritte übertragen.</p>

<p><strong>Rechtsgrundlage:</strong> Art. 6 Abs. 1 lit. b DSGVO (Durchführung vorvertraglicher Maßnahmen auf Ihre Anfrage) und lit. f DSGVO (berechtigtes Interesse an effizienter Anfragebearbeitung).</p>

<p><strong>Drittlandtransfer:</strong> Formspree verarbeitet Daten in den USA. Die Übermittlung erfolgt auf Basis von Standardvertragsklauseln.</p>

<p><strong>Speicherdauer:</strong> [MISSING INFO: Interne Aufbewahrungsfristen klären]. Ihre Daten werden bei Formspree gespeichert, bis der Zweck erfüllt ist (Bearbeitung Ihrer Anfrage). Intern speichern wir Ihre Daten gemäß unseren Aufbewahrungspflichten (z.B. steuerrechtliche Aufbewahrungsfristen bei Vertragsabschluss).</p>

<p><strong>Weitere Informationen:</strong> <a href="https://formspree.io/legal/privacy-policy/" target="_blank" rel="noopener noreferrer">Datenschutzerklärung von Formspree</a></p>
```

---

## BLOCK 5: Externe Links (keine Einbindung)
**Ersetze Abschnitt:** "Externe Dienste & Tools"

```html
<h2>Externe Links</h2>
<p>Unsere Website enthält Links zu externen Websites und Diensten. Beim Anklicken dieser Links verlassen Sie unsere Website. Wir haben keinen Einfluss auf die Datenverarbeitung durch diese Anbieter.</p>

<p><strong>Folgende externe Dienste sind verlinkt (keine Einbindung/Embeds):</strong></p>

<h3>Google Maps</h3>
<p>Link zur Routenplanung zu unserem Büro. Es werden keine Daten an Google übertragen, solange Sie den Link nicht anklicken.</p>

<h3>Microsoft Outlook Bookings</h3>
<p>Link zur Online-Terminbuchung. Es werden keine Daten an Microsoft übertragen, solange Sie den Link nicht anklicken.</p>

<h3>WhatsApp</h3>
<p>Link zum Öffnen eines WhatsApp-Chats (wa.me). Es werden keine Daten an WhatsApp übertragen, solange Sie den Link nicht anklicken.</p>

<h3>Social Media (LinkedIn, Facebook, Google)</h3>
<p>Links zu unseren Social-Media-Profilen und Google-Bewertungen. Es werden keine Social-Media-Plugins oder Tracking-Pixel eingebunden. Daten werden erst übertragen, wenn Sie die Links anklicken.</p>

<h3>Vergleichsrechner (VEMA, Nafi, Thinksurance)</h3>
<p>Links zu externen Vergleichsrechnern unserer Partner. Es werden keine Daten übertragen, solange Sie die Links nicht anklicken.</p>

<p><strong>Hinweis:</strong> Nach dem Anklicken gelten die Datenschutzbestimmungen des jeweiligen Anbieters.</p>
```

---

## BLOCK 6: Social Media Profile (optional, falls betrieben)
**Neu einfügen nach:** "Externe Links" (nur wenn ihr aktiv Social Media betreibt)

```html
<h2>Social Media Profile</h2>
<p>Wir betreiben Profile auf LinkedIn und Facebook. Wenn Sie unsere Profile besuchen, werden Daten durch die Plattformbetreiber verarbeitet (z.B. für Werbung, Tracking, Statistiken).</p>

<p><strong>Insights/Statistiken:</strong> Für die Auswertung von Statistiken (z.B. Reichweite, Interaktionen) sind wir mit Meta (Facebook) bzw. LinkedIn gemeinsam verantwortlich (Art. 26 DSGVO). Details finden Sie in den Datenschutzerklärungen der Plattformen:
<ul>
    <li><a href="https://www.facebook.com/privacy/policy/" target="_blank" rel="noopener noreferrer">Facebook Datenschutz</a></li>
    <li><a href="https://www.linkedin.com/legal/privacy-policy" target="_blank" rel="noopener noreferrer">LinkedIn Datenschutz</a></li>
</ul>
</p>

<p><strong>Rechtsgrundlage:</strong> Art. 6 Abs. 1 lit. f DSGVO (berechtigtes Interesse an Öffentlichkeitsarbeit und Kundenkommunikation).</p>
```

---

## BLOCK 7: Empfänger (anpassen)
**Ersetze Abschnitt:** "Empfänger Ihrer Daten"

```html
<h2>Empfänger Ihrer Daten</h2>
<p>Im Rahmen unserer Maklertätigkeit und zur Erfüllung unserer vertraglichen Pflichten geben wir Ihre Daten an folgende Empfänger weiter:</p>

<ul>
    <li><strong>Versicherungsgesellschaften & Rückversicherer:</strong> Zur Angebotserstellung, Vertragsabschluss und Schadenbearbeitung</li>
    <li><strong>Vergleichsplattformen:</strong> VEMA, Softfair, Nafi (zur Tarifierung und Vergleichsberechnung)</li>
    <li><strong>IT-Dienstleister:</strong> Hosting-Anbieter, E-Mail-Provider (Microsoft 365), Formspree (Kontaktformulare)</li>
    <li><strong>Schadenregulierer & Gutachter:</strong> Bei Schadenfällen zur Regulierung</li>
</ul>

<p>Die Weitergabe erfolgt nur zur Vertragserfüllung (Art. 6 Abs. 1 lit. b DSGVO) oder mit Ihrer Einwilligung (Art. 6 Abs. 1 lit. a DSGVO).</p>
```

---

## BLOCK 8: Betroffenenrechte (unverändert lassen)
**Keine Änderung nötig** - Abschnitt "Ihre Rechte" kann so bleiben.

---

## MISSING INFO - Vor Go-Live klären:

1. **Hosting-Anbieter:** Finaler Anbieter + Serverstandort (EU) + AVV-Bestätigung
2. **Google Analytics Speicherdauer:** Bestätigen, ob 14 Monate konfiguriert sind
3. **Formspree Speicherdauer:** Interne Aufbewahrungsfristen für Anfragen festlegen
4. **Social Media Insights:** Bestätigen, ob ihr aktiv Insights nutzt (dann Block 6 einfügen, sonst weglassen)
5. **Datenschutzbeauftragter:** Prüfen, ob Klaus Patzelt offiziell bestellt ist (wenn ja: so lassen, wenn nein: als "Ansprechpartner für Datenschutzfragen" bezeichnen)
6. **Server-Logs IP-Anonymisierung:** Prüfen, ob IP-Adressen tatsächlich anonymisiert werden (wenn ja: ergänzen, wenn nein: streichen)
7. **Cookie-Banner Text:** Prüfen, ob Text im Banner mit Datenschutz übereinstimmt
8. **Formspree AVV:** Prüfen, ob Auftragsverarbeitungsvertrag mit Formspree besteht
9. **Microsoft 365:** Prüfen, ob AVV vorhanden und ob Daten in EU bleiben
10. **Aufsichtsbehörde:** Kontaktdaten aktuell? (Landesbeauftragter MV)

---

**Ende der Textbausteine**
