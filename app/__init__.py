from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# Initialize application
app = Flask(__name__) # __name__ is just the name of the module: __main__
app.config['SECRET_KEY'] = '08c01258226aaa63532af39e9b8acc72'

# Configure application with database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/dev-bgda-db.db'
db = SQLAlchemy(app)
# MySQL database URI line
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://etsu_conn:vIper sp1/t pretzelz@localhost/bgda_db'

# Configure application with password encryption
bcrypt = Bcrypt(app)

# Configure application with Flask's login manager and direct users to login function for routes requiring authentication  
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'warning'

# Import routes below intialization of app to avoid circular imports
from app import routes