from flask import Blueprint, request, jsonify
from .services import create_order, get_orders, get_order, delete_order

order_bp = Blueprint("orders", __name__)

@order_bp.route("/orders", methods=["POST"])
def add_order():
    data = request.json

    if "customer" not in data or "items" not in data:
        return jsonify({"error": "Invalid order"}), 400

    data.setdefault("total", 0)
    data.setdefault("status", "Pending")

    return jsonify(create_order(data)), 201


@order_bp.route("/orders", methods=["GET"])
def all_orders():
    return jsonify(get_orders())


@order_bp.route("/orders/<order_id>", methods=["GET"])
def single_order(order_id):
    order = get_order(order_id)

    if order:
        return jsonify(order)

    return jsonify({"message": "Order not found"}), 404


@order_bp.route("/orders/<order_id>", methods=["DELETE"])
def remove_order(order_id):
    if delete_order(order_id):
        return jsonify({"message": "Order deleted"})

    return jsonify({"message": "Order not found"}), 404

@order_bp.route("/health", methods=["GET"])
def health():
    return jsonify({
        "success": True,
        "message": "Order Service Running"
    })