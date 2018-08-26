from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

from .config import config_by_name

db = SQLAlchemy()
flask_bcrypt = Bcrypt()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)
    flask_bcrypt.init_app(app)

    return app






"""from flask import Flask
from flask_restful import Api


from api.endpoints.users import (signup, login)
from api.endpoints.questions import (signup, login)

app = Flask(__name__)
api = Api(app)

api.add_resource(SignUp, '/api/v2/auth/signup')
api.add_resource(Login, '/api/v2/auth/login')
api.add_resource(Questions, '/api/v2/questions')
api.add_resource(Question, '/api/v2/questions/<int:id>')
api.add_resource(postQuestion, '/api/v2/questions/<int:id>')
api.add_resource(postAnswer, '/api/v2/questions/<int:id>')
"""