# -*- coding: utf-8 -*-

from flask import render_template, redirect, url_for, flash, abort
from flask_login import login_required, current_user
from playhouse.flask_utils import get_object_or_404
from ..models import User, JobExperience
from .forms_JExperience import addJobExperienceForm, addJobExperienceDataForm
from . import bpResume

@bpResume.route('/addJExperience', methods=['GET', 'POST'])
@login_required
def addJExperience():
    form = addJobExperienceForm()
    if form.validate_on_submit():
        query = (User.select(User.id, User.chinesename))
        users = [row for row in query]
        jExperienceForm = addJobExperienceDataForm()
        jExperienceDic = dict(
            theme = form.theme.data,
            time = form.time.data,
            location = form.location.data,
            body = form.body.data,
            user = current_user.id
        )
        jExperienceForm.user.choices = [(user.id, user.chinesename) for user in users]
        jExperienceForm.user.data = jExperienceDic['user']
        jExperienceForm.theme.data = jExperienceDic['theme']
        jExperienceForm.time.data = jExperienceDic['time']
        jExperienceForm.location.data = jExperienceDic['location']
        jExperienceForm.body.data = jExperienceDic['body']
        if not jExperienceForm.validate():
            return redirect(url_for('bpShow.resume'))
        JobExperience.create(**jExperienceDic)
        return redirect(url_for('bpShow.resume'))
    return render_template('show/resume/addJobExperience.html', form=form)

@bpResume.route('/deleteJExperience/<int:jExperienceId>', methods=['GET', 'POST'])
@login_required
def deleteJExperience(jExperienceId):
    jobExperience = get_object_or_404(JobExperience, JobExperience.id == jExperienceId)
    if not current_user.id == jobExperience.user.id:
        abort(403)
    jobExperience.delete_instance()
    return redirect(url_for('bpShow.resume'))