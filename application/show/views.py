# -*- coding: utf-8 -*-

from flask import render_template, url_for, redirect
from playhouse.flask_utils import get_object_or_404
from flask_login import current_user
from ..models import User
from . import bpShow

@bpShow.route('/home')
def home():
    return render_template('show/home.html')

@bpShow.route('/info')
def info():
    try:
        me = get_object_or_404(User, User.id == current_user.id)
        if me:
            return render_template('show/info.html', user=me)
    except:
        user = User.get(User.username == 'lc')
    return render_template('show/info.html', user=user)

@bpShow.route('/gallery')
def gallery():
    return render_template('show/gallery.html')

@bpShow.route('/contact')
def contact():
    return render_template('show/contact.html')