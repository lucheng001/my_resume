# -*- coding: utf-8 -*-

from flask_wtf import Form
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length

_all_=['addProjectDataForm', 'addProjectForm']

class addProjectDataForm(Form):
    projectData = TextAreaField(
        u'项目数据',
        validators=[
            DataRequired(u'项目数据不能为空')
        ]
    )

class addProjectForm(Form):
    name = StringField(
        u'项目名称',
        validators=[
            DataRequired(u'项目名称不能为空'),
            Length(1,200,u'名称为1到200字符')
        ]
    )

    author = StringField(
        u'项目负责人',
        validators=[
            DataRequired(u'项目负责人不能为空')
        ]
    )