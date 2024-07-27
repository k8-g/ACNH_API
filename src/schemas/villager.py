from init import ma
from marshmallow import fields

class VillagerSchema(ma.Schema):
    island_villagers = fields.Nested('IslandVillagerSchema', many=True, exclude=['villager'])
    wanted_villagers = fields.Nested('WantedVillagerSchema', many=True, exclude=['villager'])

    class Meta:
        fields = ("id", "name", "gender", "species", "personality", "birthday", "catchphrase", "hobbies")

villager_schema = VillagerSchema()
villagers_schema = VillagerSchema(many=True)

