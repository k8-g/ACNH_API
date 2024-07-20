from init import ma
from marshmallow import fields

class VillagerSchema(ma.Schema):
    island_villagers = fields.Nested('IslandVillagerSchema', many=True, exclude=['villager'])
    wanted_villagers = fields.Nested('WantedVillagerSchema', many=True, exclude=['villager'])

    class Meta:
        fields = ("id", "name", "gender", "species", "personality", "birthday", "catchphrase", "hobbies")
        # fields = ("id", "name", "gender", "species", "personality", "birthday", "catchphrase", "hobbies", "island_villagers", "wanted_villagers")

villager_schema = VillagerSchema()
villagers_schema = VillagerSchema(many=True)

    # user = fields.Nested('UserSchema', only=["name"])

    # island_villagers = fields.List(fields.Nested('IslandVillagersSchema', exclude=('villager',)))
    # wanted = fields.List(fields.Nested('VillagersWantedSchema', exclude=('villager',)))
    # notes = fields.List(fields.Nested('NotesSchema'))