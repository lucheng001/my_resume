# -*- coding: utf-8 -*-

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