# Import Flask framework for our app, render_template for loading html pages
# request module for handling http request methods and jsonify to output dictionaries / array of dictionaries as json
# flask_mysqldb module to set up mysql database for the flask app
# import config.py file which will handle our configuration settings before running the app
# import os module to access environment variables located in .env that are important in determining our app's state when ran


from flask import Flask
from flask_mysqldb import MySQL
from flask_bcrypt import Bcrypt
import config
import os
#from models.product import Product, ProductSchema


from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from .routes.alternate_route import alternate_route

app = Flask(__name__)
configtype = config.ProductionConfig() if os.environ.get(
    'FLASK_ENV') == 'production' else config.DevelopmentConfig()
app.config.from_object(configtype)

# print(app.config)

bcrypt = Bcrypt(app)

# Init db (MySQL style)
mysql = MySQL(app)


# Init db (SQLAlchemy style)
db = SQLAlchemy(app)
# Init marshmallow
ma = Marshmallow(app)

# Register blueprint to access routes in alternate_route.py
app.register_blueprint(alternate_route)
from webapp.models.product import ProductSchema
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
# Important!: Ensure this import is at the end of the file after all variable are created and not at the top with the other imports
# Otherwise, we will not be able to use any routes
from webapp.routes import main_route