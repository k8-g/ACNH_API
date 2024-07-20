from init import db

class WantedVillagers(db.Model):
    __tablename__ = "wanted_villagers"

    id = db.Column(db.Integer, primary_key=True)

    island_id = db.Column(db.Integer, db.ForeignKey('island.id'), nullable=False)
    villager_id = db.Column(db.Integer, db.ForeignKey('villager.id'), nullable=False)
    
    island = db.relationship('Island')
    villager = db.relationship('Villager')

    # island = db.relationship('Island', back_populates='wanted_villagers')
    # villager = db.relationship('Villager', back_populates='wanted_villagers')

    # user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)