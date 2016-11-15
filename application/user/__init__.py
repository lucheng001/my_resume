# -*- coding: utf-8 -*-

from flask import Blueprint

bpUser = Blueprint('bpUser', __name__)

from . import views_user, views_profile