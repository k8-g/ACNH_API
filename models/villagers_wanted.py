from init import db

class VillagersWanted(db.Model):
    __tablename__ = "villagers_wanted"

    wanted_id = db.Column(db.Integer, primary_key=True)
    villager_id = db.Column(db.Integer, db.ForeignKey('villagers.villager_id', name='fk_villagers_wanted_villager'), nullable=False)
    island_id = db.Column(db.Integer, db.ForeignKey('islands.island_id', name='fk_villagers_wanted_island'), nullable=False)
    item_name = db.Column(db.String, nullable=False)
    requirement_description = db.Column(db.Text, nullable=False)
    required_materials = db.Column(db.Text, nullable=False)
    notes_id = db.Column(db.Integer, db.ForeignKey('notes.notes_id', name='fk_villagers_wanted_notes'))

    # Relationships
    villager = db.relationship('Villager', back_populates='wanted')
    island = db.relationship('IslandUser', back_populates='wanted')
    notes = db.relationship('Notes', back_populates='wanted')

    # Relationships
    villager = db.relationship('Villager', back_populates='wanted')
    island = db.relationship('IslandUser', back_populates='wanted')
    notes = db.relationship('Notes', back_populates='wanted')
    comments = db.relationship('Comments', back_populates='wanted')

    def __init__(self, villager_id, island_id, item_name, requirement_description, required_materials, notes_id=None):
        self.villager_id = villager_id
        self.island_id = island_id
        self.item_name = item_name
        self.requirement_description = requirement_description
        self.required_materials = required_materials
        self.notes_id = notes_id