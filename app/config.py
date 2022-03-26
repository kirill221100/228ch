import os
from os.path import join, dirname, realpath

current_path = os.path.dirname(os.path.realpath(__file__))

db_path = 'postgresql://postgres:abudabi@127.0.0.1:5432/postgres'

class Config:
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOAD_FOLDER = join(dirname(realpath(__file__)), 'static/images/')
    BASIC_AUTH_PASSWORD = os.environ.get('BASIC_AUTH_PASSWORD')
    BASIC_AUTH_USERNAME = os.environ.get('BASIC_AUTH_USERNAME')
    SQLALCHEMY_DATABASE_URI = db_path
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SEND_FILE_MAX_AGE_DEFAULT = 0
    PERMANENT_SESSION_LIFETIME = 365