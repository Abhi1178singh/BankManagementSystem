from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import jwt_required, get_jwt,get_jwt_identity
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import LoanModel
from schemas import LoanSchema

blp = Blueprint("Loans", "loans", description="Operations on loans")

@blp.route("/loanWithId")
class ItemList(MethodView):
    @jwt_required()
    @blp.response(200, LoanSchema(many=True))
    def get(self):
        cust_id = get_jwt_identity()
        return LoanModel.query.filter(LoanModel.customer_id == cust_id)

@blp.route("/loan")
class ItemList(MethodView):
    @jwt_required()
    @blp.response(200, LoanSchema(many=True))
    def get(self):
        return LoanModel.query.all()

    @jwt_required()
    @blp.arguments(LoanSchema)
    @blp.response(201, LoanSchema)
    def post(self, loan_data):

        customer_id =  get_jwt_identity()
        loan_data['customer_id'] = get_jwt_identity()
        loan = LoanModel(**loan_data)

        try:
            db.session.add(loan)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the loan.")

        return loan
