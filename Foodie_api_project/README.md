# 🍔 Foodie App REST API (Flask Project)

## 📌 Project Overview

This project is a **Foodie App Backend** developed using **Python Flask**.
It simulates a real-world food ordering system where restaurants can register, add dishes, users can place orders, and admin can manage the platform.

The project also includes **manual and automation testing** using Postman, Pytest, and Robot Framework.

---

## 🛠️ Tech Stack

* Python 3
* Flask
* REST API
* Postman (Manual Testing)
* Pytest (Automation Testing)
* Robot Framework (Automation Testing)

---

## 📂 Project Structure

Foodie_api_project
│
├── routes/ (All API route files)
├── tests/ (Pytest automation tests)
├── robot_tests/ (Robot framework tests)
├── postman collection/ (Postman manual testing collection)
├── app.py (Main Flask app)
├── storage.py (In-memory database)
├── requirements.txt
└── README.md

---

## 🚀 Features Implemented

### 🟢 Restaurant Module

* Register restaurant
* Update restaurant
* Disable restaurant
* View restaurant
* View all restaurants

### 🟢 Dish Module

* Add dish
* Update dish
* Delete dish
* Enable/Disable dish
* View dishes

### 🟢 User Module

* Register user
* Search restaurants
* Place order
* Give rating

### 🟢 Admin Module

* Approve restaurant
* Disable restaurant
* View orders

### 🟢 Order Module

* Place order
* View orders by user
* View orders by restaurant

---

## 🧪 Testing

### 🔹 Manual Testing

Postman collection included to test all APIs manually.

### 🔹 Pytest Automation

Run pytest using:
pytest -v

### 🔹 Robot Framework Automation

Run robot tests using:
robot robot_tests/api_tests.robot

Robot reports generated:

* report.html
* log.html

---

## ▶️ How to Run Project

### Install dependencies

pip install -r requirements.txt

### Run Flask server

python app.py

Server runs on:
http://127.0.0.1:5000

---

## 🎯 Objective

To build a complete REST API backend and perform manual and automation testing using Postman, Pytest and Robot Framework.

---

## 👨‍💻 Author

Foodie App Backend Project
Developed as part of backend & testing assignment.
