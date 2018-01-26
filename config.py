#config.py

import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = os.environ['SECRET_KEY']
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
WTF_CSRF_ENABLED = True

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'data-test.sqlite')
SQLALCHEMY_MIGRATE_REPO = os.path.join(BASE_DIR, 'db_repository')

