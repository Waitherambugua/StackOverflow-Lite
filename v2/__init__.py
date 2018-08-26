from flask_restplus import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns

 blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK RESTPLUS API: STACKOVERFLOW-LITE',
          version='2.0',
          description='An Api for Stackoverflow-Lite'
          )

api.add_namespace(user_ns, path='/user')