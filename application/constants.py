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

class CntAllowExtensions(object):
    TEXT_TYPE = ['txt', 'pdf']
    MSOFFICE_TYPE = ['doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx']
    IMAGE_TYPE = ['bmp', 'gif', 'jpg', 'jpeg', 'png', 'svg']
    COMPRESS_TYPE = ['7z', 'rar', 'zip', 'bz2', 'gz', 'tar']

    _extensions = TEXT_TYPE + MSOFFICE_TYPE + IMAGE_TYPE + COMPRESS_TYPE
    _obects = list(set(_extensions + [ext.upper() for ext in _extensions]))

    choices = _obects
    labels = _obects