# Flask_Ecommerce
Flask-based web application for practice!






# Resources

### Setting up the project
[Project set up in VS Code: See the docs here](https://code.visualstudio.com/docs/python/tutorial-flask)

1. Install virtual environment in root folder of project
2. Add your own .env file in root folder (sample .env file shown below)
3. Run the file in root directory with command `python run.py`
```
# Configure debug mode here (True / False), (auto enabled if FLASK_ENV is set to development)
# FLASK_DEBUG=1

# Configure the environment for (development/production/testing here)
FLASK_ENV = "development"

# Entry point for flask app, if we use a custom name aside from 'app', we need to configure this value
# FLASK_APP=app

# DATABASE_URL=sqlite:///development_database.db

# API key:
# API secret key:

PROD_SECRET_KEY = "production secret key!"
DEV_SECRET_KEY = "development secret key!"
PROD_DATABASE_URI = "prod.db"
DEV_DATABASE_URI = "dev.db"

MYSQL_HOST = "localhost"
MYSQL_USER = "db_user_name"
MYSQL_PASSWORD = "db_user_password"
MYSQL_DB = "schema_name"
```

### Module documentation

[ORM - SQL Alchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/changelog)\
[Marshmallow-SQLALCHEMY](https://marshmallow-sqlalchemy.readthedocs.io/en/latest/changelog.html#changelog)\
[MarshMallow](https://marshmallow.readthedocs.io/en/stable/changelog.html)\
[Flask-WTF](https://flask-wtf.readthedocs.io/en/1.0.x/install/)\
[Flask-login](https://flask-login.readthedocs.io/en/latest/#installation)\
[Flask-Bcrypt](https://flask-bcrypt.readthedocs.io/en/latest/)
