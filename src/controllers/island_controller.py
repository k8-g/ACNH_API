from flask import Blueprint, request

from init import db
from flask_jwt_extended import jwt_required, get_jwt_identity

from models.user import User
from models.island import Island
from schemas.island import island_schema, islands_schema

# Create a blueprint
island_bp = Blueprint('island', __name__, url_prefix="/islands")

# /islands - GET - fetch all islands - R
# /islands/<id> - GET - fetch a single island - R
# /islands - POST - create a new island - C
# /islands/<id> - DELETE - delete an island - D
# /islands/<id> - PUT, PATCH - edit an island - U
# R, C, D, U = CRUD


# /islands - GET - fetch all islands - R
@island_bp.route("/", methods=['GET'])
@jwt_required()
def get_all_islands():
    # Check user id via token
    user_id = get_jwt_identity()
    # Select the user to check if they are admin
    stmt = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(stmt)
    # If the user is an admin, select all islands
    if user.is_admin:
        stmt = db.select(Island)
    else:
        # Otherwise, select only islands belonging to the user
        stmt = db.select(Island).filter_by(user_id=user_id)
    islands = db.session.scalars(stmt)
    # Return the island data
    return islands_schema.dump(islands)


# # /islands - GET - fetch all islands - R
# @island_bp.route("/", methods=['GET'])
# @jwt_required()
# def get_all_islands():
#     # check's user id via token
#     user_id = get_jwt_identity()
#     # gets island filtered by id
#     stmt = db.select(Island).filter_by(user_id=user_id)
#     islands = db.session.scalars(stmt)
#     # returns island data
#     return islands_schema.dump(islands)


# /islands - GET - fetch all islands - R
# @island_bp.route("/", methods=['GET'])
# def get_all_islands():
#     # get all islands but ordered according to island_id in descending order
#     # stmt = db.select(Island).order_by(Island.island_id.desc())
#     stmt = db.select(Island)
#     islands = db.session.scalars(stmt)
#     return islands_schema.dump(islands)

# # /islands/<id> - GET - fetch a single island - R
# @island_bp.route("/<int:island_id>", methods=['GET'])
# def get_one_island(island_id):
#     # get the island from the database
#     stmt = db.select(Island).filter_by(id=island_id)
#     island = db.session.scalar(stmt)
#     # if island exists
#     if island:
#         # return island data
#         return island_schema.dump(island)
#     else:
#         # return error message
#         return {"error": f"Island with id {island_id} not found"}, 404

# /islands/<id> - GET - fetch a single island - R
@island_bp.route("/<int:island_id>", methods=['GET'])
@jwt_required()
def get_one_island(island_id):
    # Get the logged-in user's ID
    user_id = get_jwt_identity()
    # Select the user to check if they are admin
    stmt = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(stmt)
    
    # Select the island by id
    stmt = db.select(Island).filter_by(id=island_id)
    island = db.session.scalar(stmt)
    
    # If the island exists
    if island:
        # If the user is not an admin and does not own the island 
        if not user.is_admin and str(island.user_id) != user_id:
            # return an error
            return {"error": "You are not the owner of this island."}, 403
        # Otherwise, return the island data
        return island_schema.dump(island)
    # else
    else:
        # Return error message if island not found
        return {"error": f"Island with id {island_id} not found"}, 404


# /islands - POST - create a new island - C
@island_bp.route("/", methods=['POST'])
@jwt_required()
def create_island():
    #get the data from the body of the request
    body_data = island_schema.load(request.get_json())
    #create a new Island model instance
    island = Island(
        island_name=body_data.get("island_name"),
        user_id=get_jwt_identity()
    )
    #add and commit to db
    db.session.add(island)
    db.session.commit()
    #respond
    return island_schema.dump(island)

# /islands/<id> - DELETE - delete an island - D
@island_bp.route("/<int:island_id>", methods=['DELETE'])
@jwt_required()
def delete_island(island_id):
    # get island from the db
    stmt = db.select(Island).filter_by(id=island_id)
    island = db.session.scalar(stmt)
    # if island exists
    if island:
        user_id = get_jwt_identity()
        # check if the user is the owner of the island
        if str(island.user_id) != user_id:
            # if not correct user, return message
            return {"error": "You are not the owner of this island."}, 403
        # delete the island
        db.session.delete(island)
        db.session.commit()
        # respond
        return {"message": f"Island '{island.island_name}' deleted successfully"}
    #else
    else:
        #return error
        return {"error": f"Island with id {island_id} not found"}, 404
    
    
# /islands/<id> - PUT, PATCH - edit an island - U
@island_bp.route("/<int:island_id>", methods=['PUT','PATCH'])
@jwt_required()
def update_island(island_id):
    # get the data from the body of the request
    body_data = island_schema.load(request.get_json(), partial=True)
    # get the island from the db
    stmt = db.select(Island).filter_by(id=island_id)
    island = db.session.scalar(stmt)
    # if island exists
    if island:
        user_id = get_jwt_identity()
        # check if the user is the owner of the island
        if str(island.user_id) != user_id:
            # if not correct user, return message
            return {"error": "You are not the owner of this island."}, 403
        # update the fields required
        island.island_name = body_data.get("island_name") or island.island_name
        # commit to the db
        db.session.commit()
        # return a response
        return island_schema.dump(island)
    #else
    else:
        #return an error
        return {"error": f"Island with id {island_id} not found"}, 404