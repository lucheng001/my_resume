# -*- coding: utf-8 -*-

import os
import re
import shutil
from flask import render_template, redirect, url_for, flash, current_app, abort
from flask_login import login_required, current_user
from ..models import User, Project
from .forms import addProjectDataForm, addProjectForm
from . import bpProject

@bpProject.route('/add', methods=['GET', 'POST'])
@login_required
def addProject():
    form = addProjectDataForm()
    if form.validate_on_submit():
        query = (User.select(User.id, User.chinesename))
        authors = [row for row in query]

        lines = form.projectData.data.splitlines()
        badData = []
        goodData = []
        for line in lines:
            data1 = line.split(',')
            if len(data1)!=2:
                badData.append(line)
                continue

            data2 = [re.sub(u'[\s+]', u'', d) for d in data1]
            data3 = [re.sub(u'[()]', u'', d) for d in data2]
            data4 = [re.sub(u'[ () ]', u'', d) for d in data3]
            data = [re.sub(u'[_]', u'', d) for d in data4]
            projectName, authorName = data

            if not current_user.chinesename == authorName:
                badData.append(line)
                continue

            authorId = 0
            for author in authors:
                if author.chinesename == authorName:
                    authorId = author.id
                    break
            else:
                badData.append(line)
                continue

            projectDict = dict(
                name = projectName,
                author = authorId
            )

            projectForm = addProjectForm()
            projectForm.name.data = projectDict['name']
            projectForm.author.data = projectDict['author']

            if not projectForm.validate():
                badData.append(line)
                continue

            path1=u'{}'
            path2=u'{}'
            filePath = os.path.join(current_app.config['APP_PROJECT_DIR'],
                                    path1.format(authorName), path2.format(projectName))

            if os.path.isdir(filePath):
                badData.append(line)
                continue

            tplPath = current_app.config['APP_PROJECT_TPL']
            shutil.copytree(tplPath, filePath)

            Project.create(**projectDict)

            goodData.append(line)

        msg = (
            u'提交{}条数据,'
            u'成功{}条数据,'
            u'失败{}条数据.'
        )
        if badData:
            flash(msg.format(len(lines), len(goodData), len(badData)), 'error')
            return render_template('show/project/projectBadData.html', badData=badData)
        else:
            flash(msg.format(len(lines), len(goodData), len(badData)), 'success')
            return redirect(url_for('bpProject.addProject'))

    return render_template('show/project/addProject.html', form=form)