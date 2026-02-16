import requests

BASE_URL = "http://127.0.0.1:5000"

def test_register_restaurant():
    response = requests.post(f"{BASE_URL}/restaurants/", json={
        "name": "TestHotel",
        "category": "Veg",
        "location": "Delhi",
        "contact": "8888888888"
    })
    assert response.status_code == 201

def test_view_all_restaurants():
    response = requests.get(f"{BASE_URL}/restaurants/")
    assert response.status_code == 200

def test_view_restaurant_by_id():
    response = requests.get(f"{BASE_URL}/restaurants/1")
    assert response.status_code in [200,404]
