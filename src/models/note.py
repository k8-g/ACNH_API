from init import db

class Note(db.Model):
    __tablename__ = "note"

    note_id = db.Column(db.Integer, primary_key=True)
    note = db.Column(db.String)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    island_id = db.Column(db.Integer, db.ForeignKey('island.island_id'), nullable=False)
    villager_id = db.Column(db.Integer, db.ForeignKey('villager.villager_id'), nullable=False)

    
    # wanted_id = db.Column(db.Integer, db.ForeignKey('villagers_wanted.wanted_id', nullable=False)

    user = db.relationship('User', back_populates='notes')
    islands = db.relationship("Island", back_populates="notes")
    villager = db.relationship('Villager', back_populates='notes')