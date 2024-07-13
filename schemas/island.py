from init import ma


class IslandSchema(ma.Schema):
    class Meta:
        fields = ("island_id", "name_of_island", "owner_of_island", "password", "is_admin")

# to handle a single island object
island_schema = IslandSchema(exclude=["password"])

# to handle a list of island objects
islands_schema = IslandSchema(many=True, exclude=["password"])


# What Simon used in class:
# class UserSchema(ma.Schema):
#     class Meta:
#         fields = ("island_id", "name_of_island", "owner_of_island", "password", "is_admin")

# # to handle a single user object
# user_schema = IslandUserSchema(exclude=["password"])

# # to handle a list of user objects
# users_schema = IslandUserSchema(many=True, exclude=["password"])


