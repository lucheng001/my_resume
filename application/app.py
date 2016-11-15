# -*- coding: utf-8 -*-

import os
import logging
from flask import Flask
from .extensions import db, lm, csrf
from .configuration import config

_all_ = ['create_app']

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    config_extensions(app)
    config_blueprint(app)
    configure_template_filters(app)

    return app

def config_blueprint(app):
    from .main import bpMain as mainBlueprint
    app.register_blueprint(mainBlueprint)

    from .show import bpShow as showBlueprint
    app.register_blueprint(showBlueprint, url_prefix='/show')

    from .auth import bpAuth as authBlueprint
    app.register_blueprint(authBlueprint, url_prefix='/auth')

    from .user import bpUser as userBlueprint
    app.register_blueprint(userBlueprint, url_prefix='/user')

    from .project import  bpProject as projectBlueprint
    app.register_blueprint(projectBlueprint, url_prefix='/project')


def configure_template_filters(app):
    """Configures the template filters."""
    pass

def config_extensions(app):
    db.init_app(app)
    csrf.init_app(app)
    lm.init_app(app)
    lm.session_protection = 'strong'
    lm.login_view = 'bpAuth.login'
    lm.login_message = u'请登录'
    lm.refresh_view = u'请重新登录'

    @lm.user_loader
    def load_user(user_id):
        from .models import User
        try:
            user = User.get(User.id == int(user_id))
        except:
            user = None
        return user

def config_logging(app):
    from logging.handlers import RotatingFileHandler

    logsFolder = app.config['APP_LOG_DIR']
    formatter = app.config['APP_LOG_FORMATTER']

    infoLog = os.path.join(logsFolder, app.config['APP_LOG_INFO'])
    infoFileHandler = RotatingFileHandler(
        infoLog,
        maxBytes=app.config['APP_LOG_SIZE'],
        backupCount=10
    )
    infoFileHandler.setLevel(logging.INFO)
    infoFileHandler.setFormatter(formatter)
    app.logger.addHandler(infoFileHandler)

    errorLog = os.path.join(logsFolder, app.config['APP_LOG_ERROR'])
    errorFileHandler = RotatingFileHandler(
        errorLog,
        maxBytes=app.config['APP_LOG_SIZE'],
        backupCount=10
    )
    errorFileHandler.setLevel(logging.ERROR)
    errorFileHandler.setFormatter(formatter)
    app.logger.addHandler(errorFileHandler)