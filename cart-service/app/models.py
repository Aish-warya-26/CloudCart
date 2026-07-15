def serialize_cart(cart):

    return {

        "id": str(cart["_id"]),

        "user_id": cart["user_id"],

        "items": cart["items"]

    }