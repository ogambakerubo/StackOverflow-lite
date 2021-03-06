#StackOverflow-lite/app/__init__.py
from flask import Flask, Blueprint
from app.instance.config import APP_CONFIG
from app.api.v1.routes import VERSION_UNO as v1

def create_app(config_name):
    """ Creating the app using config file in instance folder """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(APP_CONFIG[config_name] or 'default')
    app.url_map.strict_slashes = False

    app.register_blueprint(v1)

    return app
