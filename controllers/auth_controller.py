from flask import Blueprint, request
from init import db, bcrypt, jwt
from models.island import Island
from schemas.island import island_schema
from flask_jwt_extended import create_access_token

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    owner_of_island = data.get('owner_of_island')
    password = data.get('password')
    name_of_island = data.get('name_of_island')
    is_admin = data.get('is_admin', False)

    if Island.query.filter_by(owner_of_island=owner_of_island).first():
        return {"message": "User already exists"}, 400

    new_user = Island(
        name_of_island=name_of_island,
        owner_of_island=owner_of_island,
        password=bcrypt.generate_password_hash(password).decode('utf-8'),
        is_admin=is_admin
    )
    db.session.add(new_user)
    db.session.commit()

    return island_schema.dump(new_user), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    owner_of_island = data.get('owner_of_island')
    password = data.get('password')

    user = Island.query.filter_by(owner_of_island=owner_of_island).first()

    if user and bcrypt.check_password_hash(user.password, password):
        access_token = create_access_token(identity={'owner_of_island': user.owner_of_island, 'is_admin': user.is_admin})
        return {"access_token": access_token}, 200
    else:
        return {"message": "Incorrect password or name."}, 401