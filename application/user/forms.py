# -*- coding: utf-8 -*-

from flask_wtf import Form
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Length

class ChangePasswordForm(Form):
    oldPassword = PasswordField(
        u'密码',
        validators=[
            DataRequired(u'密码不能为空'),
            Length(6, 20, u'密码为6~20位')
        ]
    )

    newPassword = PasswordField(
        u'密码',
        validators=[
            DataRequired(u'密码不能为空'),
            Length(6, 20, u'密码为6~20位')
        ]
    )

class ResetProfileForm(Form):
    chinesename = StringField(u'姓名')

    aboutMe = TextAreaField(u'About Me')

    tel = StringField(u'电话')

    email = StringField(u'Email')