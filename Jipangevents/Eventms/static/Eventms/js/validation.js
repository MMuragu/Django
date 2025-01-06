document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('#signupForm'); // Replace with your form's ID or class
    form.addEventListener('submit', (event) => {
        let isValid = true;
        const email = document.querySelector('#id_email');
        const phoneNumber = document.querySelector('#id_phone_number');
        const password = document.querySelector('#id_password1');
        const confirmPassword = document.querySelector('#id_password2');
        const errorMessages = [];

        // Validate email
        if (!validateEmail(email.value)) {
            errorMessages.push("Please enter a valid email address.");
            isValid = false;
        }

        // Validate phone number
        if (!/^\d{10,15}$/.test(phoneNumber.value)) {
            errorMessages.push("Phone number must be between 10 and 15 digits and contain only numbers.");
            isValid = false;
        }

        // Validate passwords match
        if (password.value !== confirmPassword.value) {
            errorMessages.push("Passwords do not match.");
            isValid = false;
        }

        // Show error messages
        const errorDiv = document.querySelector('#errorMessages');
        errorDiv.innerHTML = errorMessages.map(msg => `<p>${msg}</p>`).join('');
        errorDiv.style.display = errorMessages.length > 0 ? 'block' : 'none';

        if (!isValid) {
            event.preventDefault(); // Prevent form submission
        }
    });

    function validateEmail(email) {
        const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return regex.test(email);
    }
});
