# -*- coding: utf-8 -*-

import os
import shutil
from flask import render_template, redirect, url_for, flash, current_app, send_from_directory
from flask_login import login_required
from werkzeug.utils import secure_filename
from playhouse.flask_utils import get_object_or_404
from urllib import quote
from ..models import Project
from .forms import uploadFileForm
from . import bpProject

@bpProject.route('/upload/<int:projectId>', methods=['GET', 'POST'])
@login_required
def upload(projectId):
    form = uploadFileForm()
    project = get_object_or_404(Project, Project.id == projectId)
    if form.validate_on_submit():
        fName = u'utitled'
        fExtension = u'unknown'
        secureFileName = secure_filename(form.file.data.filename)
        if secureFileName:
            res = secureFileName.rsplit('.', 1)
            if len(res) == 2:
                fName = res[0]
                fExtension = res[1]
            else:
                fName = ''
                fExtension = res[0]

        filePath = os.path.join(current_app.config['APP_PROJECT_DIR'], project.getFilePath())
        patter = u'项目总结.{}'
        fileName = patter.format(fExtension)
        form.file.data.save(os.path.join(filePath, fileName))
        if os.path.isfile(os.path.join(filePath, u'项目总结.未交')):
            os.remove(os.path.join(filePath, u'项目总结.未交'))
        flash(u'文件上传成功','success')
    return render_template('/show/project/uploadFile.html', form=form, project=project)

@bpProject.route('/download/<int:projectId>', methods=['GET', 'POST'])
def download(projectId):
    project = get_object_or_404(Project, Project.id == projectId)
    filePath = os.path.join(current_app.config['APP_PROJECT_DIR'], project.getFilePath())
    archiveName = project.getProjectName()
    archivePath = os.path.join(current_app.config['APP_ARCHIVE_DIR'], archiveName)
    shutil.make_archive(archivePath, 'zip', filePath)
    zipName = u'{}.zip'.format(archiveName)
    encodeZipName = quote(zipName.encode('UTF-8'))
    zipPath = current_app.config['APP_ARCHIVE_DIR']
    return send_from_directory(zipPath, zipName, as_attachment=True, attachment_filename=encodeZipName)