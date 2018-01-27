#__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
config_name = 'testing'
app.config.from_object('config')



db = SQLAlchemy(app)

from app import views,models

