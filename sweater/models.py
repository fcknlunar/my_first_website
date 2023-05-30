from datetime import datetime
from sweater import db, manager
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(16), nullable=False)
    password = db.Column(db.String(16), nullable=False)
    regdate = db.Column(db.DateTime, default=datetime.utcnow)


@manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
