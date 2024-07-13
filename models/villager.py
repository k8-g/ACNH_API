from init import db

class Villagers(db.Model):
    __tablename__ = "villagers"

    villager_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    species = db.Column(db.String, nullable=False)
    personality = db.Column(db.String, nullable=False)
    birthday = db.Column(db.String, nullable=False)
    catchphrase = db.Column(db.String, nullable=False)
    hobbies = db.Column(db.String, nullable=False)

    # Relationships
    island_villagers = db.relationship('IslandVillagers', back_populates='villagers')
    wanted = db.relationship('VillagersWanted', back_populates='villagers')
    notes = db.relationship('Notes', back_populates='villagers')