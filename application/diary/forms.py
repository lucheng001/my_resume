# -*- coding: utf-8 -*-

from flask_wtf import Form
from wtforms import TextAreaField, SelectField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField

_all_=['addProjectDataForm', 'addProjectForm']

class addDiaryForm(Form):
    diaryData = TextAreaField(
        u'日记',
        validators=[
            DataRequired(u'日记能为空')
        ]
    )

    photo = FileField(u'图片')

class addDiaryDataForm(Form):
    body = TextAreaField(
        u'日记内容',
        validators=[
            DataRequired(u'日记内容不能为空')
        ]
    )

    author = SelectField(
        u'作者',
        validators=[
            DataRequired(u'作者不能为空')
        ]
    )