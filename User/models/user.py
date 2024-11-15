from db import db


class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    address = db.Column(db.String(80), nullable=False)
    state = db.Column(db.String(80), nullable=False)
    country = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    pan = db.Column(db.String(80), nullable=False)
    contact_no = db.Column(db.Integer, nullable=False)
    dob = db.Column(db.Date, nullable=False)
    account_type = db.Column(db.String(80), nullable=False)
    

