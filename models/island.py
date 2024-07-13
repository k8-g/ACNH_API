from init import db, ma

class IslandUser(db.Model):
    # name of the table
    __tablename__ = "Islands"

    island_id = db.Column(db.Integer, primary_key=True)
    name_of_island = db.Column(db.String, nullable=False)
    owner_of_island = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)