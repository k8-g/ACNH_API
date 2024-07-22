from init import ma
from marshmallow import fields

class WantedVillagerSchema(ma.Schema):
    
    island = fields.Nested('IslandSchema', only=["id", "island_name"])
    villager = fields.Nested('VillagerSchema')
    # notes = fields.Nested('NoteSchema', exclude=["wanted_vilager"])
    notes = fields.Nested('NoteSchema', many=True, exclude=["wanted_villager"])

    class Meta:
        fields = ("island", "villager", "id", "notes")
        # fields = ("id", "island", "villager", "notes")
        ordered = True


wanted_villager_schema = WantedVillagerSchema()
wanted_villagers_schema = WantedVillagerSchema(many=True)


    # villager = fields.Nested('VillagerSchema')
    # island = fields.Nested('IslandSchema', exclude=('island_villagers', 'wanted'))
    # notes = fields.List(fields.Nested('NotesSchema'))
    # comments = fields.List(fields.Nested('CommentsSchema'))