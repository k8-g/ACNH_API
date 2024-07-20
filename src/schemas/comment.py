# from init import ma
# from marshmallow import fields

# class CommentSchema(ma.Schema):

#     user = fields.Nested('UserSchema', only=["name","id"])
#     island = fields.Nested('IslandSchema', exclude=["comments"])
#     # villager = fields.Nested('VillagerSchema', exclude=["comments"])
#     island_villager = fields.Nested('IslandVillagerSchema', exclude=['comments'])


#     class Meta:
#         # fields = ("comment_id", "comments", "date,", "user", "island",)
#         # fields = ("comment_id", "comments", "date,", "user", "island", "villager")
#         fields = ("comment_id", "comments", "date,", "user", "island", "island_villager")

# # to handle a single comment object
# comment_schema = CommentSchema()

# # to handle a list of comment objects
# comments_schema = CommentSchema(many=True)