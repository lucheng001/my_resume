# -*- coding: utf-8 -*-

import os


class Configuration(object):
    DATABASE = 'postgresql://lc:LC1006115980@localhost:5432/wolfsly'
    DEFAULT_PASSWORD = '1a2b3c4d'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfiguration(Configuration):
    DEBUG = True


class TestingConfiguration(Configuration):
    TESTING = True


class ProductionConfiguration(Configuration):
    DEBUG = False
    TESTING = False


config = {
    'development': DevelopmentConfiguration,
    'testing': TestingConfiguration,
    'production': ProductionConfiguration,
    'default': DevelopmentConfiguration
}