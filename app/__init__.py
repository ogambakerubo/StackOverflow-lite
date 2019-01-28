#StackOverflow-lite/app/__init__.py
from flask import Flask
from app.instance .config import APP_CONFIG

def create_app(config_name):
    """ Creating the app using config file in instance folder """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(APP_CONFIG[config_name] or 'default')
    
    return app
