from init import db

class Villager(db.Model):
    # name of table
    __tablename__ = "villager"

    # arributes of the table
    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String, nullable=False)
    gender = db.Column(db.String, nullable=False)
    species = db.Column(db.String, nullable=False)
    personality = db.Column(db.String, nullable=False)
    birthday = db.Column(db.String, nullable=False)
    catchphrase = db.Column(db.String, nullable=False)
    hobbies = db.Column(db.String, nullable=False)

# Villager is pre-set data, read-only for normal users
# Only an admin can Create, Update or Delete a villager's data