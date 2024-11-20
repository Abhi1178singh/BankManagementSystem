from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import (
    create_access_token,
    get_jwt,
    jwt_required,
)
from passlib.hash import pbkdf2_sha256

from db import db
from models import UserModel
from schemas import UserSchema,LoginSchema
from blocklist import BLOCKLIST


blp = Blueprint("Users", "users", description="Operations on users")


@blp.route("/register")
class UserRegister(MethodView):
    @blp.arguments(UserSchema)
    def post(self, user_data):
        if UserModel.query.filter(UserModel.username == user_data["username"]).first():
            abort(409, message="A user with that username already exists.")
        user = UserModel(
            username=user_data["username"],
            password=pbkdf2_sha256.hash(user_data["password"]),
            email = user_data["email"],
            address = user_data["address"],
            state = user_data["state"],
            country = user_data["country"],
            dob = user_data["dob"],
            contact_no = user_data["contact_no"],
            account_type = user_data["account_type"],
            pan = user_data["pan"]
        )
        db.session.add(user)
        db.session.commit()

        return {"message": "User created successfully."}, 201


@blp.route("/login")
class UserLogin(MethodView):
    @blp.arguments(LoginSchema)
    def post(self, user_data):
        user = UserModel.query.filter(
            UserModel.username == user_data["username"]
        ).first()

        if user and pbkdf2_sha256.verify(user_data["password"], user.password):
            access_token = create_access_token(identity=user.id, fresh=True)
            return {"access_token": access_token}, 200

        abort(401, message="Invalid credentials.")


@blp.route("/logout")
class UserLogout(MethodView):
    @jwt_required()
    def post(self):
        jti = get_jwt()["jti"]
        BLOCKLIST.add(jti)
        return {"message": "Successfully logged out"}, 200

@blp.route("/user")
class User(MethodView):
    @jwt_required()
    @blp.response(200, UserSchema)
    @blp.response(200, UserSchema(many=True))
    def get(self):
        return UserModel.query.all()


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


@blp.route("/user/<int:user_id>")
class User(MethodView):
    @blp.response(200, UserSchema)
    def get(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        return user
        
    @jwt_required()
    def delete(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return {"message": "User deleted."}, 200
