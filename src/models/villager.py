from init import db

class Villager(db.Model):
    __tablename__ = "villager"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    gender = db.Column(db.String, nullable=False)
    species = db.Column(db.String, nullable=False)
    personality = db.Column(db.String, nullable=False)
    birthday = db.Column(db.String, nullable=False)
    catchphrase = db.Column(db.String, nullable=False)
    hobbies = db.Column(db.String, nullable=False)

    # # Relationships
    # island_villagers = db.relationship('IslandVillager', back_populates='villager')
    # wanted_villagers = db.relationship('WantedVillager', back_populates='villager')

    # foreign keys
    # user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    # island_id = db.Column(db.Integer, db.ForeignKey('island.island_id'), nullable=False)

    # field that has info about the user
    # user = db.relationship('User', back_populates='villagers')
    # islands = db.relationship("Island", back_populates="villagers")
    # comments = db.relationship('Comment', back_populates='villager')

    # notes = db.relationship('Note', back_populates="villagers")
    