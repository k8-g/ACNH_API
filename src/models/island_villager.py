from init import db

class IslandVillager(db.Model):
    __tablename__ = "island_villager"

    island_villager_id = db.Column(db.Integer, primary_key=True)
