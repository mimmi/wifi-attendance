from app import db, login
from sqlalchemy.sql import func
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

def new_registration():
    return (db.session.query(User).first() is None)
    
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Staff(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    staff_id = db.Column(db.Integer, index=True, unique=True)
    name = db.Column(db.String(128), index=True, unique=True)
    ip = db.Column(db.String(15), index=True, unique=True)
    port = db.Column(db.Integer, index=False, unique=False)
    mac = db.Column(db.String(17), index=True, unique=True)
    hostname = db.Column(db.String(32), index=True, unique=True)
    method = db.Column(db.String(5), index=True, unique=False)
    # PING, ARP, PORT

    def __repr__(self):
        return '<Staff {}>'.format(self.name)