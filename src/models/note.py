from init import db


class Note(db.Model):
    # name of table
    __tablename__ = "notes"

    # Attributes of table
    id = db.Column(db.Integer, primary_key=True)
    notes = db.Column(db.String, nullable=True)
    # Foreign keys
    wanted_villagers_id = db.Column(db.Integer, db.ForeignKey('wanted_villagers.id'), nullable=False)


    # Relationship
    # Notes links back to WantedVillagers
    wanted_villager = db.relationship('WantedVillagers', back_populates='notes')

    # Each WantedVillager can have one or more Notes
