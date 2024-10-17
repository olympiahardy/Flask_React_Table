# This will contain the main configuration of the application
# When you install python packages use python3.13 -m pip install 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# This initialises the application
app = Flask(__name__)
# This disables an error that will allow us to send cross-origin requests to our app
CORS(app)

# Initialise the database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"
# Just disables tracking any modifications of the database
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# This creates an instance of the database and we pass our app that creates an instance that we can access the database
db = SQLAlchemy(app)