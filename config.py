import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'minicontador-secret'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///minicontador.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
