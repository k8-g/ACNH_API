from init import db

class IslandVillager(db.Model):
    __tablename__ = "island_villager"

    island_villager_id = db.Column(db.Integer, primary_key=True)
    # island_id = db.Column(db.Integer, db.ForeignKey('islands.island_id', name='fk_island_villagers_island'), nullable=False)
    # villager_id = db.Column(db.Integer, db.ForeignKey('villagers.villager_id', name='fk_island_villagers_villager'), nullable=False)
    # comment_id = db.Column(db.Integer, db.ForeignKey('comments.comments_id', name='fk_island_villagers_comment'))

    # Relationships
    # island = db.relationship('IslandUser', back_populates='island_villagers')
    # villager = db.relationship('Villager', back_populates='island_villagers')
    # comments = db.relationship('Comments', back_populates='island_villager', foreign_keys=[comment_id])

    # def __init__(self, island_id, villager_id, comment_id=None):
    #     self.island_id = island_id
    #     self.villager_id = villager_id
    #     self.comment_id = comment_id