from flask import Blueprint, request
from init import db
from models.island import Island
from schemas.island import island_schema, islands_schema
from flask_jwt_extended import jwt_required

# Create a blueprint
island_bp = Blueprint('island', __name__)

@island_bp.route('/islands', methods=['GET'])
def get_islands():
    islands = Island.query.all()
    return islands_schema.dump(islands), 200

@island_bp.route('/islands/<int:id>', methods=['GET'])
def get_island(id):
    island = Island.query.get_or_404(id)
    return island_schema.dump(island), 200

@island_bp.route('/islands', methods=['POST'])
@jwt_required()
def add_island():
    data = request.get_json()
    new_island = Island(
        name_of_island=data['name_of_island'],
        owner_of_island=data['owner_of_island'],
        password=data['password'],
        is_admin=data.get('is_admin', False)
    )
    db.session.add(new_island)
    db.session.commit()
    return island_schema.dump(new_island), 201

@island_bp.route('/islands/<int:id>', methods=['PUT'])
@jwt_required()
def update_island(id):
    island = Island.query.get_or_404(id)
    data = request.get_json()
    island.name_of_island = data['name_of_island']
    island.owner_of_island = data['owner_of_island']
    island.password = data['password']
    island.is_admin = data.get('is_admin', island.is_admin)
    db.session.commit()
    return island_schema.dump(island), 200

@island_bp.route('/islands/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_island(id):
    island = Island.query.get_or_404(id)
    db.session.delete(island)
    db.session.commit()
    return {"message": "Island deleted"}, 200