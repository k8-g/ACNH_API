import functools 
# from functools import wraps

from flask_jwt_extended import get_jwt_identity

from init import db
from models.user import User
# from models.island import Island




def authorise_as_admin():
    # get the user's id from jwt identity
    user_id = get_jwt_identity()
    # fetch the user from the db
    stmt = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(stmt)
    # check whether the user is an admin or not
    return user.is_admin

def auth_as_admin_decorator(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        # get the user's id from get_jwt_identity
        user_id = get_jwt_identity()
        # fetch the entire user using the id
        stmt = db.select(User).filter_by(id=user_id)
        user = db.session.scalar(stmt)
        # if user is an admin
        if user.is_admin:
            # allow the decorated function to execute
            return fn(*args, **kwargs)
        # else (user is not an admin)
        else:
            # return error
            return {"error": "Only admin can perform this action"}, 403

    return wrapper


# def check_if_owner(fn):
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         user_id = get_jwt_identity()
#         island_id = kwargs.get('island_id')
#         stmt = db.select(Island).filter_by(id=island_id)
#         island = db.session.scalar(stmt)
#         if not island:
#             return {"error": f"Island with id {island_id} not found"}, 404
#         if str(island.user_id) != user_id:
#             return {"error": "You are not the owner of this island."}, 403
#         return fn(*args, **kwargs)
#     return wrapper