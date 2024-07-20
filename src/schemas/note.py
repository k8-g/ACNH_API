from init import ma
from marshmallow import fields

class NoteSchema(ma.Schema):
    wanted_villager = fields.Nested('WantedVillagerSchema', exclude=["notes"])

    class Meta:
        fields = ("id", "notes", "wanted_villager")


note_schema = NoteSchema()
notes_schema = NoteSchema(many=True)