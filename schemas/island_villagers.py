from init import ma

class IslandVillagersSchema(ma.Schema):
    class Meta:
        fields = ("island_villagers_id", "island_id", "villager_id", "comment_id")

# to handle a single island_villager object
island_villager_schema = IslandVillagersSchema()

# to handle a list of island_villager objects
island_villagers_schema = IslandVillagersSchema(many=True)