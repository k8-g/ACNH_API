from init import ma
from marshmallow import fields
from marshmallow.validate import Length, And, Regexp

class IslandSchema(ma.Schema):

    user = fields.Nested('UserSchema', only=["name","id"])
    island_villagers = fields.Nested('IslandVillagerSchema', many=True, exclude=['island'])
    wanted_villagers = fields.Nested('WantedVillagerSchema', many=True, exclude=['island'])

    island_name = fields.String(required=True, validate=And(
        Length(min=2, error="Island name must be at least two characters long."),
        Regexp('^[A-Za-z0-9 ]+$', error="Island name must have alphanumerics characters only")
        ))

    class Meta:
        fields = ("user", "id", "island_name")
        ordered = True

island_schema = IslandSchema()
islands_schema = IslandSchema(many=True)

