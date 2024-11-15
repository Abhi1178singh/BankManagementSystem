from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import (
    create_access_token,
    get_jwt,
    jwt_required,
    get_jwt_identity
)
from passlib.hash import pbkdf2_sha256

from db import db
from models import UserModel
from schemas import UserSchema
from blocklist import BLOCKLIST


blp = Blueprint("Update Users", "users", description="Operations on update users")



@blp.route("/user")
class User(MethodView):
    @jwt_required()
    @blp.arguments(UserSchema)
    @blp.response(200, UserSchema)
    def put(self, user_data):
        cust_id = get_jwt_identity()
        user = UserModel.query.get_or_404(cust_id)
        
        user.id = cust_id
        user.username = user_data["username"]
        user.password = pbkdf2_sha256.hash(user_data["password"])
        user.email = user_data["email"]
        user.address = user_data["address"]
        user.state = user_data["state"]
        user.country = user_data["country"]
        user.dob = user_data["dob"]
        user.contact_no = user_data["contact_no"]
        user.account_type = user_data["account_type"]
        user.pan = user_data["pan"]
        
        db.session.add(user)
        db.session.commit()

        return user

