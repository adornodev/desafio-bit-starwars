import os
from flask import Flask
from flask_pymongo import PyMongo

mongo = PyMongo()

def create_app():
    config_filename = os.getenv('FLASK_ENV', 'development') + '.cfg'

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(config_filename)

    init_mongo(app)
    register_controllers(app)

    return app

def init_mongo(app):
    mongo.init_app(app)
    from app.models.planet import Planet

def register_controllers(app):
    from app.controllers import planet_blueprints
    app.register_blueprint(planet_blueprints)