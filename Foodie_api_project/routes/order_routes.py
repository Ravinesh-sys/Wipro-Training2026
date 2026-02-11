from flask import Blueprint, request, jsonify
import storage

order_bp = Blueprint("order", __name__)

# Place order
@order_bp.route("/", methods=["POST"])
def place_order():
    data = request.json

    user_id = data.get("user_id")
    dish_id = data.get("dish_id")

    if user_id not in storage.users:
        return jsonify({"error": "User not found"}), 404

    if dish_id not in storage.dishes:
        return jsonify({"error": "Dish not found"}), 404

    oid = storage.order_id_counter

    order = {
        "id": oid,
        "user_id": user_id,
        "dish_id": dish_id,
        "status": "placed"
    }

    storage.orders[oid] = order
    storage.order_id_counter += 1

    return jsonify({"message": "Order placed", "data": order}), 201


# Orders by user
@order_bp.route("/user/<int:user_id>", methods=["GET"])
def orders_by_user(user_id):
    result = [o for o in storage.orders.values() if o["user_id"] == user_id]
    return jsonify(result)


# Orders by restaurant
@order_bp.route("/restaurant/<int:rid>", methods=["GET"])
def orders_by_restaurant(rid):
    result = []
    for order in storage.orders.values():
        dish = storage.dishes.get(order["dish_id"])
        if dish and dish["restaurant_id"] == rid:
            result.append(order)

    return jsonify(result)