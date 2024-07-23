# connect inititialised modules to the flask application
import os

from flask import Flask
from marshmallow.exceptions import ValidationError

from init import db, ma, bcrypt, jwt

def create_app():
    app = Flask(__name__)

    app.json.sort_keys = False

    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")

    app.config["JWT_SECRET_KEY"] = os.environ.get("JWT_SECRET_KEY")

    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    @app.errorhandler(ValidationError)
    def validation_error(err):
        return {"error": err.messages}, 400


     # Import and register blueprints
    from controllers.cli_controller import db_commands
    app.register_blueprint(db_commands)

    from controllers.auth_controller import auth_bp
    app.register_blueprint(auth_bp)

    from controllers.island_controller import island_bp
    app.register_blueprint(island_bp)
  
    from controllers.villager_controller import villager_bp
    app.register_blueprint(villager_bp)
 
    from controllers.island_villagers_controller import island_villagers_bp
    app.register_blueprint(island_villagers_bp)

    from controllers.wanted_villagers_controller import wanted_villagers_bp
    app.register_blueprint(wanted_villagers_bp)

    # from controllers.notes_controller import notes_bp
    # app.register_blueprint(notes_bp)
    
    
    # Import models to ensure they are registered with SQLAlchemy
    from models.island import Island
    from models.villager import Villager
    from models.island_villager import IslandVillager
    from models.wanted_villagers import WantedVillagers

    # from models.note import Note

    # Import schemas to ensure they are registered with Marshmallow
    from schemas.island import IslandSchema, island_schema, islands_schema
    from schemas.villager import VillagerSchema, villager_schema, villagers_schema
    from schemas.island_villagers import IslandVillagerSchema, island_villager_schema, island_villagers_schema
    from schemas.wanted_villagers import WantedVillagerSchema, wanted_villager_schema, wanted_villagers_schema

    # from schemas.notes import NoteSchema, note_schema, notes_schema

    return app