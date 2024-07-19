from flask import Blueprint, request

from init import db
from flask_jwt_extended import jwt_required, get_jwt_identity

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
def get_all_islands():
    # get all islands but ordered according to island_id in descending order
    # stmt = db.select(Island).order_by(Island.island_id.desc())
    stmt = db.select(Island)
    islands = db.session.scalars(stmt)
    # notes = Note.query.all()
    return islands_schema.dump(islands)

# /islands/<id> - GET - fetch a single island - R
@island_bp.route("/<int:island_id>", methods=['GET'])
def get_one_island(island_id):
    # first id is the db id, second is the id above
    stmt = db.select(Island).filter_by(island_id=island_id)
    island = db.session.scalar(stmt)
    if island:
        return island_schema.dump(island)
    else:
        return {"error": f"Island with id {island_id} not found"}, 404


# POST METHOD CODE DOESN'T WORK
# /islands - POST - create a new island - C
@island_bp.route("/", methods=['POST'])
@jwt_required()
def create_island():
    #get the data from the body of the request
    body_data = request.get_json()
    #create a new Island model instance
    # if not body_data.get("owner_of_island") or not body_data.get("island_name"):
    #     return {"error": "owner_of_island and island_name are required"}, 400

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
    stmt = db.select(Island).filter_by(island_id=island_id)
    island = db.session.scalar(stmt)
    # if island exists
    if island:
        # delete the island
        db.session.delete(island)
        db.session.commit()
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
    body_data = request.get_json()
    # get the island from the db
    stmt = db.select(Island).filter_by(island_id=island_id)
    island = db.session.scalar(stmt)
    # if island exists
    if island:
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