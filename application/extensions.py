# -*- coding: utf-8 -*-

from playhouse.flask_utils import FlaskDB
from flask_login import LoginManager

lm = LoginManager()
db = FlaskDB()