# *- coding:utf-8 -*

from flask import Blueprint

bpShow = Blueprint('bpShow', __name__)

from . import views