document.querySelectorAll('.toggle-password').forEach(icon => { // recorre todos los íconos.
    icon.addEventListener('click', function () {
        const passwordFields = document.querySelectorAll('.password-field'); // Selecciona ambos campos de contraseña

        passwordFields.forEach(input => { //recorre cada campo de contraseña.
            if (input.type === "password") {
                input.type = "text"; // Muestra la contraseña
            } else {
                input.type = "password"; // Oculta la contraseña
            }
        });

        // Alternar el icono de todos los botones
        document.querySelectorAll('.toggle-password').forEach(btn => {
            btn.classList.toggle("fa-eye");
            btn.classList.toggle("fa-eye-slash");
        });
    });
});