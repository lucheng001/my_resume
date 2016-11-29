# -*- coding: utf-8 -*-

from flask import render_template, url_for, redirect, flash
from flask_login import current_user, login_required
from playhouse.flask_utils import get_object_or_404
from ..models import JobProfile, User
from .forms_JProfile import addJobProfileForm, addJobProfileDataForm, EditJobProfile
from . import bpResume

@bpResume.route('/addJProfile', methods=['GET', 'POST'])
@login_required
def addJProfile():
    form = addJobProfileForm()
    if form.validate_on_submit():
        jp = JobProfile.select().join(User).where(User.id == current_user.id)
        if jp:
            return redirect(url_for('bpShow.resume'))
        query = (User.select(User.id, User.chinesename))
        users = [row for row in query]
        jProfileForm = addJobProfileDataForm()
        jProfileDic = dict(
            job = form.job.data,
            jobType = form.jobType.data,
            salary = form.salary.data,
            user = current_user.id
        )
        jProfileForm.user.choices = [(user.id, user.chinesename) for user in users]
        jProfileForm.user.data = jProfileDic['user']
        jProfileForm.job = jProfileDic['job']
        jProfileForm.jobType = jProfileDic['jobType']
        jProfileForm.salary = jProfileDic['salary']

        if not jProfileForm.validate():
            flash(u'添加失败!', 'error')
            return redirect(url_for('bpShow.resume'))
        JobProfile.create(**jProfileDic)
        return redirect(url_for('bpShow.resume'))
    return render_template('show/resume/addJobProfile.html', form =form)

@bpResume.route('/editJProfile/<int:jobProfileId>', methods=['GET', 'POST'])
@login_required
def editJProfile(jobProfileId):
    form = EditJobProfile()
    if form.validate_on_submit():
        jobProfile = get_object_or_404(JobProfile, JobProfile.id == jobProfileId)
        if form.job.data:
            jobProfile.job = form.job.data
        if form.jobType.data:
            jobProfile.jobType = form.jobType.data
        if form.salary.data:
            jobProfile.salary = form.salary.data
        jobProfile.save()
        return redirect(url_for('bpShow.resume'))
    return render_template('show/resume/editJobProfile.html', form=form, jobProfileId=jobProfileId)