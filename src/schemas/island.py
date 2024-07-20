from init import ma
from marshmallow import fields

class IslandSchema(ma.Schema):

    user = fields.Nested('UserSchema', only=["name","id"])
    island_villagers = fields.Nested('IslandVillagerSchema', many=True, exclude=['island'])
    wanted_villagers = fields.Nested('WantedVillagerSchema', many=True, exclude=['island'])

    class Meta:
        fields = ("id", "island_name", "user")
        # fields = ("id", "island_name", "user", "island_villagers", "wanted_villagers")

island_schema = IslandSchema()
islands_schema = IslandSchema(many=True)

    # notes = fields.List(fields.Nested('NoteSchema', exclude=["owner"]))
    # comments = fields.List(fields.Nested('CommentSchema', exclude=["island"]))

