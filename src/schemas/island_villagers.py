from init import ma
from marshmallow import fields

class IslandVillagerSchema(ma.Schema):

    # island = fields.Nested('IslandSchema', exclude=["island_villager"])
    # villager = fields.List(fields.Nested('VillagerSchema', exclude=["island_villager"]))

    island = fields.Nested('IslandSchema', only=["id", "island_name"])
    villager = fields.Nested('VillagerSchema',exclude=["id"])


    class Meta:
        fields = ("id", "island", "villager", "text", "villager_id")

island_villager_schema = IslandVillagerSchema()
island_villagers_schema = IslandVillagerSchema(many=True)

    # user = fields.Nested('UserSchema', only=["name","id"])
    # comments = fields.List(fields.Nested('CommentSchema', exclude=["island_villager"]))

    # island = fields.Nested('IslandSchema', exclude=('island_villagers', 'wanted'))