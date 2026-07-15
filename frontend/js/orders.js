async function loadOrders() {

    const container = document.getElementById("ordersContainer");

    container.innerHTML = "<h2>Loading Orders...</h2>";

    try {

        const response = await getOrders();

        container.innerHTML = "";

        if (!response.success) {

            container.innerHTML = "<h2>No Orders Found.</h2>";

            return;

        }

        if (response.data.length === 0) {

            container.innerHTML = "<h2>No Orders Found.</h2>";

            return;

        }

        response.data.forEach(order => {

            container.innerHTML += `

            <div class="product-card">

                <h2>Order ID</h2>

                <p>${order.id}</p>

                <p><strong>User:</strong> ${order.user_id}</p>

                <p><strong>Total:</strong> ₹${order.total}</p>

            </div>

            `;

        });

    }

    catch (err) {

        container.innerHTML =

        "<h2>Order Service is not available.</h2>";

    }

}

loadOrders();