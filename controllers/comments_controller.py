from flask import Blueprint, request
from init import db
from models.comment import Comment
from schemas.comment import comments_schema, comment_schema
from flask_jwt_extended import jwt_required

# Create a blueprint
comments_bp = Blueprint('comments', __name__)

@comments_bp.route('/comments', methods=['GET'])
def get_comments():
    comments = Comment.query.all()
    return comments_schema.dump(comments), 200

@comments_bp.route('/comments/<int:id>', methods=['GET'])
def get_comment(id):
    comment = Comment.query.get_or_404(id)
    return comment_schema.dump(comment), 200

@comments_bp.route('/comments', methods=['POST'])
@jwt_required()
def add_comment():
    data = request.get_json()
    new_comment = Comment(
        island_comments=data['island_comments']
        # island_villagers_id=data.get('island_villagers_id', None),
        # wanted_id=data.get('wanted_id', None)
    )
    db.session.add(new_comment)
    db.session.commit()
    return comment_schema.dump(new_comment), 201

@comments_bp.route('/comments/<int:id>', methods=['PUT'])
@jwt_required()
def update_comment(id):
    comment = Comment.query.get_or_404(id)
    data = request.get_json()
    comment.island_comments = data['island_comments']
    # comment.island_villagers_id = data.get('island_villagers_id', comment.island_villagers_id)
    # comment.wanted_id = data.get('wanted_id', comment.wanted_id)
    db.session.commit()
    return comment_schema.dump(comment), 200

@comments_bp.route('/comments/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_comment(id):
    comment = Comment.query.get_or_404(id)
    db.session.delete(comment)
    db.session.commit()
    return {"message": "Comment deleted"}, 200