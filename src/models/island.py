from init import db

class Island(db.Model):
    # name of the table
    __tablename__ = "island"

    # attributes of the table
    id = db.Column(db.Integer, primary_key=True)
    island_name = db.Column(db.String, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    # Relationships
    # user = db.relationship('User', back_populates='islands')
    user = db.relationship('User', backref='islands')
    
    # island_villagers = db.relationship('IslandVillager', back_populates='island')
    # wanted_villagers = db.relationship('WantedVillager', back_populates='island')

    # user = db.relationship('User')
    # user = db.relationship('User', back_populates='islands')
    # villagers = db.relationship('Villager', back_populates='island')
    # comments = db.relationship('Comment', back_populates='island')
    # cascade part = if an island is deleted, the comments get deleted too
    # comments = db.relationship('Comment', back_populates='island', cascade="all, delete")
    # notes = db.relationship('Note', back_populates="islands")