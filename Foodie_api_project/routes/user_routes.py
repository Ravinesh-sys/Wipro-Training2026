from flask import Blueprint, request, jsonify
import storage

user_bp = Blueprint("user", __name__)

# User registration
@user_bp.route("/", methods=["POST"])
def register_user():
    data = request.json
    uid = storage.user_id_counter

    user = {
        "id": uid,
        "name": data.get("name"),
        "email": data.get("email")
    }

    storage.users[uid] = user
    storage.user_id_counter += 1

    return jsonify({"message": "User registered", "data": user}), 201


# Search restaurants
@user_bp.route("/search", methods=["GET"])
def search_restaurants():
    result = [
        r for r in storage.restaurants.values()
        if r["active"] and r["approved"]
    ]
    return jsonify(result)


# Give rating
@user_bp.route("/rating/<int:restaurant_id>", methods=["POST"])
def give_rating(restaurant_id):
    if restaurant_id not in storage.restaurants:
        return jsonify({"error": "Restaurant not found"}), 404

    return jsonify({"message": "Rating submitted"})

# View user by id
@user_bp.route("/<int:uid>", methods=["GET"])
def view_user(uid):
    user = storage.users.get(uid)

    if not user:
        return jsonify({"error": "User not found"}), 404

    return jsonify(user)

# View all users
@user_bp.route("/", methods=["GET"])
def view_all_users():
    return jsonify(list(storage.users.values()))