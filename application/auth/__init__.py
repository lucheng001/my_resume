# -*- coding: utf-8 -*-

from flask import Blueprint

bpAuth = Blueprint('bpAuth', __name__)

from . import  views