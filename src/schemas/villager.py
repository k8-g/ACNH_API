from init import ma
from marshmallow import fields

class VillagerSchema(ma.Schema):

    user = fields.Nested('UserSchema', only=["name"])

    class Meta:
        fields = ("villager_id", "name", "gender", "species", "personality", "birthday", "catchphrase", "hobbies", "user")

    # island_villagers = fields.List(fields.Nested('IslandVillagersSchema', exclude=('villager',)))
    # wanted = fields.List(fields.Nested('VillagersWantedSchema', exclude=('villager',)))
    # notes = fields.List(fields.Nested('NotesSchema'))

# to handle a single villager object
villager_schema = VillagerSchema()

# to handle a list of villager objects
villagers_schema = VillagerSchema(many=True)