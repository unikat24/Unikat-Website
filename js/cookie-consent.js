/**
 * Cookie Consent Banner - Unikat Versicherungsmakler
 * Lightweight DSGVO-compliant cookie consent without external dependencies
 */

(function() {
    'use strict';

    const STORAGE_KEY = 'unikat_cookie_consent';
    const ANALYTICS_ID = 'G-JXEPQLWPY4';

    // Check if consent already exists
    function getConsent() {
        try {
            const stored = localStorage.getItem(STORAGE_KEY);
            return stored ? JSON.parse(stored) : null;
        } catch (e) {
            return null;
        }
    }

    // Save consent
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

    // Load Google Analytics
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

    // Create banner HTML
    function createBanner() {
        const banner = document.createElement('div');
        banner.id = 'cookie-consent-banner';
        banner.innerHTML = `
            <div class="cookie-banner-content">
                <div class="cookie-banner-text">
                    <p><strong>Cookies & Datenschutz</strong></p>
                    <p>Wir nutzen Cookies und externe Dienste (Google Analytics, Maps), um unser Angebot zu verbessern. 
                    Weitere Informationen finden Sie in unserer <a href="datenschutz.html">Datenschutzerklärung</a>.</p>
                </div>
                <div class="cookie-banner-buttons">
                    <button id="cookie-accept-all" class="cookie-btn cookie-btn-primary">
                        <i class="fa-solid fa-check"></i> Alle akzeptieren
                    </button>
                    <button id="cookie-accept-necessary" class="cookie-btn cookie-btn-secondary">
                        Nur Notwendige
                    </button>
                </div>
            </div>
        `;
        document.body.appendChild(banner);

        // Add event listeners
        document.getElementById('cookie-accept-all').addEventListener('click', function() {
            saveConsent(true);
            loadAnalytics();
            hideBanner();
        });

        document.getElementById('cookie-accept-necessary').addEventListener('click', function() {
            saveConsent(false);
            hideBanner();
        });
    }

    // Hide banner
    function hideBanner() {
        const banner = document.getElementById('cookie-consent-banner');
        if (banner) {
            banner.style.opacity = '0';
            setTimeout(() => banner.remove(), 300);
        }
    }

    // Show banner
    function showBanner() {
        // Remove existing banner if any
        const existing = document.getElementById('cookie-consent-banner');
        if (existing) existing.remove();

        createBanner();
        
        // Fade in
        setTimeout(() => {
            const banner = document.getElementById('cookie-consent-banner');
            if (banner) banner.style.opacity = '1';
        }, 100);
    }

    // Initialize
    function init() {
        const consent = getConsent();

        if (consent === null) {
            // No consent yet - show banner
            showBanner();
        } else if (consent.analytics) {
            // Analytics accepted - load it
            loadAnalytics();
        }

        // Add event listener for "Cookie-Einstellungen" links
        document.addEventListener('click', function(e) {
            if (e.target.id === 'open-cookie-settings' || 
                e.target.id === 'open-cookie-settings-inline' ||
                e.target.closest('#open-cookie-settings')) {
                e.preventDefault();
                showBanner();
            }
        });
    }

    // Wait for DOM to be ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }

})();
