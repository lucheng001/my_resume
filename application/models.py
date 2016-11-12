# -*- coding: utf-8 -*-

import datetime
from peewee import *
from .constants import CntRoles
from .extensions import db

_all_ = ['User', 'Project', 'Model']

class User(Model):
    id = PrimaryKeyField()
    username = CharField(max_length=16, unique=True, index=True)
    chinesename = CharField(max_length=32, index=True)
    permission = IntegerField(default=0)
    sex = BooleanField(default=1)
    tel = CharField(index=True, null=True)
    email = CharField(max_length=50, null=True)
    aboutMe = TextField(null=True)
    role = CharField(max_length=32, index=True, choices=CntRoles.choices, default=CntRoles.USER.label)
    passwordHash = CharField(max_length=255)
    lastLoginTime = TimeField(default=datetime.datetime.min, formats='%Y-%m-%d %H:%M:%S')
    createTime = TimeField(default=datetime.datetime.now, formats='%Y-%m-%d %H:%M:%S')

    class Meta:
        database = db.database

class Project(Model):
    id = PrimaryKeyField()
    name = CharField(max_length=256, index=True)
    createTime = TimeField(default=datetime.datetime.now, formats='%Y-%m-%d %H:%M:%S')
    author = ForeignKeyField(User)

    class Meta:
        database = db.database

class Photo(Model):
    id = PrimaryKeyField()
    createTime = TimeField(default=datetime.datetime.now, formats='%Y-%m-%d %H:%M:%S')

    class Meta:
        database = db.database