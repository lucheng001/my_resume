# -*- coding: utf-8 -*-

from flask import render_template, url_for, redirect
from playhouse.flask_utils import get_object_or_404
from flask_login import current_user
from ..models import User, Project, Diary, JobProfile, JobExperience, ProjectExperience, ProjectStructure
from . import bpShow

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

@bpShow.route('/resume')
def resume():
    try:
        me = User.get(User.id == current_user.id)
        if me:
            user = me
    except:
        user = User.get(User.username == 'lc')
    query = JobProfile.select().join(User).where(User.id == user.id)
    jobProfiles = query

    query = JobExperience.select().join(User).where(User.id == user.id).order_by(JobExperience.id)
    jobExperiences = query

    query = ProjectExperience.select().join(User).where(User.id == user.id).order_by(ProjectExperience.id)
    projectExperiences = query

    query = ProjectStructure.select().join(User).where(User.id == user.id).order_by(ProjectStructure.id)
    projectStructures = query

    return render_template('show/resume.html', user=user, jobProfiles=jobProfiles, jobExperiences=jobExperiences, projectExperiences=projectExperiences, projectStructures=projectStructures)