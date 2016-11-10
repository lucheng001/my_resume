# -*- coding: utf-8 -*-

class CntPermission(object):
    NOPERMISSION = 0b000000
    NORMAL       = 0b000001
    ADMIN        = 0b000010

class _ADMIN(object):
    label = u'admin'
    name = u'管理员'
    permissions = (CntPermission.NOPERMISSION |
                   CntPermission.NORMAL |
                   CntPermission.ADMIN)

class _USER(object):
    label = u'user'
    name = u'用户'
    permissions = (CntPermission.NOPERMISSION |
                   CntPermission.NORMAL)

class _GUEST(object):
    label = u'guest'
    name = u'guest'
    permissions = (CntPermission.NOPERMISSION)

class CntRoles(object):
    ADMIN = _ADMIN
    USER = _USER
    GUEST = _GUEST

    _objects = [ADMIN, USER, GUEST]
    labels = [obj.label for obj in _objects]
    choices = [(obj.label, obj.name) for obj in _objects]
    _maps = dict(zip(labels, _objects))

    @classmethod
    def getRolePermission(cls, label):
        return cls._maps[label].permissions if label in CntRoles.labels else 0b0