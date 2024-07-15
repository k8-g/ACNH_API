from flask import Blueprint, request
from init import db
from models.note import Note
from schemas.note import notes_schema, note_schema
from flask_jwt_extended import jwt_required

# Create a blueprint
notes_bp = Blueprint('notes', __name__)

@notes_bp.route('/notes', methods=['GET'])
def get_notes():
    notes = Note.query.all()
    return notes_schema.dump(notes), 200

@notes_bp.route('/notes/<int:id>', methods=['GET'])
def get_note(id):
    note = Note.query.get_or_404(id)
    return note_schema.dump(note), 200

@notes_bp.route('/notes', methods=['POST'])
@jwt_required()
def add_note():
    data = request.get_json()
    new_note = Note(
        # wanted_id=data['wanted_id'],
        # villager_id=data['villager_id'],
        notes=data['notes']
    )
    db.session.add(new_note)
    db.session.commit()
    return note_schema.dump(new_note), 201

@notes_bp.route('/notes/<int:id>', methods=['PUT'])
@jwt_required()
def update_note(id):
    note = Note.query.get_or_404(id)
    data = request.get_json()
    # note.wanted_id = data['wanted_id']
    # note.villager_id = data['villager_id']
    note.notes = data['notes']
    db.session.commit()
    return note_schema.dump(note), 200

@notes_bp.route('/notes/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_note(id):
    note = Note.query.get_or_404(id)
    db.session.delete(note)
    db.session.commit()
    return {"message": "Note deleted"}, 200