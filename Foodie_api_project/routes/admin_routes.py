from flask import Blueprint, jsonify
import storage

admin_bp = Blueprint("admin", __name__)

# Approve restaurant
@admin_bp.route("/approve/<int:rid>", methods=["PUT"])
def approve_restaurant(rid):
    restaurant = storage.restaurants.get(rid)

    if not restaurant:
        return jsonify({"error": "Not found"}), 404

    restaurant["approved"] = True
    return jsonify({"message": "Restaurant approved"})


# Disable by admin
@admin_bp.route("/disable/<int:rid>", methods=["PUT"])
def disable_by_admin(rid):
    restaurant = storage.restaurants.get(rid)

    if not restaurant:
        return jsonify({"error": "Not found"}), 404

    restaurant["active"] = False
    return jsonify({"message": "Disabled by admin"})


# View all orders
@admin_bp.route("/orders", methods=["GET"])
def view_orders():
    return jsonify(list(storage.orders.values()))