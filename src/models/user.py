from init import db, ma
from marshmallow import fields
# from marshmallow.validate import Regexp


class User(db.Model):
    # name of the table
    __tablename__ = "users"

    # attributes of the table
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    islands = db.relationship("Island", back_populates="user")
    villagers = db.relationship('Villager', back_populates='user')
    notes = db.relationship('Note', back_populates="user")
    comments = db.relationship("Comment", back_populates="user")


class UserSchema(ma.Schema):
    islands = fields.List(fields.Nested('IslandSchema', exclude=["user"]))
    villagers = fields.List(fields.Nested('VillagerSchema', exclude=["user"]))
    comments = fields.List(fields.Nested('CommentSchema', exclude=["user"]))
    island_villagers = fields.List(fields.Nested('IslandVillagerSchema'))

    # email = fields.String(required=True, validate=Regexp("^\S+@\S+\.\S+$", error="Invalid Email Format"))

    # password = fields.String(required=True, validate=Regexp("^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$", error="Minimum eight characters, at least one letter and one number"))

    class Meta:
        fields = ("id", "name", "email", "password", "is_admin", "islands", "comments")


# to handle a single user object
user_schema = UserSchema(exclude=["password"])

# to handle a list of user objects
users_schema = UserSchema(many=True, exclude=["password"])