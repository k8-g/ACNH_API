# for initilising all the libraries

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
ma = Marshmallow()
bcrypt = Bcrypt()
jwt = JWTManager()

from models.user import User
from models.island import Island
from models.villager import Villager
from models.wanted_villagers import WantedVillagers
from models.note import Note
from models.island_villager import IslandVillager
