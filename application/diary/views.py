# -*- coding: utf-8 -*-

import os
import shutil
from flask import render_template, url_for, redirect, flash, current_app, abort
from flask_login import current_user, login_required
from playhouse.flask_utils import get_object_or_404
from werkzeug.utils import secure_filename
from ..models import User, Diary
from .forms import addDiaryForm, addDiaryDataForm
from . import bpDiary

@bpDiary.route('/writeDairy', methods=['GET', 'POST'])
@login_required
def addDiary():
    form = addDiaryForm()
    if form.validate_on_submit():
        query = (User.select(User.id, User.chinesename))
        authors = [row for row in query]
        diaryForm = addDiaryDataForm()
        fExtension = u'unknown'
        secureFileName = secure_filename(form.photo.data.filename)

        if secureFileName:
            res = secureFileName.rsplit('.', 1)
            if len(res) == 2:
                fExtension = res[1]
            else:
                fExtension = res[0]

        if form.photo.data:
            diaryDic = dict(
                body=form.diaryData.data,
                author=current_user.id,
                havePhoto=1,
                fExtension=fExtension
            )
            photoName = u'{body}.{fExtension}'.format(**diaryDic)
            photoPath = current_app.config['APP_DIARY_PHOTO_DIR']
            form.photo.data.save(os.path.join(photoPath, photoName))
            diaryDic = dict(
                body=form.diaryData.data,
                author=current_user.id,
                havePhoto=1,
                fExtension=fExtension,
                photoURL=u'diaryPhoto/{}'.format(photoName)
            )
        else:
            diaryDic = dict(
                body=form.diaryData.data,
                author=current_user.id,
                havePhoto=0
            )


        diaryForm.author.choices = [(author.id, author.chinesename) for author in authors]
        diaryForm.author.data = diaryDic['author']
        diaryForm.body.data = diaryDic['body']

        if not diaryForm.validate():
            flash(u'写入失败!', 'error')
            return redirect(url_for('bpShow.gallery'))

        Diary.create(**diaryDic)
        return redirect(url_for('bpShow.gallery'))
    return render_template('show/diary/addDiary.html', form=form)

@bpDiary.route('/rmDiary/<int:diaryId>', methods=['GET'])
@login_required
def delectDiary(diaryId):
    diary = get_object_or_404(Diary, Diary.id == diaryId)
    if not current_user.id == diary.author.id:
        abort(403)

    photoPath = current_app.config['APP_STATIC_DIR']
    photoName = diary.photoURL
    filePath = os.path.join(photoPath, photoName)
    if os.path.isfile(filePath):
        os.remove(filePath)

    diary.delete_instance()
    return redirect(url_for('bpShow.gallery'))