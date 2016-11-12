# -*- coding: utf-8 -*-

from flask import render_template, redirect, url_for, flash
from flask_login import  current_user, login_user
from ..models import User
from . import bpAuth

@bpAuth.route('/login')
def login():
    pass

@bpAuth.route('/test')
def test():
    query = User.select(User.id, User.chinesename)
    print 'test'
    names = [user.chinesename for user in query]
    for user in query:
        print user.chinesename
    u = User.get(User.username == 'lc')
    print u.chinesename
    return u.chinesename