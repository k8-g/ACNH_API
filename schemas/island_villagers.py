from init import ma
from marshmallow import fields

class IslandVillagerSchema(ma.Schema):
    class Meta:
        fields = ("island_villager_id")
        # fields = ("island_villagers_id", "island_id", "villager_id", "comment_id")

    # island = fields.Nested('IslandSchema', exclude=('island_villagers', 'wanted'))
    # villager = fields.Nested('VillagerSchema')
    # comments = fields.List(fields.Nested('CommentsSchema'))

# to handle a single island_villager object
island_villager_schema = IslandVillagerSchema()

# to handle a list of island_villager objects
island_villagers_schema = IslandVillagerSchema(many=True)