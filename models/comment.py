from init import db

class Comment(db.Model):
    __tablename__ = "comment"

    comments_id = db.Column(db.Integer, primary_key=True)
    # island_villagers_id = db.Column(db.Integer, db.ForeignKey('island_villagers.island_villagers_id', name='fk_comments_island_villagers'))
    # wanted_id = db.Column(db.Integer, db.ForeignKey('villagers_wanted.wanted_id', name='fk_comments_wanted'))
    island_comments = db.Column(db.Text, nullable=False)

    # Relationships
    # island_villager = db.relationship('IslandVillagers', back_populates='comments', foreign_keys=[island_villagers_id])
    # wanted = db.relationship('VillagersWanted', back_populates='comments', foreign_keys=[wanted_id])

    # def __init__(self, island_comments, island_villagers_id=None, wanted_id=None):
    #     self.island_comments = island_comments
    #     self.island_villagers_id = island_villagers_id
    #     self.wanted_id = wanted_id