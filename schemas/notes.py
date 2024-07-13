from init import ma
from marshmallow import fields

class NotesSchema(ma.Schema):
    class Meta:
        fields = ("notes_id", "wanted_id", "villager_id", "notes")

    wanted = fields.Nested('VillagersWantedSchema', exclude=('notes',))
    villager = fields.Nested('VillagerSchema', exclude=('notes',))

# to handle a single note object
note_schema = NotesSchema()

# to handle a list of note objects
notes_schema = NotesSchema(many=True)