from init import db

class Notes(db.Model):
    __tablename__ = "notes"

    notes_id = db.Column(db.Integer, primary_key=True)
    wanted_id = db.Column(db.Integer, db.ForeignKey('villagers_wanted.wanted_id', name='fk_notes_wanted'))
    villager_id = db.Column(db.Integer, db.ForeignKey('villagers.villager_id', name='fk_notes_villager'))
    notes = db.Column(db.Text, nullable=False)

    # Relationships
    wanted = db.relationship('VillagersWanted', back_populates='notes')
    villager = db.relationship('Villagers', back_populates='notes')

    def __init__(self, notes, wanted_id, villager_id):
        self.notes = notes
        self.wanted_id = wanted_id
        self.villager_id = villager_id