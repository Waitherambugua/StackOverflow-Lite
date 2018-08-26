import re
from flask_api import FlaskAPI
from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from app.database import Database
db = Database()

# local import
from instance.config import app_config

def create_app(config_name):

    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    db.init_app(app)

    jwt = JWTManager(app)

    from app import routes
    app.register_blueprint(routes.web, url_prefix="/")

    @app.errorhandler(404)
    def page_not_found(error):
        return jsonify("The resource does not exist"), 404

    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify("Encountering an internal error with our server!"), 500

    @app.errorhandler(403)
    def forbidden(error):
        return jsonify("You do not permission to access this resource"), 403

    # @app.errorhandler(400)
    # def validate_date(data):
    #     """Validate user details."""
    #     try:
    #         # check if there are special charaters in the email.
    #         if not re.match("^[a-zA-Z0-9_]*$", data["name"].strip()):
    #             return "Name can only contain alphanumeric characters"
    #         # check if email is more than 3 characters
    #         elif len(data['name'].strip()) < 3:
    #             return "Name must be more than 3 characters"
    #         # check if the name conatain only numbers or underscore
    #         elif not re.match("[a-zA-Z]{3,}_*[0-9_]*[a-zA-Z]*_*", data['name'].strip()):
    #             return "Name must have atleast 3 letters before number or underscore."
    #         elif not re.match("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+[a-zA-Z0-9-.]+$", data['email'].strip()):
    #             return "Please provide a valid email"
    #         else:
    #             return "Valid"
    #     except Exception as error:
    #         return "Please provide all the fields, missing "+ str(error)
    
    # def validate_password(data):
    #     """Validate the password and return appropriate response."""
    #     try:
    #         # chack for spaces in password
    #         if " " in data["password"]:
    #             return "password should be one word, no spaces"
    #         elif len(data['password'].strip()) < 6:
    #             return "Password should have atleast 6 characters"
    #         # check if the passwords mact
    #         elif data['password'] != data['cnfpass']:
    #             return "passwords do not match"
    #         else:
    #             return "valid"
    #     # some data is missing and a keyError exception was raised
    #     except Exception as error:
    #         return "please provide all the fields, missing " + str(error)


    return app
