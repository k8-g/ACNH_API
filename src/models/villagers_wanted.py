from init import db

class VillagersWanted(db.Model):
    __tablename__ = "villagers_wanted"

    wanted_id = db.Column(db.Integer, primary_key=True)
    requirements = db.Column(db.Text, nullable=False)

    # user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)