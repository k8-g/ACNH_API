# import pandas as pd
import csv
import os

from flask import Blueprint

from init import db, bcrypt

from models.user import User
from models.island import Island
from models.villager import Villager
from models.wanted_villagers import WantedVillagers
from models.note import Note

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
    users = [
            User(
            name="Admin",
            email="admin@email.com",
            password=bcrypt.generate_password_hash("123456").decode("utf-8"),
            is_admin=True
        ),
    User(
        #user 0
        name="Kate",
        email="kate@email.com",
        password=bcrypt.generate_password_hash("123456").decode("utf-8"),
        is_admin=True
    ),
    User(
        # user 1
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

    islands = [
        Island(
            island_name="Zorlandia",
            user_id=users[0].id
        ),
        Island(
            island_name="PuppyLand",
            user_id=users[1].id
        ),
    ]

    # villagers = [
    #     Villager(
    #         # villager_id=430,
    #         name="Judy",
    #         gender="Female",
    #         species="Bear cub",
    #         personality="Snooty",
    #         birthday="March 10",
    #         catchphrase="myohmy",
    #         hobbies="music"
    #     )
    # ]

    # wanted_villagers = [
    # WantedVillagers(
    #     island_id=islands[0].id,
    #     villager_id=villagers[0].id
    # )
    # ]

    # notes = [
    #     Note(
            
    #         wanted_villagers_id=wanted_villagers[0].id,
    #         notes="She is pretty"
    #     )
    # ]
    # ALWAYS PUT COMMA AFTER EACH LINE ^

    # Add islands to the database session
    db.session.add_all(users)
    db.session.add_all(islands)
    # db.session.add_all(villagers)
    # db.session.add_all(wanted_villagers)
    # db.session.add_all(notes)
    db.session.commit()



    # # Read villager data from CSV file
    # df = pd.read_csv('')
    # villagers = []
    # for index, row in df.iterrows():
    #     villager = Villager(
    #         id=row['id'],
    #         name=row['name'],
    #         gender=row['gender'],
    #         species=row['species'],
    #         personality=row['personality'],
    #         birthday=row['birthday'],
    #         catchphrase=row['catchphrase'],
    #         hobbies=row['hobbies']
    #     )
    #     villagers.append(villager)


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





    db.session.bulk_save_objects(villagers)
    db.session.commit()


    print("Tables seeded")