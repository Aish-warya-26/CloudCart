async function loadCart() {

    const container = document.getElementById("cartContainer");

    container.innerHTML = "<h2>Loading Cart...</h2>";

    try {

        const response = await getCart();

        container.innerHTML = "";

        if (!response.success) {

            container.innerHTML = "<h2>Your cart is empty.</h2>";

            return;

        }

        if (response.data.items.length === 0) {

            container.innerHTML = "<h2>Your cart is empty.</h2>";

            return;

        }

        response.data.items.forEach(item => {

            container.innerHTML += `

            <div class="product-card">

                <h2>${item.product_id}</h2>

                <p><strong>Quantity:</strong> ${item.quantity}</p>

            </div>

            `;

        });

    }

    catch (err) {

        container.innerHTML =

        "<h2>Cart Service is not available.</h2>";

    }

}

loadCart();