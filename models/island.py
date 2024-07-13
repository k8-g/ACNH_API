from init import db, bcrypt

class IslandUser(db.Model):
    # name of the table
    __tablename__ = "islands"

    island_id = db.Column(db.Integer, primary_key=True)
    name_of_island = db.Column(db.String, nullable=False)
    owner_of_island = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    # Back reference to IslandVillagers and VillagersWanted
    island_villagers = db.relationship('IslandVillagers', back_populates='islands')
    wanted = db.relationship('VillagersWanted', back_populates='islands')

    def __init__(self, name_of_island, owner_of_island, password, is_admin=False):
        self.name_of_island = name_of_island
        self.owner_of_island = owner_of_island
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')
        self.is_admin = is_admin