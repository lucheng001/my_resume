# -*- coding: utf-8 -*-

from flask import Blueprint

bpResume = Blueprint('bpResume', __name__)

from . import views_JProfile, views_JExperience