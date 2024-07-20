# from init import db
# from marshmallow import fields

# class Comment(db.Model):
#     __tablename__ = "comment"

#     comments_id = db.Column(db.Integer, primary_key=True)
#     comments = db.Column(db.Text, nullable=False)
#     date = db.Column(db.Date) # date created

#     user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
#     island_id = db.Column(db.Integer, db.ForeignKey("island.id"), nullable=False)
#     # villager_id = db.Column(db.Integer, db.ForeignKey("villager.id"), nullable=False)

#     user = db.relationship('User', back_populates='comments')
#     island = db.relationship('Island', back_populates='comments')
#     # villager = db.relationship('Villager', back_populates='comments')
#     island_villager = db.relationship('IslandVillager', back_populates='comments')