def serialize_order(order):
    return {
        "id": str(order["_id"]),
        "customer": order["customer"],
        "items": order["items"],
        "total": order["total"],
        "status": order["status"]
    }