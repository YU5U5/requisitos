document.getElementById('register-form').addEventListener('submit', async function(event) {
    event.preventDefault();  // Previene que el formulario se envíe de manera convencional

    // Obtén los valores del formulario
    const username = document.getElementById('username').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirmPassword').value;

    // Verifica que las contraseñas coinciden
    if (password !== confirmPassword) {
        alert('Las contraseñas no coinciden.');
        return;
    }

    // Crea el objeto con los datos que enviarás al backend
    const data = {
        username: username,
        email: email,
        password: password
    };

    try {
        // Envía la solicitud POST al backend (con la nueva ruta '/registro')
        const response = await fetch('http://127.0.0.1:8000/registro/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)  // Convierte el objeto a JSON
        });

        const responseData = await response.json();  // Convierte la respuesta a JSON

        if (response.ok) {
            console.log('Registro exitoso:', responseData);
            alert('¡Registro exitoso!');
            // Aquí puedes redirigir o hacer cualquier otra acción después del registro exitoso
        } else {
            console.error('Error en el registro:', responseData);
            alert('Hubo un error en el registro.');
        }
    } catch (error) {
        console.error('Error en la solicitud:', error);

        // Verifica si el error es un problema de red o de respuesta del servidor
        if (error.message.includes('Failed to fetch')) {
            alert('No se pudo conectar al servidor. Verifica tu conexión a Internet.');
        } else {
            alert('Hubo un problema con la conexión o el servidor.');
        }
    }
});