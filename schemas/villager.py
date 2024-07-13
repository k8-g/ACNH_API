from init import ma
from marshmallow import fields

class VillagerSchema(ma.Schema):
    class Meta:
        fields = ("villager_id", "name", "species", "personality", "birthday", "catchphrase", "hobbies")

    island_villagers = fields.Nested('IslandVillagersSchema', many=True, exclude=('villager',))
    wanted = fields.Nested('VillagersWantedSchema', many=True, exclude=('villager',))
    notes = fields.Nested('NotesSchema', many=True)

# to handle a single villager object
villager_schema = VillagerSchema()

# to handle a list of villager objects
villagers_schema = VillagerSchema(many=True)