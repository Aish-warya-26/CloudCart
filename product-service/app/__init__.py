from flask import Flask
from flask_cors import CORS
from app.routes import product_bp
import logging


def create_app():

    app = Flask(__name__)

    CORS(app)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s"
    )

    app.register_blueprint(product_bp)

    return app