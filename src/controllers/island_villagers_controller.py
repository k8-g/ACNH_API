from flask import Blueprint, request
from init import db
from models.island_villager import IslandVillager
from schemas.island_villagers import island_villager_schema, island_villagers_schema
from flask_jwt_extended import jwt_required, get_jwt_identity

# Create a blueprint
island_villagers_bp = Blueprint('island_villagers', __name__, url_prefix="/island_villagers")

@island_villagers_bp.route("/", methods=["GET"])
def get_all_island_villagers():
    stmt = db.select(IslandVillager).order_by(IslandVillager.id.asc())
    stmt = db.select(IslandVillager)
    island_villagers = db.session.scalars(stmt)
    return island_villagers_schema.dump(island_villagers)

@island_villagers_bp.route('/<int:island_villager_id>', methods=['GET'])
def get_island_villager(island_villager_id):
    # first id is the db id, second is the id above
    stmt = db.select(IslandVillager).filter_by(id=island_villager_id)
    island_villager = db.session.scalar(stmt)
    if island_villager:
        return island_villager_schema.dump(island_villager)
    else:
        return {"error": f"Villager with id {island_villager_id} not found"}, 404 

@island_villagers_bp.route('/', methods=['POST'])
@jwt_required()
def add_island_villager():
    body_data = request.get_json()
    add_island_villager = IslandVillager(
        island_id=body_data.get('island_id'),
        villager_id=body_data.get('villager_id'),
        text=body_data.get("text"),
    )
    db.session.add(add_island_villager)
    db.session.commit()
    return island_villager_schema.dump(add_island_villager), 201

@island_villagers_bp.route('/<int:island_villager_id>', methods=['PUT','PATCH'])
@jwt_required()
def update_island_villager(island_villager_id):
    body_data = request.get_json()
    island_villager = IslandVillager.query.filter_by(id=island_villager_id).first()
    
    if island_villager:
        user_id = get_jwt_identity()
        # if the user is the owner of the villager list
        if str(island_villager.island.user_id) != user_id:
            return {"error": "You are not the owner of this island's villager list"}, 403

    island_villager = IslandVillager(
        island_id=body_data.get("island_id"),
        villager_id=body_data.get('villager_id')
    )

    if island_villager:
        island_villager.text = body_data.get("text") or island_villager.text

    db.session.commit()
    return island_villager_schema.dump(island_villager), 200

@island_villagers_bp.route('/<int:island_villager_id>', methods=['DELETE'])
@jwt_required()
def delete_island_villager(island_villager_id):
    stmt = db.select(IslandVillager).filter_by(id=island_villager_id)
    island_villager = db.session.scalar(stmt)
    
    if island_villager:
        user_id = get_jwt_identity()
        # if the user is the owner of the villager list
        if str(island_villager.island.user_id) != user_id:
            return {"error": "You are not the owner of this island's villager list"}, 403
        
    if island_villager:
        db.session.delete(island_villager)
        db.session.commit()
        return {"message": f"Villager '{island_villager.villager_id}' deleted successfully from your Island List"}, 200
    else:
        return {"error": f"Villager with id {island_villager_id} not found"}, 404
