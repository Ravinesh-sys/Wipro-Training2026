import requests

BASE_URL = "http://127.0.0.1:5000"


def test_get_all_movies():
    response = requests.get(f"{BASE_URL}/api/movies")

    assert response.status_code == 200
    assert isinstance(response.json(), list)
def test_add_movie():
    payload = {
        "id": 201,
        "movie_name": "Inception",
        "language": "English",
        "duration": "2h 28m",
        "price": 300
    }

    response = requests.post(
        f"{BASE_URL}/api/movies",
        json=payload
    )

    assert response.status_code == 201

    data = response.json()
    assert data["id"] == 201
    assert data["movie_name"] == "Inception"
def test_get_movie_by_id():
    movie_id = 201  # the movie you added earlier

    response = requests.get(f"{BASE_URL}/api/movies/{movie_id}")

    assert response.status_code == 200

    data = response.json()
    assert data["id"] == movie_id
    assert data["movie_name"] == "Inception"
def test_update_movie():
    movie_id = 201

    updated_payload = {
        "movie_name": "Inception Updated",
        "language": "English",
        "duration": "2h 30m",
        "price": 400
    }

    response = requests.put(
        f"{BASE_URL}/api/movies/{movie_id}",
        json=updated_payload
    )

    assert response.status_code == 200

    data = response.json()
    assert data["movie_name"] == "Inception Updated"
    assert data["price"] == 400
def test_delete_movie():
    movie_id = 201

    response = requests.delete(f"{BASE_URL}/api/movies/{movie_id}")
    assert response.status_code == 200

    # Verify movie is deleted
    get_response = requests.get(f"{BASE_URL}/api/movies/{movie_id}")
    assert get_response.status_code == 404
def test_book_ticket():
    payload = {
        "movie_id": 101,
        "seats": 2,
        "customer_name": "Rahul Sharma"
    }

    response = requests.post(
        f"{BASE_URL}/api/bookings",
        json=payload
    )

    assert response.status_code == 201

    data = response.json()
    assert data["movie_id"] == 101
    assert data["seats"] == 2
    assert data["customer_name"] == "Rahul Sharma"
#this is the final implementation.
#All REST APIs are developed using Flask, tested manually using Postman, and automated using Pytest with assertions and proper status code validation.”