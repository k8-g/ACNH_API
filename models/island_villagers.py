from init import db

class IslandVillagers(db.Model):
    __tablename__ = "island_villagers"

    island_villagers_id = db.Column(db.Integer, primary_key=True)
    island_id = db.Column(db.Integer, db.ForeignKey('island.island_id'), nullable=False)
    villager_id = db.Column(db.Integer, db.ForeignKey('villager.villager_id'), nullable=False)
    comment_id = db.Column(db.Integer, db.ForeignKey('comments.comments_id'))

    # Relationships
    island = db.relationship('IslandUser', back_populates='island_villagers')
    villager = db.relationship('Villager', back_populates='island_villagers')
    comment = db.relationship('Comments', back_populates='island_villager')

    def __init__(self, island_id, villager_id, comment_id=None):
        self.island_id = island_id
        self.villager_id = villager_id
        self.comment_id = comment_id