from init import db

# Model name/Class name
class IslandVillager(db.Model):
    # name of the table
    __tablename__ = "island_villager"

    # Attributes of the table
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String, nullable=True)

    # Foreign keys
    island_id = db.Column(db.Integer, db.ForeignKey("island.id"), nullable=False)
    villager_id = db.Column(db.Integer, db.ForeignKey("villager.id"), nullable=False)
    
    # Relationships
    # IslandVillagers links back to Island table
    island = db.relationship('Island')
    # IslandVillagers links back to Villager table
    villager = db.relationship('Villager')

    # Each Island can have multiple IslandVillagers
    # IslandVillagers accesses Villager data
    
