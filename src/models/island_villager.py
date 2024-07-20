from init import db

class IslandVillager(db.Model):
    __tablename__ = "island_villager"

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String, nullable=True)

    # Foreign keys
    island_id = db.Column(db.Integer, db.ForeignKey("island.id"), nullable=False)
    villager_id = db.Column(db.Integer, db.ForeignKey("villager.id"), nullable=False)
    
    island = db.relationship('Island')
    villager = db.relationship('Villager')

    # island = db.relationship('Island', back_populates='island_villagers')
    # villager = db.relationship('Villager', back_populates='island_villagers')

    # Relationship to other tables
    # island = db.relationship('Island')
    # villager = db.relationship('Villager')

    # user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    # comment_id = db.Column(db.Integer, db.ForeignKey("comments.id"), nullable=False)

    # user = db.relationship('User', back_populates='island_villagers')
    # villagers = db.relationship('Villager', back_populates='island_villager')
    # comments = db.relationship('Comment', back_populates='island_villager')
