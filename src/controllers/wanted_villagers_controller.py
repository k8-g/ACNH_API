from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.villager import Villager
from models.wanted_villagers import WantedVillagers
from schemas.wanted_villagers import wanted_villager_schema, wanted_villagers_schema
from controllers.notes_controller import notes_bp

# Create a blueprint
wanted_villagers_bp = Blueprint('wanted_villagers', __name__, url_prefix="/wanted_villagers")
# wanted_villagers_bp.register_blueprint(notes_bp)
wanted_villagers_bp.register_blueprint(notes_bp)

@wanted_villagers_bp.route('/', methods=['GET'])
def get_wanted_villagers():
    stmt = db.select(WantedVillagers).order_by(WantedVillagers.id.asc())
    stmt = db.select(WantedVillagers)
    wanted_villagers = db.session.scalars(stmt)
    return wanted_villagers_schema.dump(wanted_villagers)

@wanted_villagers_bp.route('/<int:wanted_villagers_id>', methods=['GET'])
def get_wanted_villager(wanted_villagers_id):
    stmt = db.select(WantedVillagers).filter_by(id=wanted_villagers_id)
    wanted_villagers = db.session.scalar(stmt)
    if wanted_villagers:
        return wanted_villager_schema.dump(wanted_villagers)
    else:
        return {"error": f"Villager with id {wanted_villagers_id} not found"}, 404 

@wanted_villagers_bp.route('/', methods=['POST'])
@jwt_required()
def add_wanted_villager():
    body_data = request.get_json()
    # add_wanted_villager = WantedVillagers(
    #     island_id=body_data.get('island_id'), 
    #     villager_id=body_data.get('villager_id'),  
    # )

    # Look up the villager's ID based on the name provided in the request body
    villager_name = body_data.get('villager_name')
    villager = Villager.query.filter_by(name=villager_name).first()

    if not villager:
        return {"error": f"Villager with name {villager_name} not found"}, 404

    add_wanted_villager = WantedVillagers(
        island_id=body_data.get('island_id'), 
        villager_id=villager.id  # Use the retrieved villager ID
    )

    db.session.add(add_wanted_villager)
    db.session.commit()
    return wanted_villager_schema.dump(add_wanted_villager), 201

@wanted_villagers_bp.route('/<int:wanted_villagers_id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_wanted_villager(wanted_villagers_id):
    return {"error": "Updating wanted villager entries is not allowed, as this section is ID's only. You may update notes for your wanted villagers instead."}, 405
    # body_data = request.get_json()
    # wanted_villagers = WantedVillagers.query.filter_by(id=wanted_villagers_id).first()
    # # , partial=True 

    # wanted_villager = WantedVillagers(
    #     island_id=body_data.get('island_id'), 
    #     villager_id=body_data.get('villager_id'),  
    # )

    # if wanted_villagers:
    #     user_id = get_jwt_identity()
    # # if the user is the owner of the island
    # if str(wanted_villagers.island.user_id) != user_id:
    #     return {"error": "You are not the owner of this island's wanted villager list."}, 403
    
    # db.session.commit()
    # return wanted_villager_schema.dump(wanted_villager), 200

@wanted_villagers_bp.route('/<int:wanted_villagers_id>', methods=['DELETE'])
@jwt_required()
def delete_wanted_villager(wanted_villagers_id):
    # stmt = db.select(WantedVillagers).filter_by(id=wanted_villagers_id)
    # wanted_villagers = db.session.scalar(stmt)
    # if wanted_villagers:
    #     user_id = get_jwt_identity()
    #     # if the user is the owner of the island
    #     if str(wanted_villagers.island.user_id) != user_id:
    #         return {"error": "You are not the owner of this island's wanted villager list."}, 403

    # if wanted_villagers:
    #     db.session.delete(wanted_villagers)
    #     db.session.commit()
    #     return {"message": f"Villager '{wanted_villagers.villager_id}' deleted successfully from your Wanted List"}, 200
    # else:
    #     return {"error": f"Villager with id {wanted_villagers_id} not found"}, 404
    body_data = request.get_json()
    wanted_villagers_id = body_data.get('wanted_villagers_id')
    villager_name = body_data.get('villager_name')

    # if neither wanted villager's id or villager's name has been provided:
    if not wanted_villagers_id and not villager_name:
        return {"error": "Either 'wanted_villagers_id' or 'villager_name' is required to delete a wanted villager."}, 400

    # If wanted villager's id was provided:
    if wanted_villagers_id:
        stmt = db.select(WantedVillagers).filter_by(id=wanted_villagers_id)
        wanted_villagers = db.session.scalar(stmt)
    # else if villager's name was provided:
    elif villager_name:
        # Search for villager's name to obtain villager id
        villager = Villager.query.filter_by(name=villager_name).first()
        if not villager:
            return {"error": f"Villager with name {villager_name} not found"}, 404
        wanted_villagers = WantedVillagers.query.filter_by(villager_id=villager.id).first()
    
    if not wanted_villagers:
        return {"error": "Wanted villager entry not found"}, 404

    user_id = get_jwt_identity()

    if str(wanted_villagers.island.user_id) != user_id:
        return {"error": "You are not the owner of this island's wanted villager list."}, 403

    db.session.delete(wanted_villagers)
    db.session.commit()
    return {"message": f"'{wanted_villagers.villager.name}' deleted successfully from your Wanted List"}, 200



    # if not villager_name:
    #     return {"error": "Villager name is required to delete a wanted villager."}, 400

    # # Find the villager by name
    # villager = Villager.query.filter_by(name=villager_name).first()

    # if not villager:
    #     return {"error": f"Villager with name {villager_name} not found"}, 404

    # # Find the wanted villager entry
    # wanted_villagers = WantedVillagers.query.filter_by(villager_id=villager.id).first()

    # if not wanted_villagers:
    #     return {"error": f"Wanted villager entry with name {villager_name} not found"}, 404

    # user_id = get_jwt_identity()

    # if str(wanted_villagers.island.user_id) != user_id:
    #     return {"error": "You are not the owner of this island's wanted villager list."}, 403

    # db.session.delete(wanted_villagers)
    # db.session.commit()
    # return {"message": f"'{villager_name}' deleted successfully from your Wanted List"}, 200