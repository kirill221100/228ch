import os
from os.path import join, dirname, realpath

current_path = os.path.dirname(os.path.realpath(__file__))
db_path = os.environ.get('URI')

class Config:
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOAD_FOLDER = 'app/static/images/'
    BASIC_AUTH_PASSWORD = os.environ.get('BASIC_AUTH_PASSWORD')
    BASIC_AUTH_USERNAME = os.environ.get('BASIC_AUTH_USERNAME')
    API_KEY = os.environ.get('API_KEY')
    API_SECRET = os.environ.get('API_SECRET')
    SQLALCHEMY_DATABASE_URI = db_path
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SEND_FILE_MAX_AGE_DEFAULT = 0
    PERMANENT_SESSION_LIFETIME = 2678400