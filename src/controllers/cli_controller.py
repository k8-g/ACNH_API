import csv
import os

from flask import Blueprint

from init import db, bcrypt

from models.user import User
from models.island import Island
from models.villager import Villager
from models.island_villager import IslandVillager
from models.wanted_villagers import WantedVillagers
from models.note import Note

db_commands = Blueprint("db", __name__)

# Creating a command function for creating tables
@db_commands.cli.command("create")
def create_tables():
    db.create_all()
    print("Tables created")

# Creating a command function for dropping tables
@db_commands.cli.command("drop")
def drop_tables():
    db.drop_all()
    print("Tables dropped")

# Creating a command function for seeding tables
@db_commands.cli.command("seed")
def seed_tables():
    # Seed data
    # Example admin and users
    users = [
        # user 0
        User(
        name="Admin",
        email="admin@email.com",
        password=bcrypt.generate_password_hash("123456").decode("utf-8"),
        is_admin=True
        ),
        #user 1
        User(
            name="Kate",
            email="kate@email.com",
            password=bcrypt.generate_password_hash("123456").decode("utf-8"),
        ),
        # user 2
        User(
            name="Isaboo",
            email="isabelle@puppy.com",
            password=bcrypt.generate_password_hash("123456").decode("utf-8"),
        )
    ]
    db.session.add_all(users)
    db.session.commit()

    # Refresh the session to get the IDs
    db.session.refresh(users[0])
    db.session.refresh(users[1])
    db.session.refresh(users[2])

    # Example islands belonging to created users above
    islands = [
        Island(
            island_name="Zorlandia",
            user_id=users[1].id
        ),
        Island(
            island_name="PuppyLand",
            user_id=users[2].id
        ),
    ]

    # Add users & islands to the database session
    db.session.add_all(users)
    db.session.add_all(islands)
    db.session.commit()


    # Define the path to the CSV file
    csv_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'acnh_villager_data.csv')

    # Check if the file exists
    if not os.path.exists(csv_path):
        print(f"Error: CSV file not found at path: {csv_path}")
        return

    # Read villager data from CSV file
    with open(csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        villagers = []
        for row in reader:
            villager = Villager(
                id=int(row['id']),
                name=row['name'],
                gender=row['gender'],
                species=row['species'],
                personality=row['personality'],
                birthday=row['birthday'],
                catchphrase=row['catchphrase'],
                hobbies=row['hobbies']
            )
            villagers.append(villager)
    # Add villager data to the database session
    db.session.bulk_save_objects(villagers)
    db.session.commit()

    # Example IslandVillagers belonging to Island Zorlandia of user Kate
    island_villagers = [
        IslandVillager(
	        island_id=1,
	        villager_id=430
        ),
        IslandVillager(
	        island_id=1,
	        villager_id=285
        ),
        IslandVillager(
	        island_id=1,
	        villager_id=77
        ),
        IslandVillager(
	        island_id=1,
	        villager_id=87
        ),        
        IslandVillager(
	        island_id=1,
	        villager_id=165
        ),
        IslandVillager(
	        island_id=1,
	        villager_id=328
        ),
        IslandVillager(
	        island_id=1,
	        villager_id=57
        )
    ]

   

    db.session.add_all(island_villagers)
    db.session.commit()

    # Exampled WantedVillagers for Zorlandia for user Kate
    wanted_villagers = [
    WantedVillagers(
        villager_id=Villager.query.filter_by(name="Gloria").first().id,
        island_id=1
    ),
    WantedVillagers(
        villager_id=Villager.query.filter_by(name="Gwen").first().id,
        island_id=1
    )
]

    db.session.add_all(wanted_villagers)
    db.session.commit()

    # Example notes for WantedVillagers for Zorlandia
    # notes = [
    #     Note(
    #         wanted_villagers_id=1,
    #         notes="She has purple hair & pretty makeup."
    #     ),
    #     Note(
    #     wanted_villagers_id=3,
    #     notes="She has purple hair & pretty makeup too."
    #     )
    # ]
    # db.session.add_all(notes)
    # db.session.commit()

    print("Tables seeded")