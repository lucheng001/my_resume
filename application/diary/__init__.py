# -*- coding: utf-8 -*-

from flask import Blueprint

bpDiary = Blueprint('bpDiary', __name__)

from . import views