from init import db

class Island(db.Model):
    # name of the table
    __tablename__ = "island"

    # attributes of the table
    island_id = db.Column(db.Integer, primary_key=True)
    island_name = db.Column(db.String, nullable=False)


    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    user = db.relationship('User', back_populates='islands')
    # notes = db.relationship('Note', back_populates="owner")

    # villagers = db.relationship('Villager', back_populates='island')