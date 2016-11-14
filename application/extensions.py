# -*- coding: utf-8 -*-

from playhouse.flask_utils import FlaskDB
from flask_login import LoginManager
from flask_wtf.csrf import CsrfProtect

lm = LoginManager()
db = FlaskDB()
csrf = CsrfProtect()