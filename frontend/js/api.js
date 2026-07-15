/* ==========================================
   CloudCart API Configuration
========================================== */

// Development URLs
const API = {

    PRODUCT_SERVICE: "http://localhost:5000",

    CART_SERVICE: "http://localhost:5001",

    ORDER_SERVICE: "http://localhost:5002"

};


// Change this to any user ID you want
const USER_ID = "user123";



/* ==========================================
   Product APIs
========================================== */

async function getProducts() {

    const response = await fetch(
        `${API.PRODUCT_SERVICE}/products`
    );

    return await response.json();

}



/* ==========================================
   Cart APIs
========================================== */

async function getCart() {

    const response = await fetch(
        `${API.CART_SERVICE}/cart/${USER_ID}`
    );

    return await response.json();

}


async function addToCart(productId, quantity = 1) {

    const response = await fetch(

        `${API.CART_SERVICE}/cart/${USER_ID}/items`,

        {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({

                product_id: productId,

                quantity: quantity

            })

        }

    );

    return await response.json();

}



/* ==========================================
   Order APIs
========================================== */

async function getOrders() {

    const response = await fetch(
        `${API.ORDER_SERVICE}/orders`
    );

    return await response.json();

}


async function createOrder(order) {

    const response = await fetch(

        `${API.ORDER_SERVICE}/orders`,

        {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify(order)

        }

    );

    return await response.json();

}