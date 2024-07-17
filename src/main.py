# connect inititialised modules to the flask application
import os

from flask import Flask

from init import db, ma, bcrypt, jwt

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")

    app.config["JWT_SECRET_KEY"] = os.environ.get("JWT_SECRET_KEY")

    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

     # Import and register blueprints
    from controllers.cli_controller import db_commands
    app.register_blueprint(db_commands)

    from controllers.auth_controller import auth_bp
    app.register_blueprint(auth_bp)

    from controllers.island_controller import island_bp
    app.register_blueprint(island_bp, url_prefix='/')
    
    from controllers.villager_controller import villager_bp
    app.register_blueprint(villager_bp, url_prefix='/')
    
    from controllers.notes_controller import notes_bp
    app.register_blueprint(notes_bp, url_prefix='/')

    # from controllers.island_villagers_controller import island_villagers_bp
    # app.register_blueprint(island_villagers_bp)

    # from controllers.villagers_wanted_controller import villagers_wanted_bp
    # app.register_blueprint(villagers_wanted_bp)

    # from controllers.comments_controller import comments_bp
    # app.register_blueprint(comments_bp)


    
    
    # Import models to ensure they are registered with SQLAlchemy
    from models.island import Island
    # from models.villager import Villager
    # from models.island_villager import IslandVillager
    # from models.villagers_wanted import VillagersWanted
    # from models.comment import Comment
    # from models.note import Note

    # Import schemas to ensure they are registered with Marshmallow
    from schemas.island import IslandSchema, island_schema, islands_schema
    # from schemas.villager import VillagerSchema, villager_schema, villagers_schema
    # from schemas.island_villagers import IslandVillagerSchema, island_villager_schema, island_villagers_schema
    # from schemas.villagers_wanted import VillagersWantedSchema, villager_wanted_schema, villagers_wanted_schema
    # from schemas.comment import CommentSchema, comment_schema, comments_schema
    # from schemas.notes import NoteSchema, note_schema, notes_schema

    return app