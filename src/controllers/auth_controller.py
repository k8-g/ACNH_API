from datetime import timedelta

from flask import Blueprint, request
from sqlalchemy.exc import IntegrityError
from psycopg2 import errorcodes
from flask_jwt_extended import create_access_token

from init import db, bcrypt, jwt
from models.user import User, user_schema, UserSchema
# from models.island import Island
# from schemas.island import island_schema, IslandSchema


# Added url_prefix /auth
auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


# @auth_bp.route('/register', methods=['POST'])
# def register_user():
#     try:
#         # get the data from the body of the request
#         body_data = IslandSchema().load(request.get_json())

#         # create an instance of the Island model
#         user = Island(
#             name_of_island=body_data.get("name_of_island"),
#             owner_of_island=body_data.get("owner_of_island")
#             )
#         # extract the password from the body
#         password = body_data.get("password")

#         # hash the password
#         if password:
#             user.password = bcrypt.generate_password_hash(password).decode("utf-8")

@auth_bp.route('/register', methods=['POST'])
def register_user():
    try:
        # get the data from the body of the request
        body_data = request.get_json()

        # create an instance of the Island model
        user = User(
            name=body_data.get("name"),
            email=body_data.get("email")
            )
        # extract the password from the body
        password = body_data.get("password")

        # hash the password
        if password:
            user.password = bcrypt.generate_password_hash(password).decode("utf-8")


        # data = request.get_json()
        # owner_of_island = data.get('owner_of_island')
        # password = data.get('password')
        # name_of_island = data.get('name_of_island')
        # is_admin = data.get('is_admin', False)

        # if Island.query.filter_by(owner_of_island=owner_of_island).first():
        #     return {"message": "User already exists"}, 400

        # user = Island(
        #     name_of_island=name_of_island,
        #     owner_of_island=owner_of_island,
        #     password=bcrypt.generate_password_hash(password).decode('utf-8'),
        #     is_admin=is_admin
        # )
        db.session.add(user)
        db.session.commit()

        return user_schema.dump(user), 201
    except IntegrityError as err:
        if err.orig.pgcode == errorcodes.NOT_NULL_VIOLATION:
            return {"error": f"Missing information; {err.orig.diag.column_name} is required"}, 409
        if err.orig.pgcode == errorcodes.UNIQUE_VIOLATION:
            return {"error": "Email address already in use"}, 409


@auth_bp.route('/login', methods=['POST'])
def login_user():
    # get the data from the body of the request
    body_data = request.get_json()
    # owner_of_island = data.get('owner_of_island')
    # password = data.get('password')

    # find the user/island in DB with that owner name
    stmt = db.select(User).filter_by(email=body_data.get("email"))
    user = db.session.scalar(stmt)

    # user = User.query.filter_by(name=name).first()
    # if user exists and password matches
    # if user and bcrypt.check_password_hash(user.password, password):
    if user and bcrypt.check_password_hash(user.password, body_data.get("password")):
        # create jwt
        # token = create_access_token(identity=str({'user_id': user.id, 'name': user.name}), expires_delta=timedelta(days=1))
        token = create_access_token(identity=str(user.id), expires_delta=timedelta(days=1))
        return {"name": user.name, "email": user.email, "id": user.id, "is_admin": user.is_admin, "token": token}, 200
    else:
        # respond back with an error message
        return {"error": "Incorrect email or password."}, 401