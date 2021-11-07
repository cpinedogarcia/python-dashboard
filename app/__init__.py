from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

from app.models import Item
# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()

from app import dashboard, hello
