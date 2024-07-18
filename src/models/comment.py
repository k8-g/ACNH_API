from init import db

class Comment(db.Model):
    __tablename__ = "comment"

    comments_id = db.Column(db.Integer, primary_key=True)
    # island_villagers_id = db.Column(db.Integer, db.ForeignKey('island_villagers.island_villagers_id', name='fk_comments_island_villagers'))
    # wanted_id = db.Column(db.Integer, db.ForeignKey('villagers_wanted.wanted_id', name='fk_comments_wanted'))
    island_comments = db.Column(db.Text, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)