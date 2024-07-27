from init import db

class Island(db.Model):
    # name of the table
    __tablename__ = "island"

    # attributes of the table
    id = db.Column(db.Integer, primary_key=True) 
    island_name = db.Column(db.String, nullable=False)

    # Foreign key to link back to User table
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    # Relationships
    user = db.relationship('User', backref='islands')
    
