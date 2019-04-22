from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .creditals import *

app = Flask(__name__)
app.config.from_object('config')
engine = create_engine(
    'mysql://{}:{}@{}/{}'.format(
        MYSQL_USER, MYSQL_PASSWORD, MYSQL_SERVER, MYSQL_DATABASE))
session = sessionmaker(bind=engine)
session = session()
from app import views
