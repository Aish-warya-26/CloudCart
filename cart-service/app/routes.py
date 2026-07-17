from flask import Blueprint, request
import logging

from app.services import (
    get_cart,
    add_item
)

from app.utils import (
    success_response,
    error_response
)


cart_bp = Blueprint(
    "cart",
    __name__
)


logger = logging.getLogger(__name__)


@cart_bp.route("/health", methods=["GET"])
def health():

    return success_response(
        "Cart Service Running"
    )


@cart_bp.route("/cart/<user_id>", methods=["GET"])
def fetch_cart(user_id):

    try:

        cart = get_cart(user_id)

        if cart is None:

            return error_response(
                "Cart not found",
                404
            )

        return success_response(
            "Cart fetched successfully",
            cart
        )

    except Exception as e:

        logger.error(str(e))

        return error_response(
            "Unable to fetch cart",
            500
        )


@cart_bp.route("/cart/<user_id>/items", methods=["POST"])
def add_cart_item(user_id):

    try:

        data = request.get_json()

        if not data:

            return error_response(
                "Request body missing",
                400
            )

        required_fields = [
            "product_id",
            "quantity"
        ]

        for field in required_fields:

            if field not in data:

                return error_response(
                    f"{field} is required",
                    400
                )

        item = {

            "product_id": data["product_id"],

            "quantity": int(data["quantity"])

        }

        add_item(
            user_id,
            item
        )

        return success_response(
            "Item added to cart"
        )

    except Exception as e:

        logger.error(str(e))

        return error_response(
            "Unable to add item",
            500
        )