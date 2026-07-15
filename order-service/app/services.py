from bson import ObjectId
from .database import orders
from .models import serialize_order

def create_order(data):
    result = orders.insert_one(data)
    return serialize_order(orders.find_one({"_id": result.inserted_id}))

def get_orders():
    return [serialize_order(order) for order in orders.find()]

def get_order(order_id):
    order = orders.find_one({"_id": ObjectId(order_id)})
    if order:
        return serialize_order(order)
    return None

def delete_order(order_id):
    result = orders.delete_one({"_id": ObjectId(order_id)})
    return result.deleted_count > 0