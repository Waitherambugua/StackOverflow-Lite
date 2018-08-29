import os
from flask import Flask

from app import create_app


config_name = os.getenv('FLASK_CONFIG') 
try:
    app = create_app(config_name)
except KeyError:
    app = create_app('development')

from app.manage import migrate
migrate()

if __name__ == '__main__':
    app.run(debug=True)