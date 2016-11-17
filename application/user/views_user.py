# -*- coding: utf-8 -*-

from flask_login import login_required, current_user
from flask import render_template, redirect, request, url_for, flash
from playhouse.flask_utils import get_object_or_404
from werkzeug.security import check_password_hash, generate_password_hash
from ..models import User
from .forms import ChangePasswordForm
from . import bpUser

@bpUser.route('/changePassword', methods=['GET', 'POST'])
@login_required
def changePassword():
    form = ChangePasswordForm()
    if form.validate_on_submit():
        user = get_object_or_404(User, User.id == current_user.id)
        if user and check_password_hash(user.passwordHash, form.oldPassword.data):
            newPasswordHash = generate_password_hash(form.newPassword.data)
            user.passwordHash = newPasswordHash
            user.save()
            return redirect(url_for('bpShow.info'))
        else:
            flash('Old password not match!', 'error')
            return redirect(url_for('bpUser.changePassword'))
    return render_template('user/changePassword.html', form=form)