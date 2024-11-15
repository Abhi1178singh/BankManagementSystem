from db import db

class LoanModel(db.Model):
    __tablename__ ="loans"

    id = db.Column(db.Integer, primary_key=True)
    loan_type = db.Column(db.String(80), nullable=False)
    loan_amount = db.Column(db.Float(precision=2), nullable=False)
    date = db.Column(db.Date, nullable=False)
    rate_of_interest = db.Column(db.Float(precision=2), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    customer_id = db.Column(
        db.Integer, db.ForeignKey("users.id"), unique=False, nullable=False
    )