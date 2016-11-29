# -*- coding: utf-8 -*-

from flask_wtf import Form
from wtforms import TextAreaField, SelectField, StringField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField

class addJobExperienceForm(Form):
    theme = StringField(
        u'主题',
        validators=[
            DataRequired(u'主题不能为空')
        ]
    )

    time = StringField(
        u'时间',
        validators=[
            DataRequired(u'时间不能为空')
        ]
    )

    location = StringField(
        u'地点',
        validators=[
            DataRequired(u'地点不能为空')
        ]
    )

    body = TextAreaField(
        u'描述',
        validators=[
            DataRequired(u'请描述您的经历')
        ]
    )

class addJobExperienceDataForm(Form):
    theme = StringField(
        u'主题',
        validators=[
            DataRequired(u'主题不能为空')
        ]
    )

    time = StringField(
        u'时间',
        validators=[
            DataRequired(u'时间不能为空')
        ]
    )

    location = StringField(
        u'地点',
        validators=[
            DataRequired(u'地点不能为空')
        ]
    )

    body = TextAreaField(
        u'描述',
        validators=[
            DataRequired(u'请描述您的经历')
        ]
    )

    user = SelectField(
        u'用户',
        validators=[
            DataRequired(u'用户不能为空')
        ]
    )