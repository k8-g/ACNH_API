from init import ma
from marshmallow import fields

class CommentSchema(ma.Schema):
    class Meta:
        fields = ("comment_id", "island_comments")
        # fields = ("comments_id", "island_villagers_id", "wanted_id", "island_comments")

    # island_villager = fields.Nested('IslandVillagersSchema', exclude=('comments',))
    # wanted = fields.Nested('VillagersWantedSchema', exclude=('comments',))

# to handle a single comment object
comment_schema = CommentSchema()

# to handle a list of comment objects
comments_schema = CommentSchema(many=True)