# *- coding: utf-8 -*

from flask import Flask
from .configuration import config

_all_ = ['create_app']

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    config_blueprint(app)
    configure_template_filters(app)

    return app

def config_blueprint(app):
    from .main import bpMain as mainBlueprint
    app.register_blueprint(mainBlueprint)

    from .show import bpShow as showBlueprint
    app.register_blueprint(showBlueprint, url_prefix='/show')


def configure_template_filters(app):
    """Configures the template filters."""
    pass