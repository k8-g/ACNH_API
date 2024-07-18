from datetime import timedelta
from flask import Blueprint, request
from sqlalchemy.exc import IntegrityError
from psycopg2 import errorcodes
from init import db, bcrypt, jwt
from models.island import Island
from schemas.island import island_schema, IslandSchema
from flask_jwt_extended import create_access_token

auth_bp = Blueprint("auth", __name__,)

@auth_bp.route('/register', methods=['POST'])
def register_user():
    try:
        # get the data from the body of the request
        body_data = IslandSchema().load(request.get_json())

        # create an instance of the Island model
        user = Island(
            name_of_island=body_data.get("name_of_island"),
            owner_of_island=body_data.get("owner_of_island")
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

        return island_schema.dump(user), 201
    except IntegrityError as err:
        if err.orig.pgcode == errorcodes.NOT_NULL_VIOLATION:
            return {"error": f"Missing info; {err.orig.diag.column_name} is required"}, 409
        if err.orig.pgcode == errorcodes.UNIQUE_VIOLATION:
            return {"error": "Owner name already in use"}, 409

@auth_bp.route('/login', methods=['POST'])
def login():
    # get the data from the body of the request
    data = request.get_json()
    owner_of_island = data.get('owner_of_island')
    password = data.get('password')

    # find the user/island in DB with that owner name
    stmt = db.select(Island).filter_by(owner_of_island=data.get("owner_of_island"))
    user = db.session.scalar(stmt)

    user = Island.query.filter_by(owner_of_island=owner_of_island).first()
    # if user exists and password matches
    if user and bcrypt.check_password_hash(user.password, password):
        # create jwt
        token = create_access_token(identity=str({'owner_of_island': user.owner_of_island}), expires_delta=timedelta(days=1))
        return {"owner_of_island": user.owner_of_island, "is_admin": user.is_admin, "token": token}, 200
    else:
        # respond back with an error message
        return {"error": "Incorrect password or owner name."}, 401