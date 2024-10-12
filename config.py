import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///flavorfolio.db'  
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or '4a28ae9b1342b9ea1d411393c9b19242d405eeb673816fe3'
