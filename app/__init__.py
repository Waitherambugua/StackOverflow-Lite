import re
from flask_api import FlaskAPI
from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from app.db import Database


from config import CONFIGS

def create_app(config_name):

    app = Flask(__name__, instance_relative_config=True)
    #key = frozenset(app_config.items())
    app.config.from_object(CONFIGS[config_name])
    from app.main import main_blueprint
    app.register_blueprint(main_blueprint)

    db = Database()
    db.init_app(app)
    jwt = JWTManager(app)

    return app     