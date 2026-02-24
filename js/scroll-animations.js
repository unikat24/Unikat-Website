/**
 * ON-SCROLL ANIMATIONS
 * Premium Fade-In-Up Effekt mit IntersectionObserver
 * 
 * Funktionsweise:
 * - Beobachtet alle Elemente mit der Klasse .animate-on-scroll
 * - Fügt .is-visible hinzu, wenn Element zu 10-20% im Viewport ist
 * - Stoppt Beobachtung nach Animation (einmalig)
 */

document.addEventListener('DOMContentLoaded', function() {
    // Alle Elemente mit .animate-on-scroll finden
    const animatedElements = document.querySelectorAll('.animate-on-scroll');
    
    // Prüfen ob Nutzer reduzierte Bewegung bevorzugt
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    
    // Wenn reduzierte Bewegung bevorzugt wird, sofort alle Elemente sichtbar machen
    if (prefersReducedMotion) {
        animatedElements.forEach(el => {
            el.classList.add('is-visible');
        });
        return; // Beende Funktion
    }
    
    // IntersectionObserver Optionen
    const observerOptions = {
        root: null, // Viewport als Root
        rootMargin: '0px',
        threshold: 0.15 // Element wird getriggert wenn 15% sichtbar sind
    };
    
    // Callback-Funktion wenn Element ins Viewport kommt
    const observerCallback = (entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // Element ist sichtbar -> Animation starten
                entry.target.classList.add('is-visible');
                
                // Beobachtung stoppen (Animation nur einmal)
                observer.unobserve(entry.target);
            }
        });
    };
    
    // Observer erstellen
    const observer = new IntersectionObserver(observerCallback, observerOptions);
    
    // Alle Elemente beobachten
    animatedElements.forEach(element => {
        observer.observe(element);
    });
});
