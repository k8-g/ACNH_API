from init import db

class Villager(db.Model):
    __tablename__ = "villager"

    villager_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    gender = db.Column(db.String, nullable=False)
    species = db.Column(db.String, nullable=False)
    personality = db.Column(db.String, nullable=False)
    birthday = db.Column(db.String, nullable=False)
    catchphrase = db.Column(db.String, nullable=False)
    hobbies = db.Column(db.String, nullable=False)

   # island_id = db.Column(db.Integer, db.ForeignKey('island_user.island_id'), nullable=False)

    notes = db.relationship('Note', back_populates="villager")
    