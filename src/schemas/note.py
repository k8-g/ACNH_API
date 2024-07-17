from init import ma
from marshmallow import fields

class NoteSchema(ma.Schema):

    owner = fields.Nested('IslandSchema', only=["owner_of_island", "name_of_island"])
    villager = fields.Nested('VillagerSchema', only=["name"])

    class Meta:

        fields = ("owner", "villager_id", "note_id", "notes")

# to handle a single note object
note_schema = NoteSchema()

# to handle a list of note objects
notes_schema = NoteSchema(many=True)