from init import ma
from marshmallow import fields

class IslandSchema(ma.Schema):

    notes = fields.List(fields.Nested('NoteSchema', exclude=["owner"]))

    class Meta:
        fields = ("island_id", "name_of_island", "owner_of_island", "password", "is_admin", 'notes')


# to handle a single island object
island_schema = IslandSchema(exclude=["password"])

# to handle a list of island objects
islands_schema = IslandSchema(many=True, exclude=["password"])