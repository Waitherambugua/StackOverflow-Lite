import os
from app import create_app
from app.databas.db import Database

db = Database()
config_name = os.getenv('FLASK_CONFIG')
try:
    app = create_app(config_name)
except KeyError:
    app = create_app('development')


if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True, port=5001)
