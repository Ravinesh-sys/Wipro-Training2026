from flask import Blueprint, request, jsonify
import storage

restaurant_bp = Blueprint("restaurant", __name__)

# ---------------- REGISTER RESTAURANT ----------------
@restaurant_bp.route("/", methods=["POST"])
def register_restaurant():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "No data provided"}), 400

        rid = storage.restaurant_id_counter

        restaurant = {
            "id": rid,
            "name": data.get("name"),
            "category": data.get("category"),
            "location": data.get("location"),
            "contact": data.get("contact"),
            "active": True,
            "approved": False
        }

        storage.restaurants[rid] = restaurant
        storage.restaurant_id_counter += 1

        return jsonify({
            "message": "Restaurant registered successfully",
            "data": restaurant
        }), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ---------------- UPDATE RESTAURANT ----------------
@restaurant_bp.route("/<int:rid>", methods=["PUT"])
def update_restaurant(rid):
    restaurant = storage.restaurants.get(rid)

    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404

    data = request.get_json()

    restaurant["name"] = data.get("name", restaurant["name"])
    restaurant["category"] = data.get("category", restaurant["category"])
    restaurant["location"] = data.get("location", restaurant["location"])
    restaurant["contact"] = data.get("contact", restaurant["contact"])

    return jsonify({
        "message": "Restaurant updated",
        "data": restaurant
    }), 200


# ---------------- DISABLE RESTAURANT ----------------
@restaurant_bp.route("/<int:rid>/disable", methods=["PUT"])
def disable_restaurant(rid):
    restaurant = storage.restaurants.get(rid)

    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404

    restaurant["active"] = False

    return jsonify({"message": "Restaurant disabled"}), 200


# ---------------- VIEW RESTAURANT BY ID ----------------
@restaurant_bp.route("/<int:rid>", methods=["GET"])
def view_restaurant(rid):
    restaurant = storage.restaurants.get(rid)

    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404

    return jsonify(restaurant), 200


# ---------------- VIEW ALL RESTAURANTS ----------------
@restaurant_bp.route("/", methods=["GET"])
def view_all_restaurants():
    return jsonify(list(storage.restaurants.values())), 200
