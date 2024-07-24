from init import db

class WantedVillagers(db.Model):
    # table name
    __tablename__ = "wanted_villagers"

    # attributes of the table
    id = db.Column(db.Integer, primary_key=True)

    # Foreign keys
    island_id = db.Column(db.Integer, db.ForeignKey('island.id'), nullable=False)
    villager_id = db.Column(db.Integer, db.ForeignKey('villager.id'), nullable=False)
    

    # Relationships
    # WantedVillagers links back to Island
    island = db.relationship('Island', backref='wanted_villagers')
    # WantedVillagers links back to Villager
    villager = db.relationship('Villager', backref='wanted_villagers')
    # WantedVillager links back to Note
    notes = db.relationship('Note', back_populates='wanted_villager')

    # Each Island can have multiple WantedVillagers
    # Each WantedVillager can have multiple notes
    # WantedVillager accesses Villager's data

