async function loadOrders() {

    const container = document.getElementById("ordersContainer");

    container.innerHTML = "";

    container.innerHTML += `

    <div class="product-card">

        <h2>Apple iPhone 16 Pro</h2>

        <p><strong>Price:</strong> ₹129999</p>

        <p><strong>Quantity:</strong> 1</p>

        <p><strong>Total:</strong> ₹129999</p>

    </div>

    `;

    container.innerHTML += `

    <div class="product-card">

        <h2>Samsung Galaxy S25 Ultra</h2>

        <p><strong>Price:</strong> ₹119999</p>

        <p><strong>Quantity:</strong> 1</p>

        <p><strong>Total:</strong> ₹119999</p>

    </div>

    `;

    container.innerHTML += `

    <div class="product-card">

        <h2>Google Pixel 10 Pro</h2>

        <p><strong>Price:</strong> ₹99999</p>

        <p><strong>Quantity:</strong> 1</p>

        <p><strong>Total:</strong> ₹99999</p>

    </div>

    `;
}

loadOrders();