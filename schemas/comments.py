from init import ma
from marshmallow import fields

class CommentsSchema(ma.Schema):
    class Meta:
        fields = ("comments_id", "island_villagers_id", "wanted_id", "island_comments")

    island_villager = fields.Nested('IslandVillagersSchema', exclude=('comments',))
    wanted = fields.Nested('VillagersWantedSchema', exclude=('comments',))

# to handle a single comment object
comment_schema = CommentsSchema()

# to handle a list of comment objects
comments_schema = CommentsSchema(many=True)