from flask import Blueprint, request
from init import db
from models.villagers_wanted import VillagersWanted
from schemas.villagers_wanted import villagers_wanted_schema, villager_wanted_schema
from flask_jwt_extended import jwt_required

# Create a blueprint
villagers_wanted_bp = Blueprint('villagers_wanted', __name__)

@villagers_wanted_bp.route('/villagers_wanted', methods=['GET'])
def get_villagers_wanted():
    villagers_wanted = VillagersWanted.query.all()
    return villagers_wanted_schema.dump(villagers_wanted), 200

@villagers_wanted_bp.route('/villagers_wanted/<int:id>', methods=['GET'])
def get_villager_wanted(id):
    villager_wanted = VillagersWanted.query.get_or_404(id)
    return villager_wanted_schema.dump(villager_wanted), 200

@villagers_wanted_bp.route('/villagers_wanted', methods=['POST'])
@jwt_required()
def add_villager_wanted():
    data = request.get_json()
    new_villager_wanted = VillagersWanted(
        # villager_id=data['villager_id'],
        # island_id=data['island_id'],
        item_name=data['item_name'],
        requirement_description=data['requirement_description'],
        required_materials=data['required_materials']
        # notes_id=data.get('notes_id', None)
    )
    db.session.add(new_villager_wanted)
    db.session.commit()
    return villager_wanted_schema.dump(new_villager_wanted), 201

@villagers_wanted_bp.route('/villagers_wanted/<int:id>', methods=['PUT'])
@jwt_required()
def update_villager_wanted(id):
    villager_wanted = VillagersWanted.query.get_or_404(id)
    data = request.get_json()
    # villager_wanted.villager_id = data['villager_id']
    # villager_wanted.island_id = data['island_id']
    villager_wanted.item_name = data['item_name']
    villager_wanted.requirement_description = data['requirement_description']
    villager_wanted.required_materials = data['required_materials']
    # villager_wanted.notes_id = data.get('notes_id', villager_wanted.notes_id)
    db.session.commit()
    return villager_wanted_schema.dump(villager_wanted), 200

@villagers_wanted_bp.route('/villagers_wanted/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_villager_wanted(id):
    villager_wanted = VillagersWanted.query.get_or_404(id)
    db.session.delete(villager_wanted)
    db.session.commit()
    return {"message": "Villager Wanted deleted"}, 200