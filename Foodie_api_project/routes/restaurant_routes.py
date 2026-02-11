from flask import Blueprint, request, jsonify
import storage

restaurant_bp = Blueprint("restaurant", __name__)

# Register restaurant
@restaurant_bp.route("/", methods=["POST"])
def register_restaurant():
    data = request.json

    global_id = storage.restaurant_id_counter

    restaurant = {
        "id": global_id,
        "name": data.get("name"),
        "category": data.get("category"),
        "location": data.get("location"),
        "contact": data.get("contact"),
        "active": True,
        "approved": False
    }

    storage.restaurants[global_id] = restaurant
    storage.restaurant_id_counter += 1

    return jsonify({"message": "Restaurant registered", "data": restaurant}), 201


# Update restaurant
@restaurant_bp.route("/<int:rid>", methods=["PUT"])
def update_restaurant(rid):
    restaurant = storage.restaurants.get(rid)

    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404

    data = request.json
    restaurant.update(data)

    return jsonify({"message": "Restaurant updated", "data": restaurant})


# Disable restaurant
@restaurant_bp.route("/<int:rid>/disable", methods=["PUT"])
def disable_restaurant(rid):
    restaurant = storage.restaurants.get(rid)

    if not restaurant:
        return jsonify({"error": "Not found"}), 404

    restaurant["active"] = False

    return jsonify({"message": "Restaurant disabled"})


# View restaurant
@restaurant_bp.route("/<int:rid>", methods=["GET"])
def view_restaurant(rid):
    restaurant = storage.restaurants.get(rid)

    if not restaurant:
        return jsonify({"error": "Not found"}), 404

    return jsonify(restaurant)

# View all restaurants
@restaurant_bp.route("/", methods=["GET"])
def view_all_restaurants():
    return jsonify(list(storage.restaurants.values()))