from init import ma
from marshmallow import fields

class VillagersWantedSchema(ma.Schema):
    class Meta:
        fields = ("wanted_id", "villager_id", "island_id", "item_name", "requirement_description", "required_materials", "notes_id")

    villager = fields.Nested('VillagerSchema')
    island = fields.Nested('IslandSchema', exclude=('island_villagers', 'wanted'))
    notes = fields.Nested('NotesSchema', many=True)
    comments = fields.Nested('CommentsSchema', many=True)

# to handle a single villager_wanted object
villager_wanted_schema = VillagersWantedSchema()

# to handle a list of villager_wanted objects
villagers_wanted_schema = VillagersWantedSchema(many=True)