# -*- coding: utf-8 -*-

from flask import  Blueprint

bpProject = Blueprint('bpProject', __name__)

from . import views