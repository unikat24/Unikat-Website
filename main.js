/* DATEI: main.js */

async function loadComponent(elementId, filePath) {
    const element = document.getElementById(elementId);
    if (!element) return;

    try {
        const response = await fetch(filePath);
        if (response.ok) {
            element.innerHTML = await response.text();
            
            // Wenn der Header geladen wurde, initialisiere Menü & Active-State
            if (elementId === 'header-placeholder') {
                initNavigation(); // Mobile/Tablet Logik
                setActiveLink();  // WICHTIG: Markiert den aktuellen Menüpunkt
            }
        }
    } catch (error) {
        console.error(`Fehler beim Laden von ${filePath}:`, error);
    }
}

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
        // Wir nehmen das Eltern-Element (<a>) und dessen Eltern-Element (<li>/.nav-item)
        const parentLink = trigger.parentElement;
        
        parentLink.addEventListener('click', (e) => {
            // Nur auf Mobile/Tablet (<= 1024px) verhindern wir den Link-Sprung
            if (window.innerWidth <= 1024) {
                e.preventDefault();
                const navItem = parentLink.parentElement;
                navItem.classList.toggle('open');
            }
        });
    });
}

function setActiveLink() {
    // Holt den aktuellen Dateinamen aus der URL (z.B. "privat.html")
    // Fallback auf "index.html", wenn Pfad leer ist (z.B. bei Domain-Aufruf)
    const currentPath = window.location.pathname.split('/').pop() || 'index.html';
    
    const links = document.querySelectorAll('.nav-link, .dropdown-link');
    
    links.forEach(link => {
        const href = link.getAttribute('href');
        
        // Wenn der Link zur aktuellen Seite passt
        if (href === currentPath) {
            link.classList.add('active'); // CSS sorgt dann für die Unterstreichung/Farbe
            
            // Falls es ein Untermenü-Link ist (z.B. Logistik), 
            // markiere auch den Hauptpunkt "Unternehmen" als aktiv
            if (link.classList.contains('dropdown-link')) {
                const parentNav = link.closest('.nav-item').querySelector('.nav-link');
                if (parentNav) parentNav.classList.add('active');
            }
        }
    });
}

// Startet das Laden, sobald das DOM bereit ist
document.addEventListener("DOMContentLoaded", () => {
    loadComponent('header-placeholder', 'header.html');
    loadComponent('footer-placeholder', 'footer.html');
});