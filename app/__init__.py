#__init__.py

from flask import Flask
from config import config
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)
config_name = 'development'
app.config.from_object(config[config_name])

db = SQLAlchemy(app)

from app import views,models

