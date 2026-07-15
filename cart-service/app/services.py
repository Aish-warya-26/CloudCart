from bson import ObjectId

from app.database import cart_collection

from app.models import serialize_cart



def get_cart(user_id):

    cart = cart_collection.find_one({

        "user_id": user_id

    })


    if cart:

        return serialize_cart(cart)


    return None



def create_cart(cart):

    result = cart_collection.insert_one(cart)

    return str(result.inserted_id)



def add_item(user_id, item):

    cart = cart_collection.find_one({

        "user_id": user_id

    })


    if cart:

        cart_collection.update_one(

            {
                "user_id": user_id
            },

            {
                "$push": {
                    "items": item
                }
            }

        )


    else:

        cart_collection.insert_one({

            "user_id": user_id,

            "items": [item]

        })