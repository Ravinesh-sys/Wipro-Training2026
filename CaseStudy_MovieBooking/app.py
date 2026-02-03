from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data
movies = []
bookings = []


# ---------------------------
# GET all movies
# ---------------------------
@app.route("/api/movies", methods=["GET"])
def get_movies():
    return jsonify(movies), 200


# ---------------------------
# POST new movie
# ---------------------------
@app.route("/api/movies", methods=["POST"])
def add_movie():
    data = request.json

    movie = {
        "id": data.get("id"),
        "movie_name": data.get("movie_name"),
        "language": data.get("language"),
        "duration": data.get("duration"),
        "price": data.get("price")
    }

    movies.append(movie)
    return jsonify(movie), 201


# ---------------------------
# GET movie by ID
# ---------------------------
@app.route("/api/movies/<int:movie_id>", methods=["GET"])
def get_movie_by_id(movie_id):
    for movie in movies:
        if movie["id"] == movie_id:
            return jsonify(movie), 200

    return jsonify({"message": "Movie not found"}), 404


# ---------------------------
# PUT update movie
# ---------------------------
@app.route("/api/movies/<int:movie_id>", methods=["PUT"])
def update_movie(movie_id):
    data = request.json

    for movie in movies:
        if movie["id"] == movie_id:
            movie["movie_name"] = data.get("movie_name", movie["movie_name"])
            movie["language"] = data.get("language", movie["language"])
            movie["duration"] = data.get("duration", movie["duration"])
            movie["price"] = data.get("price", movie["price"])

            return jsonify(movie), 200

    return jsonify({"message": "Movie not found"}), 404


# ---------------------------
# DELETE movie
# ---------------------------
@app.route("/api/movies/<int:movie_id>", methods=["DELETE"])
def delete_movie(movie_id):
    for movie in movies:
        if movie["id"] == movie_id:
            movies.remove(movie)
            return jsonify({"message": "Movie deleted successfully"}), 200

    return jsonify({"message": "Movie not found"}), 404


# ---------------------------
# POST booking
# ---------------------------
@app.route("/api/bookings", methods=["POST"])
def book_ticket():
    data = request.json

    booking = {
        "booking_id": len(bookings) + 1,
        "movie_id": data.get("movie_id"),
        "seats": data.get("seats"),
        "customer_name": data.get("customer_name")
    }

    bookings.append(booking)
    return jsonify(booking), 201


# ---------------------------
# Run app
# ---------------------------
if __name__ == "__main__":
    app.run(debug=True)
