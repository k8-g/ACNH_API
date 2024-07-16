from flask import Blueprint

from init import db, bcrypt

from models.island import Island

db_commands = Blueprint("db", __name__)

@db_commands.cli.command("create")
def create_tables():
    db.create_all()
    print("Tables created")

@db_commands.cli.command("drop")
def drop_tables():
    db.drop_all()
    print("Tables dropped")

@db_commands.cli.command("seed")
def seed_tables():
    # Example seed data
    islands = [
        Island(
            name_of_island="Zorlandia",
            owner_of_island="Kate",
            password=bcrypt.generate_password_hash("123456").decode("utf-8"),
            is_admin=True
        ),
        Island(
            name_of_island="Second Island",
            owner_of_island="Katherine",
            password=bcrypt.generate_password_hash("123456").decode("utf-8"),
            is_admin=False
        ),
        # Add more Islands as needed
    ]
    
    # Add islands to the database session
    db.session.add_all(islands)
    db.session.commit()
    print("Tables seeded")