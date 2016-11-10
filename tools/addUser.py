# -*- coding: utf-8 -*-

from werkzeug.security import generate_password_hash
from application import create_app
from application.extensions import db
from application.constants import CntRoles

grop1 = [
    ('admin', '管理员'),
    ('lc', '鲁成')
]

def addUsers():
    app = create_app('default')
    from application.models import User
    database = db.database

    password = app.config['DEFAULT_PASSWORD']

    database.connect()

    for user in grop1:
        User.create(
            username = user[0],
            chinesename = user[1],
            role = CntRoles.ADMIN.label,
            permission=CntRoles.getRolePermission(CntRoles.ADMIN.label),
            aboutMe = "Love Python and ArchLinux, good at kickboxing, swimming and like rock climbing."
        )

    database.close()

if __name__ == '__main__':
    addUsers()