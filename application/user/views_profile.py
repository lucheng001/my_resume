# -*- coding: utf-8 -*-

from flask import render_template, redirect, flash, url_for
from flask_login import login_required, current_user
from playhouse.flask_utils import get_object_or_404
from ..models import User
from .forms import ResetProfileForm
from . import bpUser

@bpUser.route('/resetProfile', methods=['GET', 'Post'])
@login_required
def resetProfile():
    form = ResetProfileForm()
    if form.validate_on_submit():
        user = get_object_or_404(User, User.id == current_user.id)
        if form.chinesename.data:
            user.chinesename = form.chinesename.data
        if form.aboutMe.data:
            user.aboutMe = form.aboutMe.data
        if form.tel.data:
            user.tel = form.tel.data
        if form.email.data:
            user.email = form.email.data
        user.save()
        return redirect(url_for('bpShow.info'))
    return render_template('user/resetProfile.html', form=form)