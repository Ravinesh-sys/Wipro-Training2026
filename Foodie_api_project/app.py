from flask import Flask
from routes.restaurant_routes import restaurant_bp
from routes.dish_routes import dish_bp
from routes.user_routes import user_bp
from routes.admin_routes import admin_bp
from routes.order_routes import order_bp

app = Flask(__name__)

app.register_blueprint(restaurant_bp, url_prefix="/restaurants")
app.register_blueprint(dish_bp, url_prefix="/dishes")
app.register_blueprint(user_bp, url_prefix="/users")
app.register_blueprint(admin_bp, url_prefix="/admin")
app.register_blueprint(order_bp, url_prefix="/orders")

if __name__ == "__main__":
    app.run(debug=True)