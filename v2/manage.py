import os
import unittest

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_restplus import Api
from flask import Blueprint
from api.endpoints import user
from api import create_app, db



app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK RESTPLUS API: STACKOVERFLOW-LITE',
          version='2.0',
          description='An Api for Stackoverflow-Lite'
          )
app.register_blueprint(blueprint)

app.app_context().push()

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

@manager.command
def run():
    app.run()

@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('api/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
    manager.run()