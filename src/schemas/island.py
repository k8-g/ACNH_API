from init import ma
from marshmallow import fields

class IslandSchema(ma.Schema):

    # notes = fields.List(fields.Nested('NoteSchema', exclude=["owner"]))
    user = fields.Nested('UserSchema', only=["name","id"])

    class Meta:
        fields = ("island_id", "island_name", "user")


# to handle a single island object
island_schema = IslandSchema()

# to handle a list of island objects
islands_schema = IslandSchema(many=True)