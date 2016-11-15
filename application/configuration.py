# -*- coding: utf-8 -*-

import os


class Configuration(object):
    DATABASE = 'postgresql://lc:LC1006115980@localhost:5432/wolfsly'
    DEFAULT_PASSWORD = '1a2b3c4d'
    SECRET_KEY = '1000$CuRs6Mjx$'
    APP_DIR = os.path.abspath(os.path.dirname(__file__))
    BASE_DIR = os.path.abspath(os.path.dirname(APP_DIR))
    APP_LOG_DIR = os.path.join(BASE_DIR, 'logs')
    APP_LOG_INFO = os.path.join(APP_LOG_DIR, 'info.app.log')
    APP_LOG_ERROR = os.path.join(APP_LOG_DIR, 'error.app.log')
    APP_LOG_SIZE = 4 * 1024 * 1024
    APP_LOG_FORMATTER = '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'

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