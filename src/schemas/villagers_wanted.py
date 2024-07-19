from init import ma
from marshmallow import fields

class VillagersWantedSchema(ma.Schema):
    class Meta:
        fields = ("wanted_id", "item_name", "requirement_description", "required_materials")


    # villager = fields.Nested('VillagerSchema')
    # island = fields.Nested('IslandSchema', exclude=('island_villagers', 'wanted'))
    # notes = fields.List(fields.Nested('NotesSchema'))
    # comments = fields.List(fields.Nested('CommentsSchema'))

# to handle a single villager_wanted object
villager_wanted_schema = VillagersWantedSchema()

# to handle a list of villager_wanted objects
villagers_wanted_schema = VillagersWantedSchema(many=True)