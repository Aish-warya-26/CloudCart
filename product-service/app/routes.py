from flask import Blueprint, request
from bson import ObjectId
import logging

from app.services import (
    get_all_products,
    get_product,
    add_product,
    update_product,
    delete_product
)

from app.utils import (
    success_response,
    error_response
)


product_bp = Blueprint("products", __name__)

logger = logging.getLogger(__name__)


@product_bp.route("/health", methods=["GET"])
def health():

    return success_response(
        "Product Service Running"
    )


@product_bp.route("/products", methods=["GET"])
def products():

    try:
        products = get_all_products()

        return success_response(
            "Products fetched successfully",
            products
        )

    except Exception as e:

        logger.error(str(e))

        return error_response(
            "Unable to fetch products",
            500
        )


@product_bp.route("/products/<product_id>", methods=["GET"])
def product(product_id):

    try:

        if not ObjectId.is_valid(product_id):
            return error_response(
                "Invalid product ID",
                400
            )


        product = get_product(product_id)


        if product is None:

            return error_response(
                "Product not found",
                404
            )


        return success_response(
            "Product fetched successfully",
            product
        )


    except Exception as e:

        logger.error(str(e))

        return error_response(
            "Something went wrong",
            500
        )



@product_bp.route("/products", methods=["POST"])
def create_product():

    try:

        data = request.get_json()


        if not data:

            return error_response(
                "Request body missing",
                400
            )


        required_fields = [
            "name",
            "price",
            "quantity"
        ]


        for field in required_fields:

            if field not in data:

                return error_response(
                    f"{field} is required",
                    400
                )


        product = {

            "name": data["name"],

            "price": float(data["price"]),

            "quantity": int(data["quantity"])

        }


        product_id = add_product(product)


        return success_response(
            "Product created successfully",
            {
                "id": product_id
            },
            201
        )


    except Exception as e:

        logger.error(str(e))

        return error_response(
            "Unable to create product",
            500
        )



@product_bp.route("/products/<product_id>", methods=["PUT"])
def update(product_id):

    try:


        if not ObjectId.is_valid(product_id):

            return error_response(
                "Invalid product ID",
                400
            )


        data = request.get_json()


        if not data:

            return error_response(
                "Request body missing",
                400
            )


        updated_product = {}


        allowed_fields = [
            "name",
            "price",
            "quantity"
        ]


        for field in allowed_fields:

            if field in data:

                updated_product[field] = data[field]



        if not updated_product:

            return error_response(
                "No valid fields provided",
                400
            )



        result = update_product(
            product_id,
            updated_product
        )


        if result == 0:

            return error_response(
                "Product not found",
                404
            )


        return success_response(
            "Product updated successfully"
        )



    except Exception as e:

        logger.error(str(e))

        return error_response(
            "Unable to update product",
            500
        )



@product_bp.route("/products/<product_id>", methods=["DELETE"])
def remove_product(product_id):

    try:

        if not ObjectId.is_valid(product_id):

            return error_response(
                "Invalid product ID",
                400
            )


        result = delete_product(product_id)


        if result == 0:

            return error_response(
                "Product not found",
                404
            )


        return success_response(
            "Product deleted successfully"
        )


    except Exception as e:

        logger.error(str(e))

        return error_response(
            "Unable to delete product",
            500
        )