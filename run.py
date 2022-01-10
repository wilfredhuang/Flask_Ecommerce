from webapp import app

# __name__ refers to the name of local python file we are working i.e (market.py)
if __name__ == "__main__":
    app.run(debug=True)
    print(app.config['SECRET_KEY'])
