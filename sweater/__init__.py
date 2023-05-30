from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
manager = LoginManager(app)
app.secret_key = 'abrikosi ne lubyat kogda ih edyat' # НЕ ПАЛИ ЭТО НИГДЕ!!!!

from sweater import models, routes

db.create_all()