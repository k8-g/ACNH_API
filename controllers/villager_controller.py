from flask import Blueprint, request
from init import db
from models.villager import Villager
from schemas.villager import villager_schema, villagers_schema
from flask_jwt_extended import jwt_required

# Create a blueprint
villager_bp = Blueprint('villager', __name__)

@villager_bp.route('/villagers', methods=['GET'])
def get_villagers():
    villagers = Villager.query.all()
    return villagers_schema.dump(villagers), 200

@villager_bp.route('/villagers/<int:id>', methods=['GET'])
def get_villager(id):
    villager = Villager.query.get_or_404(id)
    return villager_schema.dump(villager), 200

@villager_bp.route('/villagers', methods=['POST'])
@jwt_required()
def add_villager():
    data = request.get_json()
    new_villager = Villager(
        name=data['name'],
        species=data['species'],
        personality=data['personality'],
        birthday=data['birthday'],
        catchphrase=data['catchphrase'],
        hobbies=data['hobbies']
    )
    db.session.add(new_villager)
    db.session.commit()
    return villager_schema.dump(new_villager), 201

@villager_bp.route('/villagers/<int:id>', methods=['PUT'])
@jwt_required()
def update_villager(id):
    villager = Villager.query.get_or_404(id)
    data = request.get_json()
    villager.name = data['name']
    villager.species = data['species']
    villager.personality = data['personality']
    villager.birthday = data['birthday']
    villager.catchphrase = data['catchphrase']
    villager.hobbies = data['hobbies']
    db.session.commit()
    return villager_schema.dump(villager), 200

@villager_bp.route('/villagers/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_villager(id):
    villager = Villager.query.get_or_404(id)
    db.session.delete(villager)
    db.session.commit()
    return {"message": "Villager deleted"}, 200