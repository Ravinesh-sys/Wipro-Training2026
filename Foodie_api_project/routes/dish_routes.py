from flask import Blueprint, request, jsonify
import storage

dish_bp = Blueprint("dish", __name__)

# Add dish
@dish_bp.route("/<int:restaurant_id>", methods=["POST"])
def add_dish(restaurant_id):
    if restaurant_id not in storage.restaurants:
        return jsonify({"error": "Restaurant not found"}), 404

    data = request.json
    did = storage.dish_id_counter

    dish = {
        "id": did,
        "restaurant_id": restaurant_id,
        "name": data.get("name"),
        "price": data.get("price"),
        "available": True
    }

    storage.dishes[did] = dish
    storage.dish_id_counter += 1

    return jsonify({"message": "Dish added", "data": dish}), 201

# View dish by id
@dish_bp.route("/<int:dish_id>", methods=["GET"])
def view_dish(dish_id):
    dish = storage.dishes.get(dish_id)

    if not dish:
        return jsonify({"error": "Dish not found"}), 404

    return jsonify(dish)


# View all dishes
@dish_bp.route("/", methods=["GET"])
def view_all_dishes():
    return jsonify(list(storage.dishes.values()))


# Update dish
@dish_bp.route("/<int:dish_id>", methods=["PUT"])
def update_dish(dish_id):
    dish = storage.dishes.get(dish_id)

    if not dish:
        return jsonify({"error": "Dish not found"}), 404

    data = request.json
    dish.update(data)

    return jsonify({"message": "Dish updated", "data": dish})


# Enable/Disable dish
@dish_bp.route("/<int:dish_id>/toggle", methods=["PUT"])
def toggle_dish(dish_id):
    dish = storage.dishes.get(dish_id)

    if not dish:
        return jsonify({"error": "Dish not found"}), 404

    dish["available"] = not dish["available"]

    return jsonify({"message": "Dish availability changed", "data": dish})


# Delete dish
@dish_bp.route("/<int:dish_id>", methods=["DELETE"])
def delete_dish(dish_id):
    if dish_id not in storage.dishes:
        return jsonify({"error": "Dish not found"}), 404

    del storage.dishes[dish_id]
    return jsonify({"message": "Dish deleted"})