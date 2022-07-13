from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize application
app = Flask(__name__) # __name__ is just the name of the module: __main__
app.config['SECRET_KEY'] = '08c01258226aaa63532af39e9b8acc72'

# Configure application with database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/dev-bgda-db.db'
db = SQLAlchemy(app)
# MySQL database URI line
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://etsu_conn:vIper sp1/t pretzelz@localhost/bgda_db'

# Import routes below intialization of app to avoid circular imports
from app import routes