from flask import Blueprint, request

from init import db
from flask_jwt_extended import jwt_required, get_jwt_identity

from models.villager import Villager
from schemas.villager import villager_schema, villagers_schema


# Create a blueprint
villager_bp = Blueprint('villager', __name__, url_prefix="/villagers")

# /villagers - GET - fetch all villagers - R
@villager_bp.route("/", methods=["GET"])
def get_all_villagers():
    # stmt = db.select(Villager).order_by(Villager.villager_id.asc())
    stmt = db.select(Villager)
    villagers = db.session.scalars(stmt)
    # notes = Note.query.all()
    return villagers_schema.dump(villagers)

# /villagers/<id> - GET - fetch a single villager - R
@villager_bp.route("/<int:villager_id>", methods=["GET"])
def get_villager(villager_id):
    # first id is the db id, second is the id above
    stmt = db.select(Villager).filter_by(villager_id=villager_id)
    villager = db.session.scalar(stmt)
    if villager:
        return villager_schema.dump(villager)
    else:
        return {"error": f"Villager with id {villager_id} not found"}, 404 


@villager_bp.route("/", methods=["POST"])
@jwt_required()
def create_villager():
    body_data = request.get_json()
    user_id=get_jwt_identity()

    island_id = body_data.get('island_id')
    if not island_id:
        return {"error": "island_id is required"}, 400
    
    villager = Villager(
        name=body_data.get("name"),
        species=body_data.get("species"),
        gender=body_data.get("gender"),
        personality=body_data.get("personality"),
        birthday=body_data.get("birthday"),
        catchphrase=body_data.get("catchphrase"),
        hobbies=body_data.get("hobbies"),
        # user_id=get_jwt_identity()
        user_id=user_id,
        island_id=island_id
    )
    db.session.add(villager)
    db.session.commit()
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


@villager_bp.route("/<int:villager_id>", methods=["DELETE"])
@jwt_required()
def delete_villager(villager_id):
    stmt = db.select(Villager).filter_by(villager_id=villager_id)
    villager = db.session.scalar(stmt)
    if villager:
        db.session.delete(villager)
        db.session.commit()
        return {"message": f"Villager '{villager.name}' deleted successfully"}
    else:
        return {"error": f"Villager with id {villager_id} not found"}, 404


@villager_bp.route("/<int:villager_id>",  methods=["PUT","PATCH"])
@jwt_required()
def update_villager(villager_id):
    # get the data from the body of the request
    body_data = request.get_json()

    # CODE BELOW DIDN'T WORK
    # stmt = db.session(Villager).filter_by(villager_id=villager_id)
    # # get the villager from the db
    # villager = db.session.scalar(stmt)

    # WORKS
    villager = Villager.query.filter_by(villager_id=villager_id).first()

    if villager:
        # update the fields required
        villager.villager_id = body_data.get("villager_id") or villager.villager_id
        villager.name = body_data.get("name") or villager.name
        villager.gender = body_data.get("gender") or villager.gender
        villager.species = body_data.get("species") or villager.species
        villager.personality = body_data.get("personality") or villager.personality
        villager.birthday = body_data.get("birthday") or villager.birthday
        villager.catchphrase = body_data.get("catchphrase") or villager.catchphrase
        villager.hobbies = body_data.get("hobbies") or villager.hobbies
        # commit to the db
        db.session.commit()
        # return a response
        return villager_schema.dump(villager)
    else:
        return {"error": f"Villager with id {villager_id} not found"}, 404

