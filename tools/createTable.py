# -*- coding: utf-8 -*-

from application import create_app
from application.extensions import db


def createTables():
    app = create_app('default')
    from application.models import (User, Project, Photo, Diary, JobProfile, JobExperience, ProjectExperience, ProjectStructure)
    database = db.database
    database.connect()
    database.create_tables([User, Project, Photo, Diary, JobProfile, JobExperience, ProjectExperience, ProjectStructure])
    database.close()

if __name__ == '__main__':
    createTables()
