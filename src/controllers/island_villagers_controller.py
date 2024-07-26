from flask import Blueprint, request
from init import db
from models.user import User
from models.island import Island
from models.villager import Villager
from models.island_villager import IslandVillager
from schemas.island_villagers import island_villager_schema, island_villagers_schema
from flask_jwt_extended import jwt_required, get_jwt_identity

# Create a blueprint
island_villagers_bp = Blueprint('island_villagers', __name__, url_prefix="/island_villagers")

# /island_villagers - GET - fetch all island villagers
@island_villagers_bp.route("/", methods=["GET"])
@jwt_required()
def get_all_island_villagers():
    # # fetch all island villagers s and order them according to ID No. in descending order
    # stmt = db.select(IslandVillager).order_by(IslandVillager.id.asc())
    # stmt = db.select(IslandVillager)
    # island_villagers = db.session.scalars(stmt)
    # return island_villagers_schema.dump(island_villagers)

    # Get the logged-in user's ID
    user_id = get_jwt_identity()
    
    # Check if the user is an admin
    stmt = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(stmt)
    # If the user is an admin
    if user.is_admin:
        # fetch all island villagers
        stmt = db.select(IslandVillager).order_by(IslandVillager.id.asc())
    else:
        # If the user is not an admin, fetch only their island villagers
        stmt = db.select(IslandVillager).join(Island).filter(Island.user_id == user_id).order_by(IslandVillager.id.asc())
    
    island_villagers = db.session.scalars(stmt)
    return island_villagers_schema.dump(island_villagers)

# /island_villagers/<id> - GET - fetch a single island_villager
@island_villagers_bp.route('/<int:island_villager_id>', methods=['GET'])
@jwt_required()
def get_island_villager(island_villager_id):
    # # first id is the db id, second is the id above
    # stmt = db.select(IslandVillager).filter_by(id=island_villager_id)
    # island_villager = db.session.scalar(stmt)
    # # if island villager requested exists
    # if island_villager:
    #     # return response
    #     return island_villager_schema.dump(island_villager)
    # # else
    # else:
    #     # return error message
    #     return {"error": f"Villager with id {island_villager_id} not found"}, 404 


    # # Get the logged-in user's ID
    # user_id = get_jwt_identity()
    
    # # Check if the user is an admin
    # stmt = db.select(User).filter_by(id=user_id)
    # user = db.session.scalar(stmt)
    
    # # Fetch the island villager
    # stmt = db.select(IslandVillager).filter_by(id=island_villager_id)
    # island_villager = db.session.scalar(stmt)
    # # if the island villager exists
    # if island_villager:
    #     # If the user is an admin or the owner of the island villager
    #     if user.is_admin or island_villager.island.user_id == user_id:
    #         # return the data
    #         return island_villager_schema.dump(island_villager)
    #     # else if the user is not authorised
    #     else:
    #         # return an error
    #         return {"error": "You do not have permission to view this island villager."}, 403
    # else:
    #     # Return an error if the island villager is not found
    #     return {"error": f"Island villager with id {island_villager_id} not found"}, 404


    # Get the user's id from the JWT
    user_id = get_jwt_identity()
    # Debug: print the user id
    print(f"User ID from JWT: {user_id}")
    
    # First id is the db id, second is the id above
    stmt = db.select(IslandVillager).filter_by(id=island_villager_id)
    island_villager = db.session.scalar(stmt)
    # Debug: print the island villager details
    print(f"Island Villager: {island_villager}")

    # If island villager requested exists
    if island_villager:
        # Debug: print the island user id
        print(f"Island User ID: {island_villager.island.user_id}")
        # Check if the user is the owner of the island villager list
        if str(island_villager.island.user_id) != user_id:
            return {"error": "You do not have permission to view this island villager."}, 403
        # Return response
        return island_villager_schema.dump(island_villager)
    # Else
    else:
        # Return error message
        return {"error": f"Island villager with id {island_villager_id} not found"}, 404

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

   # Ensure no attempt to change island_villager_id
    if 'island_villager_id' in body_data:
        return {"error": "Updating the island villager ID is not allowed"}, 400
    
    # villager_id = body_data.get('villager_id')
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
            return {"error": f"Island villager with name {villager_name} not found."}, 404
        villager_id = villager.id
    # if villager id exists
    if villager_id:
        island_villager.villager_id = villager_id
    # update the fields as required
    # island_villager.island_id = body_data.get("island_id") or island_villager.island_id
    island_villager.text = body_data.get("text") or island_villager.text
    # commit to database
    db.session.commit()
    # respond
    return island_villager_schema.dump(island_villager), 200

# /island_villager/<id> - DELETE - delete an island villager from island villager list
@island_villagers_bp.route('/<int:island_villager_id>', methods=['DELETE'])
@jwt_required()
def delete_island_villager(island_villager_id):
    # # get island villager info from the database
    # stmt = db.select(IslandVillager).filter_by(id=island_villager_id)
    # island_villager = db.session.scalar(stmt)
    # # if island villager exists
    # if island_villager:
    #     # gets the user's id
    #     user_id = get_jwt_identity()
    #     # check if the user is the owner of the island villager list, if not the user
    #     if str(island_villager.island.user_id) != user_id:
    #         # return error message
    #         return {"error": "You are not the owner of this island's villager list"}, 403
    # # if island villager exists
    # if island_villager:
    #     # delete and commit to database
    #     db.session.delete(island_villager)
    #     db.session.commit()
    #     # Return response
    #     return {"message": f"Villager '{island_villager.villager_id}' deleted successfully from your Island List"}, 200
    # # else
    # else:
    #     # return error message
    #     return {"error": f"Villager with id {island_villager_id} not found"}, 404

    # Get the user's id from the JWT
    user_id = get_jwt_identity()
    
    # First id is the db id, second is the id above
    stmt = db.select(IslandVillager).filter_by(id=island_villager_id)
    island_villager = db.session.scalar(stmt)
    
    # If island villager requested exists
    if island_villager:
        # Check if the user is the owner of the island villager list
        if str(island_villager.island.user_id) != user_id:
            return {"error": "You do not have permission to view this island villager."}, 403
        
        # Retrieve the villager details
        villager = db.session.scalar(db.select(Villager).filter_by(id=island_villager.villager_id))
        
        # if villager not found
        if not villager:
            return {"error": "Villager not found"}, 404
        
        # Delete the island villager
        db.session.delete(island_villager)
        db.session.commit()
        
        # return response with both ID and name
        return {"message": f"Villager '{villager.name}' (ID: {island_villager.villager_id}) deleted successfully from your Island List"}, 200
    # else
    else:
        # return error message
        return {"error": f"Island villager with id {island_villager_id} not found"}, 404