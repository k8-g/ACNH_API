from flask import Blueprint, request
from init import db
from models.island_villagers import IslandVillagers
from schemas.island_villagers import island_villager_schema, island_villagers_schema
from flask_jwt_extended import jwt_required

# Create a blueprint
island_villagers_bp = Blueprint('island_villagers', __name__)

@island_villagers_bp.route('/island_villagers', methods=['GET'])
def get_island_villagers():
    island_villagers = IslandVillagers.query.all()
    return island_villagers_schema.dump(island_villagers), 200

@island_villagers_bp.route('/island_villagers/<int:id>', methods=['GET'])
def get_island_villager(id):
    island_villager = IslandVillagers.query.get_or_404(id)
    return island_villager_schema.dump(island_villager), 200

@island_villagers_bp.route('/island_villagers', methods=['POST'])
@jwt_required()
def add_island_villager():
    data = request.get_json()
    new_island_villager = IslandVillagers(
        island_id=data['island_id'],
        villager_id=data['villager_id'],
        comment_id=data.get('comment_id', None)
    )
    db.session.add(new_island_villager)
    db.session.commit()
    return island_villager_schema.dump(new_island_villager), 201

@island_villagers_bp.route('/island_villagers/<int:id>', methods=['PUT'])
@jwt_required()
def update_island_villager(id):
    island_villager = IslandVillagers.query.get_or_404(id)
    data = request.get_json()
    island_villager.island_id = data['island_id']
    island_villager.villager_id = data['villager_id']
    island_villager.comment_id = data.get('comment_id', island_villager.comment_id)
    db.session.commit()
    return island_villager_schema.dump(island_villager), 200

@island_villagers_bp.route('/island_villagers/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_island_villager(id):
    island_villager = IslandVillagers.query.get_or_404(id)
    db.session.delete(island_villager)
    db.session.commit()
    return {"message": "Island Villager deleted"}, 200