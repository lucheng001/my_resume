# -*- coding: utf-8 -*-

import datetime
from flask import render_template, redirect, url_for, flash, request, current_app
from flask_login import  current_user, login_user, logout_user, login_required
from ..models import User
from .forms import LoginForm
from . import bpAuth

@bpAuth.route('/login', methods=['GET', 'POST'])
def login():
    nextUrl = request.args.get('next', None)
    form = LoginForm()
    if form.validate_on_submit():
        try:
            user = User.get(User.username == form.username.data)
        except:
            user = None
            msg = 'login failed, no such user:{0}'
            current_app.logger.warning(msg.format(form.username.data))
            flash('no such user', 'error')

        if user and user.verifyPassword(form.password.data):
            user.lastLoginTime = datetime.datetime.now()
            user.save()
            login_user(user)
            if form.password.data == current_app.config['DEFAULT_PASSWORD']:
                flash('Please change your password!','message')
                return redirect(url_for('bpUser.changePassword'))
            return redirect(url_for('bpShow.info'))

        elif user:
            msg = 'login failed, password not match, username:{0}'
            current_app.logger.warning(msg.format(form.username.data))
            flash('password not match')

    return  render_template('auth/login.html', form=form)

@bpAuth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('bpShow.info'))