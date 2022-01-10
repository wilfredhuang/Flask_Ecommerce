from flask import render_template, request, jsonify, flash, redirect, \
    url_for
from flask_mysqldb import MySQL
from webapp.models.product import Product
from webapp.models.user import User
from webapp.forms.forms import *
from webapp import app, db, ma, product_schema, products_schema, mysql, bcrypt

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


# route functions

# External styling, we need to import render_template first


# Adding different routes for the same webpage
@app.route('/')
@app.route('/home')
def home_page():
    print(app.config['SECRET_KEY'])
    return render_template('home.html')

# Static Route example


@app.route('/about')
def about_page():
    return '<h1> About Page </h1>'

# Dynamic Route example


@app.route('/about/<username>')
def about_page_dynamic(username):
    return f'<p> This is the page of {username}  </p>'

# Sending data to templates


@app.route('/market')
def market_page():

    # Items list of dictionaries

    items = [
        {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
        {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
        {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
    ]
    return render_template('market.html', items=items)

# Create/insert user example using Flask-MySQLdb which is an extension to access mysql dbs
# The operation will still be successful even with marshmallow and sqlalchemy variables active

"""
@app.route('/adduser', methods=['GET', 'POST'])
def adduser_page():
#     With vanilla mysql module
#     # We need to use control flow when handling different types of request method on the same endpoint
    if request.method == 'POST':
        # fetch form data
        userDetails = request.form

        # Get these values from 'name' attr of each input in the form
        email = userDetails['form_email']
        password = userDetails['form_password']

        # Create cursor, to execute queries (sql statements)
        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO users(email, password) VALUES(%s, %s)", (email, password))

        # Commit these changes to database (required!)
        mysql.connection.commit()

        # Close cursor after operation done

        cur.close()

        return 'success'

    return render_template('adduser.html')
"""

@app.route("/register", methods=['GET', 'POST'])
def register():
    # if current_user.is_authenticated:
    #     return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


# CRUD products API example using flask-marshmallow + flask-sqlalchemy
# flask-sqlalchemy is an object relational mapper (ORM) that provides layer of abstraction between db and the developer
# by allowing us to perform db operations by python code rather than plain sql like in flask-mysql module


@app.route('/product', methods=['POST'])
def create_product():
    new_product = Product("Product A", "This is product A", 100, 5)

    db.session.add(new_product)
    db.session.commit()

    return product_schema.jsonify(new_product)


# Get All Products
@app.route('/product', methods=['GET'])
def get_products():
  all_products = Product.query.all()
  result = products_schema.dump(all_products)
  return jsonify(result)

# Get Single Products
@app.route('/product/<id>', methods=['GET'])
def get_product(id):
  product = Product.query.get(id)
  return product_schema.jsonify(product)


# Update a Product
@app.route('/product/<id>', methods=['PUT'])
def update_product(id):
  product = Product.query.get(id)

  name = request.json['name']
  description = request.json['description']
  price = request.json['price']
  qty = request.json['qty']

  product.name = name
  product.description = description
  product.price = price
  product.qty = qty

  db.session.commit()

  return product_schema.jsonify(product)

# Delete Product
@app.route('/product/<id>', methods=['DELETE'])
def delete_product(id):
  product = Product.query.get(id)
  db.session.delete(product)
  db.session.commit()

  return product_schema.jsonify(product)