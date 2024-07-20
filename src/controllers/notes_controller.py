from flask import Blueprint, request

from init import db
from flask_jwt_extended import jwt_required, get_jwt_identity

from models.note import Note
from schemas.note import notes_schema, note_schema


# Create a blueprint
notes_bp = Blueprint("notes", __name__, url_prefix="/notes")

# /notes - GET - fetch all notes
# /notes/<id> - GET - fetch a single note
# /notes - POST - create a new note
# /notes/<id> - DELETE - delete a note
# /notes/<id> - PUT, PATCH - edit a note

# /notes - GET
@notes_bp.route("/", methods=["GET"])
def get_all_notes():
    stmt = db.select(Note)
    notes = db.session.scalars(stmt)
    # notes = Note.query.all()
    return notes_schema.dump(notes)


# /notes/<id> - GET - fetch a single note
@notes_bp.route("/<int:note_id>", methods=['GET'])
def get_one_note(note_id):
    stmt = db.select(Note).filter_by(id=note_id)
    note = db.session.scalar(stmt)
    if note:
        return note_schema.dump(note)
    else:
        return {"error": f"Note with id {note_id} not found"}, 404
    # note = Note.query.get_or_404(id)
 
# /notes - POST - create a new note
# @notes_bp.route("/", methods=["POST"])
# @jwt_required()
# def create_note():
#     data = request.get_json()
#     new_note = Note(
#         # wanted_id=data['wanted_id'],
#         # villager_id=data['villager_id'],
#         notes=data['notes']
#     )
#     db.session.add(new_note)
#     db.session.commit()
#     return note_schema.dump(new_note), 201

# @notes_bp.route('/notes/<int:id>', methods=['PUT'])
# @jwt_required()
# def update_note(id):
#     note = Note.query.get_or_404(id)
#     data = request.get_json()
#     # note.wanted_id = data['wanted_id']
#     # note.villager_id = data['villager_id']
#     note.notes = data['notes']
#     db.session.commit()
#     return note_schema.dump(note), 200

# @notes_bp.route('/notes/<int:id>', methods=['DELETE'])
# @jwt_required()
# def delete_note(id):
#     note = Note.query.get_or_404(id)
#     db.session.delete(note)
#     db.session.commit()
#     return {"message": "Note deleted"}, 200