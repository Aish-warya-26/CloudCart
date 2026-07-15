async function loadProducts() {

    const container = document.getElementById("productsContainer");

    container.innerHTML = "<h2>Loading Products...</h2>";

    try {

        const response = await getProducts();

        container.innerHTML = "";

        if (!response.success) {

            container.innerHTML = "<h2>Unable to load products.</h2>";

            return;

        }

        response.data.forEach(product => {

            container.innerHTML += `

            <div class="product-card">

                <h2>${product.name}</h2>

                <p><strong>Price:</strong> ₹${product.price}</p>

                <p><strong>Stock:</strong> ${product.quantity}</p>

                <button onclick="addProduct('${product.id}')">

                    Add to Cart

                </button>

            </div>

            `;

        });

    }

    catch (err) {

        container.innerHTML =

        "<h2>Cannot connect to Product Service.</h2>";

    }

}



async function addProduct(productId){

    try{

        const response = await addToCart(productId,1);

        if(response.success){

            alert("Product added to cart!");

        }

        else{

            alert(response.message);

        }

    }

    catch{

        alert("Cart Service is not available.");

    }

}



loadProducts();