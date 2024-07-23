from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.note import Note
from schemas.note import notes_schema, note_schema
from models.villager import Villager
from models.wanted_villagers import WantedVillagers


# Create a blueprint
# /wanted_villagers/<int:wanted_villager_id>/notes
notes_bp = Blueprint("notes", __name__, url_prefix="/<int:wanted_villagers_id>/notes")


# /notes - POST - create a new note
# /notes/<id> - DELETE - delete a note
# /notes/<id> - PUT, PATCH - edit a note

# we already get the notes while  fetching wanted_villagers, so need for GET note route

# /notes - POST - create a new note
@notes_bp.route("/", methods=["POST"])
@jwt_required()
def create_note(wanted_villagers_id):
    # body_data = request.get_json()
    # wanted_villagers_id = body_data.get('wanted_villagers_id')
    # # fetch the wanted villager with that particular id - wanted_villager_id
    # stmt = db.select(WantedVillagers).filter_by(id=wanted_villagers_id)
    # wanted_villager = db.session.scalar(stmt)
    # # if wanted villager exists
    # if wanted_villager:
    #     # create instance of the note model
    #     note = Note(
    #         notes=body_data.get("notes"),
    #         # wanted_villager=wanted_villager
    #         wanted_villagers_id=wanted_villagers_id
    #     )
    #     # add and commit
    #     db.session.add(note)
    #     db.session.commit()
    #     # return the created commit
    #     return note_schema.dump(note), 201
    # # else
    # else:
    #     # return an error; wanted villager does not exist
    #     return {"error": f"Wanted Villager with id {wanted_villagers_id} not found"}, 404
    body_data = request.get_json()
    wanted_villagers_id = body_data.get('wanted_villagers_id')
    villager_name = body_data.get('villager_name')

    user_id = get_jwt_identity()

    if not wanted_villagers_id and not villager_name:
        return {"error": "Either wanted_villagers_id or villager_name must be provided"}, 400

    if wanted_villagers_id:
        stmt = db.select(WantedVillagers).filter_by(id=wanted_villagers_id)
        wanted_villager = db.session.scalar(stmt)
    elif villager_name:
        stmt = db.select(WantedVillagers).join(Villager).filter(Villager.name == villager_name)
        wanted_villager = db.session.scalar(stmt)

    if wanted_villager:
        if str(wanted_villager.island.user_id) != user_id:
            return {"error": "You are not the owner of this island's wanted villager list"}, 403

        note = Note(
            notes=body_data.get("notes"),
            wanted_villagers_id=wanted_villager.id
        )
        db.session.add(note)
        db.session.commit()
        return note_schema.dump(note), 201
    else:
        return {"error": "Wanted Villager not found"}, 404



# Delete Note - /wanted_villagers/wanted_vilagers_id/notes/note_id
@notes_bp.route('/<int:note_id>', methods=['DELETE'])
@jwt_required()
def delete_note(wanted_villagers_id, note_id):
# fetch the note from the db with that id - note_id
    stmt = db.select(Note).filter_by(id=note_id)
    note = db.session.scalar(stmt)
    # if note exists
    if note:
        user_id = get_jwt_identity()
        # if the user is the owner of the note
        if str(note.wanted_villager.island.user_id) != user_id:
            return {"error": "You are not the author of this note"}, 403
        # delete the note
        db.session.delete(note)
        db.session.commit()
        # return some message
        return {"message": f"Note '{note.notes}' deleted successfully"}
    # else
    else:
        # return an error saying comment does not exist
        return {"error": f"Note with id {note_id} not found"}, 404


# Update note - /wanted_villagers/wanted_villagers_id/notes/note_id
@notes_bp.route("/<int:note_id>", methods=["PUT", "PATCH"])
@jwt_required()
def edit_note(wanted_villagers_id, note_id):
    # # get the values from the body of the request
    # body_data = request.get_json()
    # # find the note from the db with the id - note_id
    # stmt = db.select(Note).filter_by(id=note_id)
    # note = db.session.scalar(stmt)
    # # if note exists
    # if note:
    #     user_id = get_jwt_identity()
    #     # if the user is the owner of the note
    #     if str(note.wanted_villager.island.user_id) != user_id:
    #         return {"error": "You are not the author of this note"}, 403
    #     # update the fields
    #     note.notes = body_data.get("notes") or note.notes
    #     # commit
    #     db.session.commit()
    #     # return some response to the client
    #     return note_schema.dump(note)
    # # else
    # else:
    #     # return error saying comment does not exist
    #     return {"error": f"Note with id {note_id} not found"}, 404 

    # Get either wanted villagers id or villager name from the body of the request
    body_data = request.get_json()
    wanted_villagers_id = body_data.get('wanted_villagers_id')
    villager_name = body_data.get('villager_name')

    user_id = get_jwt_identity()
    # if neither wanted villager's id or villager name is provided:
    if not wanted_villagers_id and not villager_name:
        return {"error": "Either wanted_villagers_id or villager_name must be provided"}, 400
    # if wanted villager's id is provided:
    if wanted_villagers_id:
        stmt = db.select(WantedVillagers).filter_by(id=wanted_villagers_id)
        wanted_villager = db.session.scalar(stmt)
    # else if villager's name is provided:
    elif villager_name:
        stmt = db.select(WantedVillagers).join(Villager).filter(Villager.name == villager_name)
        wanted_villager = db.session.scalar(stmt)
    # if the user's id doesn't match the island's user id
    if wanted_villager:
        if str(wanted_villager.island.user_id) != user_id:
            return {"error": "You are not the owner of this island's wanted villager list"}, 403

        stmt = db.select(Note).filter_by(id=note_id, wanted_villagers_id=wanted_villager.id)
        note = db.session.scalar(stmt)

        if note:
            note.notes = body_data.get("notes") or note.notes
            db.session.commit()
            return note_schema.dump(note)
        else:
            return {"error": f"Note with id {note_id} not found for the specified wanted villager"}, 404
    else:
        return {"error": "Wanted Villager not found"}, 404