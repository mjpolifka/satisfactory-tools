from satisfactory_tools import create_app

create_app()


"""
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.models import Ingredient

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

"""