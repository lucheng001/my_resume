# -*- coding: utf-8 -*-

from flask_wtf import Form
from wtforms import TextAreaField, SelectField, StringField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField

class addJobProfileForm(Form):
    job = StringField(
        u'目标职能',
        validators=[
            DataRequired(u'目标职能不能为空')
        ]
    )

    jobType = StringField(
        u'工作类型',
        validators=[
            DataRequired(u'工作类型不能为空')
        ]
    )

    salary = StringField(
        u'期望薪资',
        validators=[
            DataRequired(u'期望薪资不能为空')
        ]
    )

class addJobProfileDataForm(Form):
    job = StringField(
        u'目标职能',
        validators=[
            DataRequired(u'目标职能不能为空')
        ]
    )

    jobType = StringField(
        u'工作类型',
        validators=[
            DataRequired(u'工作类型不能为空')
        ]
    )

    salary = StringField(
        u'期望薪资',
        validators=[
            DataRequired(u'期望薪资不能为空')
        ]
    )

    user = SelectField(
        u'用户',
        validators=[
            DataRequired(u'用户不能为空')
        ]
    )

class EditJobProfile(Form):
    job = StringField(u'目标职能')

    jobType = TextAreaField(u'工作类型')

    salary = StringField(u'期望薪资')