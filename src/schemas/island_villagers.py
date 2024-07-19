from init import ma
from marshmallow import fields

class IslandVillagerSchema(ma.Schema):

    user = fields.Nested('UserSchema', only=["name","id"])
    island = fields.Nested('IslandSchema', exclude=["island_villager"])
    comments = fields.List(fields.Nested('CommentSchema', exclude=["island_villager"]))
    villager = fields.List(fields.Nested('VillagerSchema', exclude=["island_villager"]))

    class Meta:
        # fields = ("island_villager_id")
        fields = ("island_villagers_id", "user", "island", "villager_id", "comments")

    # island = fields.Nested('IslandSchema', exclude=('island_villagers', 'wanted'))


# to handle a single island_villager object
island_villager_schema = IslandVillagerSchema()

# to handle a list of island_villager objects
island_villagers_schema = IslandVillagerSchema(many=True)