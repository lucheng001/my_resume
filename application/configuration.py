# -*- coding: utf-8 -*-

import os


class Configuration(object):

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