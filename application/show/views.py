# -*- coding: utf-8 -*-

from flask import render_template, url_for, redirect
from playhouse.flask_utils import get_object_or_404
from flask_login import current_user
from ..models import User, Project, Diary
from . import bpShow

@bpShow.route('/home')
def home():
    return render_template('show/home.html')

@bpShow.route('/info')
def info():
    try:
        me = User.get(User.id == current_user.id)
        if me:
            user = me
    except:
        user = User.get(User.username == 'lc')

    query = Project.select().join(User).where(User.id == user.id)
    projects = [row for row in query]

    return render_template('show/info.html', user=user, projects=projects)

@bpShow.route('/gallery')
def gallery():
    try:
        me = User.get(User.id == current_user.id)
        if me:
            user = me
    except:
        user = User.get(User.username == 'lc')

    query = Diary.select().join(User).where(User.id == user.id)
    diarys = query

    return render_template('show/gallery.html', user=user, diarys=diarys)

@bpShow.route('/contact')
def contact():
    return render_template('show/contact.html')