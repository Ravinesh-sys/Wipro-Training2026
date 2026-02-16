import requests

BASE_URL = "http://127.0.0.1:5000"

def test_add_dish():
    response = requests.post(f"{BASE_URL}/dishes/1", json={
        "name": "TestPizza",
        "price": 250
    })
    assert response.status_code in [201,404]

def test_view_all_dishes():
    response = requests.get(f"{BASE_URL}/dishes/")
    assert response.status_code == 200

def test_view_dish_by_id():
    response = requests.get(f"{BASE_URL}/dishes/1")
    assert response.status_code in [200,404]
