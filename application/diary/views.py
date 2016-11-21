# -*- coding: utf-8 -*-

from flask import render_template, url_for, redirect, flash
from flask_login import current_user, login_required
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

        diaryDic = dict(
            body = form.diaryData.data,
            author = current_user.id
        )

        diaryForm = addDiaryDataForm()
        diaryForm.author.choices = [(author.id, author.chinesename) for author in authors]
        diaryForm.author.data = diaryDic['author']
        diaryForm.body.data = diaryDic['body']

        if not diaryForm.validate():
            flash(u'写入失败!', 'error')
            return redirect(url_for('bpShow.gallery'))

        Diary.create(**diaryDic)
        return redirect(url_for('bpShow.gallery'))
    return render_template('show/diary/addDiary.html', form=form)