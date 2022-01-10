# FLASK CONFIG
from os import environ, path
from dotenv import load_dotenv

# Get the current folder that we are in
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config(object):
    DATABASE_URI = 'sqlite://:memory:'


class ProductionConfig(Config):
    ENV = "production"
    DEBUG = False
    SECRET_KEY = "SECRET_KEY_HERE"
    DATABASE_URI = 'mysql://user@localhost/foo'


class DevelopmentConfig(Config):
    ENV = "development"
    DEBUG = True
    SECRET_KEY = "SECRET_KEY_HERE"

    # # app.config["SQLACHEMY_DATABASE_URI"] = 'mysql://username:password@localhost/db_name'
    # DB for standard mysql module
    MYSQL_HOST = environ.get("MYSQL_HOST")
    MYSQL_USER = environ.get("MYSQL_USER")
    MYSQL_PASSWORD = environ.get("MYSQL_PASSWORD")
    MYSQL_DB = environ.get("MYSQL_DB")

    # DB for sqlalchemy
    SQLALCHEMY_DATABASE_URI = f"mysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    TESTING = True
