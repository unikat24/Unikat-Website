/* DATEI: main.js - Nur Mobile Navigation (Header/Footer sind jetzt inline) */

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
