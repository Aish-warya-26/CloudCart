# ☁️ CloudCart

CloudCart is a cloud-native e-commerce application developed using a microservices architecture.

## GitHub Repository

https://github.com/Aish-warya-26/CloudCart

# Screenshots

## Home

![Home](screenshots/home.png)

---

## Features

- Product Management
- Shopping Cart
- Order Management
- MongoDB Database
- Docker Containers
- Kubernetes Deployment
- REST APIs
- Responsive Frontend

---

## Tech Stack

- Python Flask
- MongoDB
- Docker
- Kubernetes
- HTML
- CSS
- JavaScript
- Nginx

---

## Microservices

### Product Service

- View Products
- Product APIs

### Cart Service

- Add to Cart
- View Cart

### Order Service

- Place Orders
- View Orders

---

## Project Structure

```
CloudCart/
│
├── product-service/
├── cart-service/
├── order-service/
├── frontend/
├── k8s/
└── README.md
```

---

## Running Project

### Build Images

```bash
docker build -t product-service ./product-service
docker build -t cart-service ./cart-service
docker build -t order-service ./order-service
```

### Deploy

```bash
kubectl apply -f k8s/
```

### Port Forward

```bash
kubectl port-forward svc/product-service 5000:5000

kubectl port-forward svc/cart-service 5001:5001

kubectl port-forward svc/order-service 5002:5002
```

### Frontend

```
http://localhost:8080
```

---

## APIs

### Product

GET

```
/products
```

### Cart

GET

```
/cart/<user_id>
```

POST

```
/cart/<user_id>/items
```

### Order

GET

```
/orders
```

POST

```
/orders
```

---

## Author

Aishwarya Chourasia
