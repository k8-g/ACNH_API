from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from utils import authorise_as_admin
from models.villager import Villager
from schemas.villager import villager_schema, villagers_schema


# Create a blueprint
villager_bp = Blueprint('villager', __name__, url_prefix="/villagers")

# /villagers - GET - fetch all villagers - R
@villager_bp.route("/", methods=["GET"])
def get_all_villagers():
    # # Select all villagers and order them by their id in ascending order
    # stmt = db.select(Villager).order_by(Villager.id.asc())
    # stmt = db.select(Villager)
    # villagers = db.session.scalars(stmt)
    # # Return the list of villagers
    # return villagers_schema.dump(villagers)

# Get the name from query parameters if provided
    villager_name = request.args.get('name')
    # If a villager name is provided
    if villager_name:
        # fetch the villager by name
        stmt = db.select(Villager).filter_by(name=villager_name)
        villager = db.session.scalar(stmt)
        # If villager exists
        if villager:
            # return the villager data
            return villager_schema.dump(villager)
        # else
        else:
            # Return an error if villager is not found
            return {"error": f"Villager with name '{villager_name}' not found"}, 404
    else:
        # Select all villagers and order them by their id in ascending order
        stmt = db.select(Villager).order_by(Villager.id.asc())
        villagers = db.session.scalars(stmt)
        # Return the list of villagers
        return villagers_schema.dump(villagers)



# /villagers/<id> - GET - fetch a single villager - R
@villager_bp.route("/<int:villager_id>", methods=["GET"])
def get_villager(villager_id):
    # Select a villager by id
    stmt = db.select(Villager).filter_by(id=villager_id)
    villager = db.session.scalar(stmt)
    # If villager exists
    if villager:
        # return the villager data
        return villager_schema.dump(villager)
    # else
    else:
        # Return an error if villager is not found
        return {"error": f"Villager with id {villager_id} not found"}, 404 

# /villagers - POST - create a new villager
@villager_bp.route("/", methods=["POST"])
@jwt_required()
def create_villager():
    # check if user is admin or not
    is_admin = authorise_as_admin()
    # if not admin
    if not is_admin:
        # return error message
        return{"Error": "User is not authorised to perform this action."}, 403
    # Select a villager by id

    # Get the data from the body of the request
    body_data = request.get_json()
    # Get user id from JWT token
    user_id=get_jwt_identity()

    # island_id = body_data.get('island_id')
    # if not island_id:
    #     return {"error": "island_id is required"}, 400

    # Create a new villager instance
    villager = Villager(
        # id=body_data.get("id")
        name=body_data.get("name"),
        species=body_data.get("species"),
        gender=body_data.get("gender"),
        personality=body_data.get("personality"),
        birthday=body_data.get("birthday"),
        catchphrase=body_data.get("catchphrase"),
        hobbies=body_data.get("hobbies"),
        # user_id=get_jwt_identity()
        # user_id=user_id,
        # island_id=island_id
    )
    # Add and commit the villager to the database
    db.session.add(villager)
    db.session.commit()
    # Return the created villager
    return villager_schema.dump(villager)


    # new_villager = Villager(
    #     name=body_data['name'],
    #     species=body_data['species'],
    #     gender=body_data['gender'],
    #     personality=body_data['personality'],
    #     birthday=body_data['birthday'],
    #     catchphrase=body_data['catchphrase'],
    #     hobbies=body_data['hobbies'],
    #     # island_id=get_jwt_identity()
    # )
    # db.session.add(new_villager)
    # db.session.commit()
    # return villager_schema.dump(new_villager), 201

# /villagers/<id> - DELETE - delete a villager
@villager_bp.route("/<int:villager_id>", methods=["DELETE"])
@jwt_required()
def delete_villager(villager_id):
    # check if user is admin or not
    is_admin = authorise_as_admin()
    # if not admin
    if not is_admin:
        # return error message
        return{"Error": "User is not authorised to perform this action."}, 403
    # Select a villager by id
    stmt = db.select(Villager).filter_by(id=villager_id)
    villager = db.session.scalar(stmt)
    # If villager exists
    if villager:
        # delete the villager
        db.session.delete(villager)
        # commit to database
        db.session.commit()
        # return success message
        return {"message": f"Villager '{villager.name}, ID No. {villager_id}' deleted successfully"}
    # else
    else:
        # return error message
        return {"error": f"Villager with id {villager_id} not found"}, 404

# /villagers/<id> - PUT, PATCH - update a villager
@villager_bp.route("/<int:villager_id>",  methods=["PUT","PATCH"])
@jwt_required()
def update_villager(villager_id):

    # check if user is admin or not
    is_admin = authorise_as_admin()
    # if not admin
    if not is_admin:
        # return error message
        return{"Error": "User is not authorised to perform this action."}, 403
    
    # get the data from the body of the request
    body_data = request.get_json()

    # CODE BELOW DIDN'T WORK
    # stmt = db.session(Villager).filter_by(villager_id=villager_id)
    # # get the villager from the db
    # villager = db.session.scalar(stmt)

    # Select a villager by id
    villager = Villager.query.filter_by(id=villager_id).first()
    # If villager exists
    if villager:
        # update the fields required
        villager.id = body_data.get("id") or villager.id
        villager.name = body_data.get("name") or villager.name
        villager.gender = body_data.get("gender") or villager.gender
        villager.species = body_data.get("species") or villager.species
        villager.personality = body_data.get("personality") or villager.personality
        villager.birthday = body_data.get("birthday") or villager.birthday
        villager.catchphrase = body_data.get("catchphrase") or villager.catchphrase
        villager.hobbies = body_data.get("hobbies") or villager.hobbies
        # commit to the db
        db.session.commit()
        # return a response - with updated villager
        return villager_schema.dump(villager)
    # else
    else:
        # return error message
        return {"error": f"Villager with id {villager_id} not found"}, 404

# # Authorise so only admin can delete villager data from the db
# def authorise_as_admin():
#     # get the user's id from jwt identity
#     user_id = get_jwt_identity()
#     # fetch the user from the db
#     stmt = db.select(User).filter_by(id=user_id)
#     user = db.session.scalar(stmt)
#     # check whether the user is an admin or not
#     return user.is_admin

