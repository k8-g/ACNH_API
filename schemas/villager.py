from init import ma

class VillagerSchema(ma.Schema):
    class Meta:
        fields = ("villager_id", "name", "species", "personality", "birthday", "catchphrase", "hobbies")

# to handle a single villager object
villager_schema = VillagerSchema()

# to handle a list of villager objects
villagers_schema = VillagerSchema(many=True)