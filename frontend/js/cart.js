async function loadCart() {

    const container = document.getElementById("cartContainer");

    container.innerHTML = "<h2>Loading Cart...</h2>";

    try {

        const response = await getCart();

        container.innerHTML = "";

        if (!response.success || response.data.items.length === 0) {

            container.innerHTML = "<h2>Your cart is empty.</h2>";

            return;

        }

        let grandTotal = 0;

        for (const item of response.data.items) {

            const productResponse = await getProduct(item.product_id);

            if (!productResponse.success) {
                continue;
            }

            const product = productResponse.data;

            const subtotal = product.price * item.quantity;

            grandTotal += subtotal;

            container.innerHTML += `

            <div class="product-card">

                <h2>${product.name}</h2>

                <p><strong>Price:</strong> ₹${product.price}</p>

                <p><strong>Quantity:</strong> ${item.quantity}</p>

                <p><strong>Subtotal:</strong> ₹${subtotal}</p>

            </div>

            `;

        }

        container.innerHTML += `

        <div class="product-card">

            <h2>Grand Total</h2>

            <h1>₹${grandTotal}</h1>

            <button onclick="checkout(${grandTotal})">
                Checkout
            </button>

        </div>

        `;

    }

    catch(err){

        container.innerHTML =
        "<h2>Cart Service is not available.</h2>";

    }

}

async function checkout(total){

    try{

        const cartResponse = await getCart();

        const order = {

            customer: USER_ID,

            items: cartResponse.data.items,

            total: total

        };

        const response = await createOrder(order);

        if(response){

            alert("✅ Order placed successfully!");

            console.log(response);

        }

    }

    catch(err){

        console.error(err);

        alert("❌ Unable to place order.");

    }

}

loadCart();