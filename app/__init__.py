import os
from dotenv.main import dotenv_values
from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .creditals import *

app = Flask(__name__)
app.config.from_object('config')
project_root = os.path.join(os.path.dirname(__file__), '../')
config = dotenv_values(project_root + '.env') 

engine = create_engine(
    'mysql://{}:{}@{}/{}'.format(
        config['MYSQL_USER'],
        config['MYSQL_PASSWORD'],
        config['MYSQL_SERVER'],
        config['MYSQL_DATABASE']
    )
)
session = sessionmaker(bind=engine)
session = session()
from app import views
