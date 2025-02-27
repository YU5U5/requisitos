// Función para mostrar/ocultar el formulario de búsqueda
function toggleSearch() {
    const searchContainer = document.getElementById('searchContainer');
    if (searchContainer.style.display === 'none' || searchContainer.style.display === '') {
        searchContainer.style.display = 'block';
    } else {
        searchContainer.style.display = 'none';
    }
}

// Función para mostrar la sección del carrito
function viewCart() {
    alert('Ver carrito de compras');
}

// Función para mostrar la sección de perfil
function viewProfile() {
    alert('Ver perfil de usuario');
}

// Función para filtrar los productos por el nombre al escribir en el campo de búsqueda
function searchProduct() {
    const query = document.getElementById('searchInput').value.toLowerCase();
    const products = document.querySelectorAll('.product-card');

    products.forEach(product => {
        const productName = product.getAttribute('data-name').toLowerCase();
        if (productName.includes(query)) {
            product.style.display = 'block';  // Mostrar el producto
        } else {
            product.style.display = 'none';  // Ocultar el producto
        }
    });
}

let cart = JSON.parse(localStorage.getItem('cart')) || [];

function addToCart(productName, productPrice, productImage) {
    const existingProduct = cart.find(item => item.name === productName);

    if (existingProduct) {
        // Si el producto ya está en el carrito, incrementamos la cantidad
        existingProduct.quantity += 1;
    } else {
        // Si el producto no está en el carrito, lo añadimos con cantidad 1
        cart.push({ name: productName, price: productPrice, image: productImage, quantity: 1 });
    }

    localStorage.setItem('cart', JSON.stringify(cart)); // Guardar en localStorage
    alert(`${productName} ha sido agregado al carrito`);
}
