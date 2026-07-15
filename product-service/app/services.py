from bson import ObjectId
from app.database import products_collection
from app.models import serialize_product


def get_all_products():
    return [
        serialize_product(product)
        for product in products_collection.find()
    ]


def get_product(product_id):
    product = products_collection.find_one({
        "_id": ObjectId(product_id)
    })

    if product:
        return serialize_product(product)

    return None


def add_product(product):
    result = products_collection.insert_one(product)
    return str(result.inserted_id)


def update_product(product_id, product):
    result = products_collection.update_one(
        {"_id": ObjectId(product_id)},
        {"$set": product}
    )

    return result.modified_count


def delete_product(product_id):
    result = products_collection.delete_one(
        {"_id": ObjectId(product_id)}
    )

    return result.deleted_count
