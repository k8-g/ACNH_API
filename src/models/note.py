from init import db


class Note(db.Model):
    __tablename__ = "notes"

    id = db.Column(db.Integer, primary_key=True)
    notes = db.Column(db.String, nullable=True)

    wanted_villagers_id = db.Column(db.Integer, db.ForeignKey('wanted_villagers.id'), nullable=False)


    # Relationship
    # wanted_villagers = db.relationship('WantedVillagers')

    wanted_villager = db.relationship('WantedVillagers', back_populates='notes')



    # user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    # island_id = db.Column(db.Integer, db.ForeignKey('island.id'), nullable=False)
    # villager_id = db.Column(db.Integer, db.ForeignKey('villager.id'), nullable=False)


    # user = db.relationship('User', back_populates='notes')
    # islands = db.relationship("Island", back_populates="notes")
    # villager = db.relationship('Villager', back_populates='notes')