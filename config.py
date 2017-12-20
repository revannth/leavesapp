#config.py

import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
	SECRET_KEY = os.environ.get('SECRET_KEY')
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True
	WTF_CSRF_ENABLED = True
	def init_app(app):
		pass

class DevelopmentConfig(Config):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'data-dev.sqlite')

class TestingConfig(Config): 
	TESTING = True
	SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
	'sqlite:///' + os.path.join(BASE_DIR, 'data-test.sqlite')

config = {
	'development':DevelopmentConfig,
	'testing':TestingConfig,
	'default':DevelopmentConfig

}