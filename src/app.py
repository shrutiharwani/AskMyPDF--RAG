from flask import Flask
from src.routes import register_routes
from src.services.history_db import init_db


def create_app():
    app = Flask(__name__)
    app.secret_key = "super-secret-key"

    # ✅ Initialize SQLite DB
    init_db()

    # ✅ Register all routes
    register_routes(app)

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
