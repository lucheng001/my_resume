# -*- coding: utf-8 -*-

from flask import render_template, url_for, redirect
from . import bpMain

@bpMain.route('/')
def index():
    return redirect(url_for('bpShow.info'))

@bpMain.app_errorhandler(404)
def error404(error):
    return render_template('main/404.html'), 404

@bpMain.app_errorhandler(403)
def error403(error):
    return render_template('main/403.html'), 403

@bpMain.app_errorhandler(500)
def error500(error):
    return render_template('main/500.html'), 500