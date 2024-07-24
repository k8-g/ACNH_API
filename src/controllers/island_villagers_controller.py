from flask import Blueprint, request
from init import db
from models.villager import Villager
from models.island_villager import IslandVillager
from schemas.island_villagers import island_villager_schema, island_villagers_schema
from flask_jwt_extended import jwt_required, get_jwt_identity

# Create a blueprint
island_villagers_bp = Blueprint('island_villagers', __name__, url_prefix="/island_villagers")

# /island_villagers - GET - fetch all island villagers
@island_villagers_bp.route("/", methods=["GET"])
def get_all_island_villagers():
    # fetch all island villagers s and order them according to ID No. in descending order
    stmt = db.select(IslandVillager).order_by(IslandVillager.id.asc())
    stmt = db.select(IslandVillager)
    island_villagers = db.session.scalars(stmt)
    return island_villagers_schema.dump(island_villagers)

# /island_villagers/<id> - GET - fetch a single island_villager
@island_villagers_bp.route('/<int:island_villager_id>', methods=['GET'])
def get_island_villager(island_villager_id):
    # first id is the db id, second is the id above
    stmt = db.select(IslandVillager).filter_by(id=island_villager_id)
    island_villager = db.session.scalar(stmt)
    # if island villager requested exists
    if island_villager:
        # return response
        return island_villager_schema.dump(island_villager)
    # else
    else:
        # return error message
        return {"error": f"Villager with id {island_villager_id} not found"}, 404 

# /island_villagers - POST - Add a new island_villager to island villager list

@island_villagers_bp.route('/', methods=['POST'])
@jwt_required()
def add_island_villager():
    # body_data = request.get_json()
    # add_island_villager = IslandVillager(
    #     island_id=body_data.get('island_id'),
    #     villager_id=body_data.get('villager_id'),
    #     text=body_data.get("text"),
    # )
    # db.session.add(add_island_villager)
    # db.session.commit()
    # return island_villager_schema.dump(add_island_villager), 201

    # get the data from the body of the request
    body_data = request.get_json()

    villager_id = body_data.get('villager_id')
    villager_name = body_data.get('villager_name')

    # if villager id and or villager name is not provided
    if not villager_id and not villager_name:
        # return error message
        return {"error": "Either villager_id or villager_name must be provided."}, 400

    # if Villager name is provided
    if villager_name:
        # Search for the villager name
        villager = Villager.query.filter_by(name=villager_name).first()
        # if villager name doesn't exist in database
        if not villager:
            # return error message
            return {"error": f"Villager with name {villager_name} not found."}, 404
        villager_id = villager.id

    # create island villager model instance
    add_island_villager = IslandVillager(
        island_id=body_data.get('island_id'),
        villager_id=villager_id,
        text=body_data.get("text"),
    )
    # add and commit to database
    db.session.add(add_island_villager)
    db.session.commit()
    # respond
    return island_villager_schema.dump(add_island_villager), 201


@island_villagers_bp.route('/<int:island_villager_id>', methods=['PUT','PATCH'])
@jwt_required()
def update_island_villager(island_villager_id):
    # body_data = request.get_json()
    # island_villager = IslandVillager.query.filter_by(id=island_villager_id).first()
    
    # if island_villager:
    #     user_id = get_jwt_identity()
    #     # if the user is the owner of the villager list
    #     if str(island_villager.island.user_id) != user_id:
    #         return {"error": "You are not the owner of this island's villager list"}, 403

    # island_villager = IslandVillager(
    #     island_id=body_data.get("island_id"),
    #     villager_id=body_data.get('villager_id')
    # )

    # if island_villager:
    #     island_villager.text = body_data.get("text") or island_villager.text

    # db.session.commit()
    # return island_villager_schema.dump(island_villager), 200

    # get the data from the body of the request
    body_data = request.get_json()
    island_villager = IslandVillager.query.filter_by(id=island_villager_id).first()
    # if island villager does not exist in island villager list
    if not island_villager:
        # return error message
        return {"error": f"Island villager with id {island_villager_id} not found"}, 404
    # get user's id
    user_id = get_jwt_identity()
    # check if the user is the owner of the island villager list, if not the user
    if str(island_villager.island.user_id) != user_id:
        # return error message
        return {"error": "You are not the owner of this island's villager list"}, 403

    villager_id = body_data.get('villager_id')
    villager_name = body_data.get('villager_name')

    # if not correct villager name
    if not villager_name:
        # return error message
        return {"error": "Villager name is required to update the island villager"}, 400
        # so that user is updating note on correct island villager name

    # if villager name exists
    if villager_name:
        # search for villager name
        villager = Villager.query.filter_by(name=villager_name).first()
        # if villager doesn't exist in island villager list
        if not villager:
            # return error message
            return {"error": f"Villager with name {villager_name} not found."}, 404
        villager_id = villager.id
    # if villager id exists
    if villager_id:
        island_villager.villager_id = villager_id
    # update the fields as required
    island_villager.island_id = body_data.get("island_id") or island_villager.island_id
    island_villager.text = body_data.get("text") or island_villager.text
    # commit to database
    db.session.commit()
    # respond
    return island_villager_schema.dump(island_villager), 200

# /island_villager/<id> - DELETE - delete an island villager from island villager list
@island_villagers_bp.route('/<int:island_villager_id>', methods=['DELETE'])
@jwt_required()
def delete_island_villager(island_villager_id):
    # get island villager info from the database
    stmt = db.select(IslandVillager).filter_by(id=island_villager_id)
    island_villager = db.session.scalar(stmt)
    # if island villager exists
    if island_villager:
        # gets the user's id
        user_id = get_jwt_identity()
        # check if the user is the owner of the island villager list, if not the user
        if str(island_villager.island.user_id) != user_id:
            # return error message
            return {"error": "You are not the owner of this island's villager list"}, 403
    # if island villager exists
    if island_villager:
        # delete and commit to database
        db.session.delete(island_villager)
        db.session.commit()
        # Return response
        return {"message": f"Villager '{island_villager.villager_id}' deleted successfully from your Island List"}, 200
    # else
    else:
        # return error message
        return {"error": f"Villager with id {island_villager_id} not found"}, 404
