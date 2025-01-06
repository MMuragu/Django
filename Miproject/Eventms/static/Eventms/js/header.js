const menuToggle = document.querySelector('.menu-toggle');
const navMenu = document.querySelector('nav ul');

menuToggle.addEventListener('click', function () {
    navMenu.classList.toggle('show');

    // Change button text dynamically
    if (navMenu.classList.contains('show')) {
        menuToggle.textContent = '✕'; // Close icon
    } else {
        menuToggle.textContent = '☰'; // Hamburger icon
    }
});
