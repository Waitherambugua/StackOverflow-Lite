from flask import flask
from flask_restful import Api

from api.endpoints.users import (signup, login)
from api.endpoints.questions import (signup, login)

app = Flask(__name__)
api = Api(app)

api.add_resource(UserRegister, '/api/v2/auth/signup')
api.add_resource(UserLogin, '/api/v2/auth/login')
