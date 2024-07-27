# Kate Gerber's Animal Crossing Database API

[Github Link](https://github.com/k8-g/ACNH_API)

[Installation Doc](/installation%20doc.md)

## R1. Explain the problem that this app will solve, and explain how this app solves or addresses the problem

So the goal of this app is, I want to allow someone to keep track of their villagers on their island for the Switch game, Animal Crossing: New Horizon (ACNH). 

This Flask app API will be so that one can keep track of the current villagers they have on their Animal Crossing island and also keep track of the villagers they want to collect, with the option to add comments and notes on both current and wishlisted villagers. A user can also read some data about different villagers available.

This API app consisists of several tables in the database; user, island, villagers, island villagers, wanted villagers and notes.


## R2. Describe the way tasks are allocated and tracked in your project.

A Trello board was extensively used throughout the entire duration of the project.

(Hopefully one of these links should link to the public board, otherwise screenshots can be found below)

[Trello link](https://trello.com/b/s8ynY9wW)

[Trello invite link](https://trello.com/invite/b/668e2e1b9b47a60e3686eeec/ATTI69ed715bb9450d852e0530ea65e0b8967121DED2/✿◡◡-kates-t2a2-api-webserver)

### Trello Screenshots

Trello board
![Trello board](/docs/Trello%20Screenshots/Trello%20board.png)


Rough ERD
![Draw rough ERD](/docs/Trello%20Screenshots/Draw%20rough%20ERD.png)


Submit Rough ERD
![Submit Rough ERD](/docs/Trello%20Screenshots/Submit%20rough%20ERD.png)


Updated ERD
![Updated ERD](/docs/Trello%20Screenshots/Updated%20ERD.png)


Feature/Authenication
![Feature/Authenication](/docs/Trello%20Screenshots/Feature:authenication.png)


Models
![Models](/docs/Trello%20Screenshots/Models.png)


Schemas
![Schemas](/docs/Trello%20Screenshots/Schemas.png)


Feature/Controllers
![Feature/Controllers](/docs/Trello%20Screenshots/Feature:controllers.png)


Feature/Islands
![Feature/Islands](/docs/Trello%20Screenshots/Feature:islands.png)


Feature/Villagers
![Feature/Villagers](/docs/Trello%20Screenshots/Feature:villagers.png)


Feature/WantedVillagers
![Feature/WantedVillagers](/docs/Trello%20Screenshots/Feature:wanted%20villagers.png)


Feature/Notes
![Feature/Notes](/docs/Trello%20Screenshots/Feature:notes.png)


Feature/Validation
![Feature/Validation](/docs/Trello%20Screenshots/Feature:validation.png)


Feature/Authorisation
![Feature/Authorisation](/docs/Trello%20Screenshots/Feature:authorisation.png)


Models/islands
![Models/islands](/docs/Trello%20Screenshots/Models:islands.png)


Models/villagers
![Models/villagers](/docs/Trello%20Screenshots/Models:villagers.png)


Models/island_villagers
![Models/island_villagers](/docs/Trello%20Screenshots/Models:island_villagers.png)


Models/wanted_villagers
![Models/wanted_villagers](/docs/Trello%20Screenshots/Feature:wanted%20villagers.png)


Models/notes
![Models/notes](/docs/Trello%20Screenshots/Models:note.png)


Models/user
![Models/user](/docs/Trello%20Screenshots/Models:user.png)


Add Villager data
![Add Villager data](/docs/Trello%20Screenshots/Add%20villager%20data.png)


Add email lowercase code
![Add email lowercase](/docs/Trello%20Screenshots/Add%20email%20lowercase.png)


## R3. List and explain the third-party services, packages and dependencies used in this app.

**Libraries installed:**

- flask_bcrypt
    - bcrypt==4.1.3
	- Flask-Bcrypt==1.0.1
        - A library for hashing passwords. It’s used to enhance security by storing hashed passwords instead of plaintext.

- psycopg2-binary
    - psycopg2-binary==2.9.9
        - A PostgreSQL adapter for Python. It’s used to connect and interact with PostgreSQL databases.

- flask_sqlalchemy
    - Flask-SQLAlchemy==3.1.1
    - SQLAlchemy==2.0.31
        - An extension that simplifies the use of SQLAlchemy, the Python SQL toolkit, with Flask. It provides ORM (Object Relational Mapping) support for working with databases.

- flask_marshmallow
    - flask-marshmallow==1.2.1
        - Integrates the Flask web framework with the Marshmallow object serialization/deserialization library. This is used for data validation and formatting.

- marshmallow_sqlalchemy
    - marshmallow-sqlalchemy==1.0.0
        - An integration library that connects Marshmallow with SQLAlchemy. It helps in serializing and deserializing SQLAlchemy models.

- flask_jwt_extended
    - Flask-JWT-Extended==4.6.0
        - An extension for Flask that adds support for creating JSON Web Tokens (JWT). JWT is used for securely transmitting information between parties as a JSON object.

- python-dotenv
    - python-dotenv==1.0.1
        - A library that loads environment variables from a .env file into the environment. This helps manage configuration.


**General Flask Libraries**
- blinker==1.8.2
  - Provides support for creating and managing signals in Python applications. It’s commonly used for event handling in Flask applications.

- click==8.1.7
    - A package used to create command-line interfaces (CLI). It’s used by Flask for its CLI commands.

- Flask==3.0.3
    - A lightweight WSGI web application framework in Python. Flask provides the essential tools and libraries to build web applications, APIs, and more.

- itsdangerous==2.2.0
    - A package used for cryptographic signing in Python. Flask uses it for securely signing data, such as cookies.

- Jinja2==3.1.4
    - A templating engine for Python. Flask uses Jinja2 to render HTML templates.

- MarkupSafe==2.1.5
    - A library that provides a way to safely handle strings with potentially unsafe characters. It’s used by Jinja2.

- Werkzeug==3.0.3
    - A comprehensive WSGI web application library. It’s used by Flask for handling HTTP requests and responses.


**General Python Libraries**
- marshmallow==3.21.3
    - An object serialization/deserialization library. It helps convert complex data types to and from native Python data types.

- numpy==2.0.1
    - A package for numerical computing in Python. It provides support for large, multi-dimensional arrays and matrices.

- packaging==24.1

- PyJWT==2.8.0
    - A Python library for creating and verifying JSON Web Tokens (JWT).

- python-dateutil==2.9.0.post0
    - A library that provides powerful extensions to the standard datetime module.

- pytz==2024.1
    - A library that provides accurate and cross-platform timezone calculations.

- six==1.16.0
    - A compatibility library for writing code that works on both Python 2 and 3.

- typing_extensions==4.12.2
    - A backport of typing features for older versions of Python.

- tzdata==2024.1
    - timezone data for use with pytz.


## R4. Explain the benefits and drawbacks of this app’s underlying database system.

Benefits of PostgreSQL

- Reliability:
    - PostgreSQL ensures your data is safe and consistent, even if something goes wrong during a transaction.
- Versatile Data Handling:
    - It can store and manage various types of data, including JSON, arrays, and more complex structures.
- Search Capabilities:
    - PostgreSQL can efficiently search through large amounts of text data, which is useful for finding specific information quickly.
- Customizable:
    - You can add custom functions and types, making it flexible to suit your specific needs.
- Strong Support:
    - There’s a large community and plenty of resources available for help and guidance.
- Security:
    - It offers robust security features to protect your data from unauthorized access.
- Scalable:
    - PostgreSQL can handle large volumes of data and many users, making it suitable for growing applications.

Drawbacks of PostgreSQL

- Complexity:
    - It can be complicated to set up and manage, requiring more knowledge and expertise.
- Performance Tuning:
    - To get the best performance, you might need to spend time optimizing settings and queries.
- Resource Usage:
    - PostgreSQL can use a lot of memory and storage, which might be a problem for smaller setups.
- Configuration Overhead:
    - There are many settings to configure, which can be overwhelming and, if done incorrectly, can cause issues.
- Migration Challenges:
    -Moving data to or from PostgreSQL can be difficult, especially if you’re switching from a very different database system.

## R5. Explain the features, purpose and functionalities of the object-relational mapping system (ORM) used in this app.

Features of SQLAlchemy 

- Object-Relational Mapping (ORM):
    - SQLAlchemy provides an ORM that allows developers to map Python classes to database tables. This makes it easy to interact with the database using Python objects and methods instead of raw SQL queries.
- Declarative Syntax:
    - Using SQLAlchemy’s declarative syntax, you can define database schema by creating Python classes that represent tables. Each class attribute represents a column in the table.
- Query Building:
    - SQLAlchemy allows you to build complex queries using Python code. The ORM provides an easy-to-use query interface that abstracts the complexity of SQL.
- Relationship Management:
    - SQLAlchemy ORM supports defining relationships between tables such as one-to-many, many-to-one, and many-to-many. This makes it easier to manage related data.
- Session Management:
    - SQLAlchemy uses sessions to manage database operations. A session is used to interact with the database and keep track of changes to objects.

Purpose of SQLAlchemy ORM in the ACNH API

- Simplify Database Interactions:
    - The ORM abstracts the underlying database interactions, allowing you to work with Python objects instead of writing raw SQL queries. This simplifies the development process.
- Maintainability:
    - Using ORM helps in keeping the codebase clean and maintainable. Changes to the database schema can be made in the Python code, and the ORM takes care of syncing these changes with the database.
- Efficiency:
    - The ORM can optimize database access and improve performance by managing sessions and connections efficiently.

Functionalities of SQLAlchemy ORM in the ACNH API

- Define Models:
    - Each table in the database is represented by a Python class. For example, the User, Island, Villager, WantedVillagers, IslandVillager, and Note models represent different tables in the ACNH API.
- Create and Query Records:
    - You can create new records by creating instances of the model classes and saving them to the database session. Similarly, you can query records using the query interface provided by SQLAlchemy.
- Manage Relationships:
    - SQLAlchemy ORM manages relationships between different models, such as the relationship between User and Island, Island and Villager, etc. This allows you to easily fetch related data.
- Session Management:
    - SQLAlchemy’s session management ensures that all changes to the database are tracked and committed in a transactional way. This helps maintain data integrity.

## R6. Design an entity relationship diagram (ERD) for this app’s database, and explain how the relations between the diagrammed models will aid the database design. 
This should focus on the database design BEFORE coding has begun, eg. during the project planning or design phase.

![Original ERD](/docs/Draft%20ERDS/Draft1.ACNH_Villager_Collection_API_ERD11.png)

The ERD above, designed at the start of this project, had six sections;
- IslandUser
- Villagers
- IslandVillagers
- Comments
- WantedVillagers
- Notes

Relationships:
- IslandVillagers linked to IslandUser (Many to One)
- IslandVillagers linked to Villagers (Many to One)
- Comments linked to IslandVillagers (Many to One)
- Comments linked to WantedVillagers (Many to One)
- Villagers link to WantedVillagers (One to Many)
- WantedVillagers linked to IslandUser (Many to One)
- WantedVillagers linked to Villlagers (Many to One)
- WantedVillagers linked to Notes (One to Many)


- Each User can have one or more Islands (One to Many)
- Each IslandUser can have one or more/many IslandVillagers and WantedVillagers (One to Many)
- Each IslandVillager can have multiple comments (One to Many)
- Each WantedVillager can have multiple notes (One to Many)

I wanted this original design to have User/Island to be able to have multiple villagers saved in their island villager list and their wanted villager list. Each island villager could then have multiple comments, and each wanted villager could have multiple notes, so having them separate was my of keeping track of which section was which.

In having User & Island as one table, I realised that it was too confusing to me as in my mind, as one user can have one or more islands, and having User and Island as one table was too confusing for me and wasn't working for me, so I decided to change it to be updated ERD as mentioned in Q7, having separate tables for Island and User, and had to rework the entire code to add this new structure in.


## R7. Explain the implemented models and their relationships, including how the relationships aid the database implementation.

This should focus on the database implementation AFTER coding has begun, eg. during the project development phase.

The final ERD was done after I realised that the original and other draft ERD's (stored in the docs/Draft ERDS folder) were too complicated and I was struggling to work with a combined user/island table and made the decision to have a separate user table and separate island table, as it made more sense to me that way.

I also ended up removing the comments table as it was better to have a seperate notes section for Wanted Villagers to allow multiple notes on a Wanted Villager with Island Villagers having a single text field to allow for a comment if needed, but Wanted Villagers is the main section I wanted Notes, as there a user can add multiple notes keeping track of invite requirements or just simply write why they wanted the villager of what they like about that villager.

Final ERD as below:
![Final ERD](/docs/ACNH_API_ERD.png)

### The entities/tables:
(PK = Primary Key, FK = Foriegn Key)

- User: This table is where information about each user is stored for authenication and authorisation purposes. A user may update or delete their own user data.
(PK = Primary Key, FK = Foriegn Key)
    - `id` (PK): unique id number
    - `name`: The user's name
    - `email`: unique email address for logging in purposes
    - `password`: for allowing a particular user to access their data
    - `is_admin`: so that the API knows whether a user is an admin or not

- Island: This table represents different islands each user can keep track of. A user can have one or more islands, if they wish. A user may access, update or delete their own island.

    - `id` (PK): Unique identifier for each island.
    - `island_name`: Name of the island.
    - `user_id` (FK): The id from the user table to link an island to its user.

- Relationships:
    - Island links back to the User table to access user data for authorisation purposes
    ```
    user = db.relationship('User', backref='islands')
    ```

- Villager: This table holds the villager data. This data is only allowed to be updated or deleted by an admin.

    - `id` (PK): Unique identifier for each villager. This number has been set by the admin, using their matching amiibo number.
    - `name`: Name of the villager.
    - `gender`: Gender of the villager.
    - `species`: Species of the villager.
    - `personality`: Personality type of the villager.
    - `birthday`: Birthday of the villager.
    - `catchphrase`: Catchphrase of the villager.
    - `hobbies`: Hobbies of the villager.

- Villager data is a pre-filled data table purely for other tables to access its data, (READ-ONLY/GET), unless one has admin permission.
- Only an admin can Create (POST), Update (PATCH) or Delete (DELETE) a villager's data


- IslandVillager: This table is where a user may add a villager's data to a list to keep track of which villagers they currently have on their island.

    - `id` (PK): Unique identifier for each island_villager.
    - `island_id` (FK): Foreign key linking to the Island table.
    - `villager_id` (FK): Foreign key linking to the Villager table.
    - `text`: Allows a user to make a comment about said villager if they wish.

- Relationships:
    - IslandVillagers links back to Island table
    ```
    island = db.relationship('Island')
    ```
    - IslandVillagers links back to Villager table
    ```
    villager = db.relationship('Villager')
    ```

- WantedVillagers: This table represents the villagers that are wanted to be colleted on an island. A user can keep track of a list of villagers they want for their island.

    - `id` (PK): Unique identifier for each villager wanted.
    - `Villager_id` (FK): Foreign key linking to the Villagers table.
    - `island_id` (FK): Foreign key linking to the Island table.

- Relationships:
   - WantedVillagers links back to Island
   ```
    island = db.relationship('Island', backref='wanted_villagers')
    ```
    - WantedVillagers links back to Villager
    ```
    villager = db.relationship('Villager', backref='wanted_villagers')
    ```
    - WantedVillager links back to Note
    ```
    notes = db.relationship('Note', back_populates='wanted_villager')
    ```

- Notes: This table contains any notes a user might write about their Wanted Villagers. Here they can write what they might need to  invite a villager, what they like about them, etc.

    - `id` (PK): Unique identifier for each note.
    - `wanted_id` (FK): Foreign key linking to the WantedVillagers
    - `notes`: The note text.

-  Relationships:
    - Notes links back to WantedVillagers
    ```
    wanted_villager = db.relationship('WantedVillagers', back_populates='notes')
    ```

**Relationships and Their Significance**

- User
    - is accessed by Island table
    - contains all the user data

- Island links to User; Many-to-One
    - Each User can have one or more island
    - Each Island only has User
    - By linking Islands to Users, it ensures that each island has an owner, which helps in managing ownership and access control.


- Island to IslandVillagers: One-to-Many
    - Each island can have multiple island villagers residing on it.
    - Each island villager in a list can only be associated to one island.
    - Connecting IslandVillagers to Islands allows for tracking which villagers belong to which island, helping in organizing and managing island-specific data.

- Villager
    - is accessed by IslandVillager and WantedVillager
    - contains all the villager's data

- IslandVillager to Villager: Many-to-one. 
    - Each Villager can be associated with multiple IslandVillagers on different user's islands.
    - Each IslandVillager is associated with only one Villager.
    - This relationship helps in identifying and retrieving detailed information about villagers associated with each island, ensuring accurate data representation.

- WantedVillagers to Island: Many-to-one. 
    - Each Island can have multiple WantedVillagers
    - Each WantedVillager is associated with only one Island.
    - User information is acessed via island, which then accesses the User table.
    - By linking WantedVillagers to Islands, it makes it easy to track and manage the villagers that each island owner/user wants, aiding in user-specific and island-specific wishlist management.


- WantedVillagers to Villager: Many-to-one. 
    - Each Villager can be associated with multiple WantedVillagers. 
    - Each WantedVillager is associated with only one Villager.
    - Connecting WantedVillagers to allows in retrieving detailed information about each wanted villager, providing comprehensive data for the wanted villager list.

- Notes
    - is accessed by WantedVillagers
    - contains all the notes data

- Notes to WantedVillagers: Many-to-one. 
    - Each WantedVillager can have multiple Notes.
    - Each Note is associated with only one WantedVillager.
    - Connecting Notes to WantedVillagers allows users to add specific notes to their wanted villagers, enhancing the functionality by allowing detailed and personal remarks.



## R8. Explain how to use this application’s API endpoints. Each endpoint should be explained, including the following data for each endpoint:
- HTTP verb
- Path or route
- Any required body (json) or header data (auth/jwt)
- Response

### API Endpoints:

**Registering new user**

- HTTP verb: POST
- Route: http://localhost:8081/auth/register
- Any required body (json) or header data (auth/jwt):
    - Auth Bearer Token/JWT required - No

JSON body:
```
{
    "name": "Sami",
	"email": "Sami@kitty.com",
    "password": "password123"
}
```
Response:
```
{
	"id": 4,
	"name": "Sami",
	"email": "sami@kitty.com",
	"is_admin": false,
	"islands": []
}
```

 - Email converts to lowercase


![Insomnia test: POST Register New User](/docs/Screenshots/1.%20GET%20auth:register.png)

Fail: Missing required field

JSON body:
```
{
	"id": 4,
	"name": "Sami",

	"is_admin": false,
	"islands": []
}
```
Response:
```
{
	"error": {
		"email": [
			"Missing data for required field."
		]
	}
}
```

![Insomnia test: POST Register New User](/docs/Screenshots/1.%20GET%20auth:register%20fail.png)


**Logging in as registered user**
- HTTP verb: POST
- Route: http://localhost:8081/auth/login
- Any required body (json) or header data (auth/jwt):
    - Auth Bearer Token/JWT required - No
    
JSON Body:
```
{
	"name": "Sami",
	"email": "Sami@kitty.com",
  "password": "password123"
}
```
Response:
```
{
	"name": "Sami",
	"email": "sami@kitty.com",
	"id": 4,
	"is_admin": false,
	"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcyMTg0ODYxNywianRpIjoiZWZhYjVmMGEtNDZlMC00MjgyLTkyZDctZTE2NDUwNzIzYTc1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjQiLCJuYmYiOjE3MjE4NDg2MTcsImNzcmYiOiI1YzM3NzZmZS04MWVmLTRjMTQtOTMxOS1hMzBkZGEwNDJiMjciLCJleHAiOjE3MjE5MzUwMTd9.cWd_gnkazDZNgZoHhPD8-TK_FfqmMYGIl_b7wc2PeG4"
}
```

 - Email converts to lowercase

![Insomnia test: POST Login User](/docs/Screenshots/2.%20GET%20auth:login.png)

Fail: If incorrect email or password used
JSON Body:
```
{
	"name": "Sami",
	"email": "Sami@kitty.com",
  "password": "password124"
}
```
Response:
```
{
	"error": "Incorrect email or password"
}
```
![Insomnia test: POST Login User](/docs/Screenshots/2.%20GET%20auth:login%20fail.png)


**Deleting user**
- HTTP verb: DELETE
- Route: http://localhost:8081/auth/users/5
- Any required body (json) or header data (auth/jwt):
    - Auth Bearer Token/JWT required - Admin
    
JSON Body:
```
-
```
Response:
```
{
	"message": "User with id 5 deleted"
}
```

- Only an admin can delete a user

![Insomnia test: DELETE User](/docs/Screenshots/DELETE%20user.png)

Fail: If a non-admin user tries to delete
JSON Body:
```
-
```
Response:
```
{
	"error": "Only an admin can perform this action"
}
```
![Insomnia test: Delete User](/docs/Screenshots/DELETE%20user%20not%20admin.png)



**Creating an Island**

Logged in as New User Sami
- HTTP verb: POST
- Route: http://localhost:8081/islands
- Any required body (json) or header data (auth/jwt):
    - Auth Bearer Token/JWT required - User Sami
    
JSON body:

```
{
    "island_name": "KittyLand"
}
```
Response:
```
{
	"user": {
		"name": "Sami",
		"id": 4
	},
	"id": 3,
	"island_name": "KittyLand"
}
```

![Insomnia test: POST New Island](/docs/Screenshots/3.%20POST%20:islands.png)

Fail: Missing data field required

Response:
```
{
	"error": {
		"island_name": [
			"Missing data for required field."
		]
	}
}
```
![Insomnia test: POST New Island Fail](/docs/Screenshots/3.%20POST%20island%20fail.png)


**Get all islands**
- HTTP verb: GET
- Route: http://localhost:8081/islands
- Any required body (json) or header data (auth/jwt):
    - Auth Bearer Token/JWT required - No

JSON body:
```
-
```
Response:
```
[
	{
		"user": {
			"name": "Kate",
			"id": 2
		},
		"id": 1,
		"island_name": "Zorlandia"
	},
	{
		"user": {
			"name": "Isaboo",
			"id": 3
		},
		"id": 2,
		"island_name": "PuppyLand"
	},
	{
		"user": {
			"name": "Sami",
			"id": 4
		},
		"id": 3,
		"island_name": "KittyLand"
	}
]
```

![Insomnia test: GET /islands](/docs/Screenshots/4.%20GET%20:islands.png)

**Get one island**
- HTTP verb: GET
- Route: http://localhost:8081/islands/3
- Any required body (json) or header data (auth/jwt):
    - Auth Bearer Token/JWT required - No

JSON body:
```
-
```
Response:
```
{
	"user": {
		"name": "Sami",
		"id": 4
	},
	"id": 3,
	"island_name": "KittyLand"
}
```

![Insomnia test: GET /islands/3](/docs/Screenshots/5.%20GET%20:islands:3.png)

- HTTP verb: GET
- Route: http://localhost:8081/islands/4
- Any required body (json) or header data (auth/jwt):
    - Auth Bearer Token/JWT required - No
Fail: Island ID not found

Response:
```
{
	"error": "Island with id 4 not found"
}
```

![Insomnia test: GET /islands/4](/docs/Screenshots/5.%20GET%20islands:4%20fail.png)

**Updating an Island**
- HTTP verb: PATCH
- Route: http://localhost:8081/islands/3
- Any required body (json) or header data (auth/jwt):
    - Auth Bearer Token/JWT Required - User Sami

JSON body:
```
{
		"island_name": "Chonky Island"
	}
```
Correct user & correct island ID No.
Response:

```
{
	"user": {
		"name": "Sami",
		"id": 4
	},
	"id": 3,
	"island_name": "Chonky Island"
}
```


![Insomnia test: PATCH /islands/3](/docs/Screenshots/6.%20PATCH%20:islands.png)

Fail: Wrong user/jwt

```
{
	"error": "You are not the owner of this island."
}
```

![Insomnia test: PATCH /islands/3](/docs/Screenshots/6.%20PATCH%20islands%20fail.png)

**Deleting an Island**
- HTTP verb: DELETE 
- Route: http://localhost:8081/islands/3
- Any required body (json) or header data (auth/jwt):
    - Auth Bearer Token/JWT Required - User Sami

JSON body:
```
-
```
Correct JWT
Response:
```
{
	"message": "Island 'Chonky Island' deleted successfully"
}
```

![Insomnia test: DELETE /islands/3](/docs/Screenshots/7.%20DELETE%20:islands.png)

- HTTP verb: DELETE 
- Route: http://localhost:8081/islands/3
- Any required body (json) or header data (auth/jwt):
    - Auth Bearer Token/JWT Required - User Kate

Fail: Incorrect JWT
Response:
```
{
	"error": "You are not the owner of this island."
}
```
![Insomnia test: DELETE /islands/3](/docs/Screenshots/7.%20DELETE%20island%20fail.png)


**GET all villagers**
- HTTP verb: GET 
- Route: http://localhost:8081/villagers
- Any required body (json) or header data (auth/jwt):
    - Auth Bearer Token/JWT required - No

JSON body:
```
-
```
Response:
```
[
	{
		"id": 443,
		"name": "Ace",
		"gender": "Male",
		"species": "Bird",
		"personality": "Jock",
		"birthday": "11-Aug",
		"catchphrase": "ace",
		"hobbies": "Nature"
	},
	{
		"id": 500,
		"name": "Admiral",
		"gender": "Male",
		"species": "Bird",
		"personality": "Cranky",
		"birthday": "27-Jan",
		"catchphrase": "aye aye",
		"hobbies": "Nature"
	},
	{
		"id": 198,
		"name": "Agent S",
		"gender": "Female",
		"species": "Squirrel",
		"personality": "Peppy",
		"birthday": "2-Jul",
		"catchphrase": "sidekick",
		"hobbies": "Fitness"
	},
	...,
    ...,
]
```

- Everyone can access villager data; admin AND user
 - Villager data is preset, not to be changed
 - Villagers' IDs start at 18-448 & 500-557
 - Villagers' IDs 18-448 match their online Amiibo number
 - Villagers' IDs 500+ don't have Amiibo's numbers.

![Insomnia test: GET /villagers](/docs/Screenshots/9.%20GET%20:villagers.png)

**Get one villager**

- HTTP verb: GET 
- Route: http://localhost:8081/villagers/430
- Any required body (json) or header data (auth/jwt):
    - Auth Bearer Token/JWT required - No

- Using Villager ID No.
JSON body:
```
-
```
Response:
```
{
	"id": 430,
	"name": "Judy",
	"gender": "Female",
	"species": "Cub",
	"personality": "Snooty",
	"birthday": "10-Mar",
	"catchphrase": "myohmy",
	"hobbies": "Music"
}
```
- Everyone can access villager data; admin AND user
 - Villager ID No. can be used to find villager data
 - Villager's ID No. matches their online Amiibo number ('cept for 500+)

![Insomnia test: GET /villagers/430](/docs/Screenshots/10.%20GET%20:villagers:430.png)
 
 - Villager name can be queried to fetch that villager's data
    - Route: http://localhost:8081/villagers?name=Judy

![Insomnia test: GET /villagers?name=Judy](/docs/Screenshots/11.%20GET%20:villagers%20judy.png)

Fail - Villager ID doesn't exist
![Insomnia test: GET /villagers/1](/docs/Screenshots/10.%20GET%20villagers%20fail.png)


**Creating new villager**
- HTTP verb: POST
- Route: http://localhost:8081/villagers
- Any required body (json) or header data (auth/jwt):
    - Auth Bearer Token/JWT required - User Sami

JSON body:
```
{
    "name": "Cherry",
    "gender": "Female",
    "species": "Dog",
    "personality": "Big Sister",
    "birthday": "May 11",
    "catchphrase": "what what",
    "hobbies": "Music"
}
```
Response:
```
{
	"Error": "User is not authorised to perform this action."
}
```

 - Only admin is authorised to add villager data
 - Villager data is preset, not to be changed

![Insomnia test: POST /villagers](/docs/Screenshots/8.%20POST%20:villagers.png)


**Creating a new villager**
Logged in as Admin
- HTTP verb: POST 
- Route: http://localhost:8081/villagers
- Any required body (json) or header data (auth/jwt):
    - Auth Bearer Token/JWT required - Admin

JSON body:
```
{
    "name": "Fakie",
  "gender": "Male",
  "species": "Dog",
  "personality": "Cranky",
  "birthday": "Sept 11",
  "catchphrase": "dang",
  "hobbies": "Fitness"
}
```
Response:
```
{
	"id": 1,
	"name": "Fakie",
	"gender": "Male",
	"species": "Dog",
	"personality": "Cranky",
	"birthday": "Sept 11",
	"catchphrase": "dang",
	"hobbies": "Fitness"
}
```
- Only admin can Create a villager

![Insomnia test: POST /villagers](/docs/Screenshots/POST%20villagers%20admin.png)


**Updating Villager**
- HTTP verb: PATCH 
- Route: http://localhost:8081/villagers/1
- Any required body (json) or header data (auth/jwt):
    - Auth Bearer Token/JWT required - User Sami

JSON body:
```
{
	"id": 77
}
```
Response:
```
{
	"Error": "User is not authorised to perform this action."
}
```


 - Only admin is authorised to update villager data
 - Villager data is preset, not to be changed

![Insomnia test: PATCH /villagers](/docs/Screenshots/13.%20PATCH%20:villagers.png)


**Updating a villager**
Logged in as admin
- HTTP verb: PATCH 
- Route: http://localhost:8081/villagers/1
- Any required body (json) or header data (auth/jwt):
    - Auth Bearer Token/JWT required - Admin

JSON body:
```
{
	"name": "FakieMcFakerson"
}
```
Response:
```
{
	"id": 1,
	"name": "FakieMcFakerson",
	"gender": "Male",
	"species": "Dog",
	"personality": "Cranky",
	"birthday": "Sept 11",
	"catchphrase": "dang",
	"hobbies": "Fitness"
}
```
![Insomnia test: PATCH /villagers/1](/docs/Screenshots/PATCH%20villagers%20admin.png)

**Deleting a villager**
- HTTP verb: DELETE 
- Route: http://localhost:8081/villagers/5
- Any required body (json) or header data (auth/jwt):
    - Auth Bearer Token/JWT required - User

JSON body:
```
-
```
Fail: User tries to delete villager
Response:
```
{
	"Error": "User is not authorised to perform this action."
}
```
 - Only admin is authorised to delete a villager
 - Villager data is preset, not to be changed


![Insomnia test: DELETE /villagers/5](/docs/Screenshots/12.%20DELETE%20:villagers.png)

- HTTP verb: DELETE 
- Route: http://localhost:8081/villagers/1
- Any required body (json) or header data (auth/jwt):
    - Auth Bearer Token/JWT required - Admin

JSON body:
```
-
```
Response:
```
{
	"message": "Villager 'FakieMcFakerson, ID No. 1' deleted successfully"
}
```

![Insomnia test: DELETE /villagers/1](/docs/Screenshots/DELETE%20villagers%20admin.png)



**GET Island Villagers**
Logged in as User Kate
- HTTP verb: GET 
- Route: http://localhost:8081/island_villagers
- Any required body (json) or header data (auth/jwt):
    - Auth Bearer Token/JWT required - User Kate

JSON body:
```
-
```
Response:
```
[
	{
		"id": 1,
		"island": {
			"id": 1,
			"island_name": "Zorlandia"
		},
		"villager": {
			"name": "Judy",
			"gender": "Female",
			"species": "Cub",
			"personality": "Snooty",
			"birthday": "10-Mar",
			"catchphrase": "myohmy",
			"hobbies": "Music"
		},
		"text": null,
		"villager_id": 430
	},
	{
		"id": 2,
		"island": {
			"id": 1,
			"island_name": "Zorlandia"
		},
		"villager": {
			"name": "Merengue",
			"gender": "Female",
			"species": "Rhino",
			"personality": "Normal",
			"birthday": "19-Mar",
			"catchphrase": "shortcake",
			"hobbies": "Nature"
		},
		"text": null,
		"villager_id": 285
	},
	{
		"id": 3,
		"island": {
			"id": 1,
			"island_name": "Zorlandia"
		},
		"villager": {
			"name": "Cherry",
			"gender": "Female",
			"species": "Dog",
			"personality": "Big Sister",
			"birthday": "11-May",
			"catchphrase": "what what",
			"hobbies": "Music"
		},
		"text": null,
		"villager_id": 77
	},
	{
		"id": 4,
		"island": {
			"id": 1,
			"island_name": "Zorlandia"
		},
		"villager": {
			"name": "Bunnie",
			"gender": "Female",
			"species": "Rabbit",
			"personality": "Peppy",
			"birthday": "9-May",
			"catchphrase": "tee-hee",
			"hobbies": "Fashion"
		},
		"text": null,
		"villager_id": 87
	},
	{
		"id": 5,
		"island": {
			"id": 1,
			"island_name": "Zorlandia"
		},
		"villager": {
			"name": "Filbert",
			"gender": "Male",
			"species": "Squirrel",
			"personality": "Lazy",
			"birthday": "3-Jun",
			"catchphrase": "bucko",
			"hobbies": "Nature"
		},
		"text": null,
		"villager_id": 165
	},
	{
		"id": 6,
		"island": {
			"id": 1,
			"island_name": "Zorlandia"
		},
		"villager": {
			"name": "Boone",
			"gender": "Male",
			"species": "Gorilla",
			"personality": "Jock",
			"birthday": "12-Sep",
			"catchphrase": "baboom",
			"hobbies": "Fitness"
		},
		"text": null,
		"villager_id": 328
	},
	{
		"id": 7,
		"island": {
			"id": 1,
			"island_name": "Zorlandia"
		},
		"villager": {
			"name": "Phil",
			"gender": "Male",
			"species": "Ostrich",
			"personality": "Smug",
			"birthday": "27-Nov",
			"catchphrase": "hurk",
			"hobbies": "Music"
		},
		"text": null,
		"villager_id": 57
	}
]
```

Logged in as User Kate
 - A logged in user can only view their own island villagers
![Insomnia test: GET island_villagers](/docs/Screenshots/14.%20GET%20island_villagers.png)

Logged in as Admin
- HTTP verb: GET 
- Route: http://localhost:8081/island_villagers
- Any required body (json) or header data (auth/jwt):
    - Auth Bearer Token/JWT required - Admin

JSON body:
```
-
```
Response:
```
[
	{
		"id": 1,
		"island": {
			"id": 1,
			"island_name": "Zorlandia"
		},
		"villager": {
			"name": "Judy",
			"gender": "Female",
			"species": "Cub",
			"personality": "Snooty",
			"birthday": "10-Mar",
			"catchphrase": "myohmy",
			"hobbies": "Music"
		},
		"text": null,
		"villager_id": 430
	},
	{
		"id": 2,
		"island": {
			"id": 1,
			"island_name": "Zorlandia"
		},
		"villager": {
			"name": "Merengue",
			"gender": "Female",
			"species": "Rhino",
			"personality": "Normal",
			"birthday": "19-Mar",
			"catchphrase": "shortcake",
			"hobbies": "Nature"
		},
		"text": null,
		"villager_id": 285
	},
	{
		"id": 3,
		"island": {
			"id": 1,
			"island_name": "Zorlandia"
		},
		"villager": {
			"name": "Cherry",
			"gender": "Female",
			"species": "Dog",
			"personality": "Big Sister",
			"birthday": "11-May",
			"catchphrase": "what what",
			"hobbies": "Music"
		},
		"text": null,
		"villager_id": 77
	},
	{
		"id": 4,
		"island": {
			"id": 1,
			"island_name": "Zorlandia"
		},
		"villager": {
			"name": "Bunnie",
			"gender": "Female",
			"species": "Rabbit",
			"personality": "Peppy",
			"birthday": "9-May",
			"catchphrase": "tee-hee",
			"hobbies": "Fashion"
		},
		"text": null,
		"villager_id": 87
	},
	{
		"id": 5,
		"island": {
			"id": 1,
			"island_name": "Zorlandia"
		},
		"villager": {
			"name": "Filbert",
			"gender": "Male",
			"species": "Squirrel",
			"personality": "Lazy",
			"birthday": "3-Jun",
			"catchphrase": "bucko",
			"hobbies": "Nature"
		},
		"text": null,
		"villager_id": 165
	},
	{
		"id": 6,
		"island": {
			"id": 1,
			"island_name": "Zorlandia"
		},
		"villager": {
			"name": "Boone",
			"gender": "Male",
			"species": "Gorilla",
			"personality": "Jock",
			"birthday": "12-Sep",
			"catchphrase": "baboom",
			"hobbies": "Fitness"
		},
		"text": null,
		"villager_id": 328
	},
	{
		"id": 7,
		"island": {
			"id": 1,
			"island_name": "Zorlandia"
		},
		"villager": {
			"name": "Phil",
			"gender": "Male",
			"species": "Ostrich",
			"personality": "Smug",
			"birthday": "27-Nov",
			"catchphrase": "hurk",
			"hobbies": "Music"
		},
		"text": null,
		"villager_id": 57
	},
	{
		"id": 8,
		"island": {
			"id": 2,
			"island_name": "PuppyLand"
		},
		"villager": {
			"name": "Sasha",
			"gender": "Male",
			"species": "Rabbit",
			"personality": "Lazy",
			"birthday": "19-May",
			"catchphrase": "hoppity",
			"hobbies": "Fashion"
		},
		"text": null,
		"villager_id": 433
	},
	{
		"id": 9,
		"island": {
			"id": 2,
			"island_name": "PuppyLand"
		},
		"villager": {
			"name": "Ione",
			"gender": "Female",
			"species": "Squirrel",
			"personality": "Normal",
			"birthday": "11-Sep",
			"catchphrase": "gleam",
			"hobbies": "Fashion"
		},
		"text": null,
		"villager_id": 434
	}
]
```

Logged in as Admin
 - Admin can view all island's island villagers
![Insomnia test: GET island villagers as Admin](/docs/Screenshots/15.%20GET%20island%20villagers%20admin.png)

Logged in as User Isaboo
- HTTP verb: GET 
- Route: http://localhost:8081/island_villagers
- Any required body (json) or header data (auth/jwt):
    - Auth Bearer Token/JWT required - User Isaboo

JSON body:
```
-
```
Response:
```
[
	{
		"id": 8,
		"island": {
			"id": 2,
			"island_name": "PuppyLand"
		},
		"villager": {
			"name": "Sasha",
			"gender": "Male",
			"species": "Rabbit",
			"personality": "Lazy",
			"birthday": "19-May",
			"catchphrase": "hoppity",
			"hobbies": "Fashion"
		},
		"text": null,
		"villager_id": 433
	},
	{
		"id": 9,
		"island": {
			"id": 2,
			"island_name": "PuppyLand"
		},
		"villager": {
			"name": "Ione",
			"gender": "Female",
			"species": "Squirrel",
			"personality": "Normal",
			"birthday": "11-Sep",
			"catchphrase": "gleam",
			"hobbies": "Fashion"
		},
		"text": null,
		"villager_id": 434
	}
]
```

Logged in as User Isaboo
 - A logged in user can only view their own island villagers
![Insomnia test: GET island villagers ](/docs/Screenshots/16.%20GET%20island%20villagers%20isaboo.png)

**Updating Island Villager**

Logged in as User Kate
- HTTP verb: PATCH 
- Route: http://localhost:8081/island_villagers/4
- Any required body (json) or header data (auth/jwt):
    - Auth Bearer Token/JWT required - User Kate

JSON body:
```
{
    "villager_name": "Bunnie",
	"text": "Bunnie is funny"
}
```
Response:
```
{
	"id": 4,
	"island": {
		"id": 1,
		"island_name": "Zorlandia"
	},
	"villager": {
		"name": "Bunnie",
		"gender": "Female",
		"species": "Rabbit",
		"personality": "Peppy",
		"birthday": "9-May",
		"catchphrase": "tee-hee",
		"hobbies": "Fashion"
	},
	"text": "Bunnie is funny",
	"villager_id": 87
}
```

- User can update their own island villager's text field to add comments about said island villager
- Updating island villager ID not allowed

Correct user/jwt updating

JSON body:
```
{
    "villager_name": "Bunnie",
    "text": "Bunnie is funny"
}
```
Response:
```
{
	"id": 4,
	"island": {
		"id": 1,
		"island_name": "Zorlandia"
	},
	"villager": {
		"name": "Bunnie",
		"gender": "Female",
		"species": "Rabbit",
		"personality": "Peppy",
		"birthday": "9-May",
		"catchphrase": "tee-hee",
		"hobbies": "Fashion"
	},
	"text": "Bunnie is funny",
	"villager_id": 87
}
```

![Insomnia test: PATCH /island_villagers](/docs/Screenshots/17.%20PATCH%20:island%20villagers.png)

Fail: Trying to update island villager ID instead of text
JSON body:
```
{
    "villager_name": "Bunnie",
    "island_villager_id": 10
}
```
Response:
```
{
	"error": "Updating the island villager ID is not allowed"
}
```

![Insomnia test: PATCH /island_villagers](/docs/Screenshots/18.%20PATCH%20island%20villagers.png)

Fail: Incorrect jwt/wrong user trying to update

JSON body:
```
{
"villager_name": "Bunnie",
	"text": "Bunnie is funny"
}
```
Response:
```
{
	"error": "You are not the owner of this island's villager list"
}
```

![Insomnia test: PATCH /island_villagers](/docs/Screenshots/18.%20PATCH%20island%20villagers%20wrong%20user.png)



**Deleting Island Villager**

Logged in as User Kate
- HTTP verb: DELETE
- Route: http://localhost:8081/island_villagers/7
- Any required body (json) or header data (auth/jwt):
    - Auth Bearer Token/JWT required - User Kate

JSON body:
```
-
```
Correct user/jwt deleting - User Kate
Response:
```
{
	"message": "Villager 'Phil' (ID: 57) deleted successfully from your Island List"
}
```

- Only a logged in User can delete their own island villager from their island villager list

![Insomnia test: DELETE /island_villagers/7](/docs/Screenshots/19.%20DELETE%20island%20villagers.png)

Fail: Incorrect jwt/wrong user trying to delete - User Isaboo
Response:
```
{
	"error": "You are not the owner of this island's villager list"
}
```
![Insomnia test: DELETE /island_villagers/7](/docs/Screenshots/20.%20DELETE%20island%20villagers%20wrong%20jwt.png)

Fail: Island Villager doesn't exist in list
Response:
```
{
	"error": "Island villager with id 7 not found"
}
```

![Insomnia test: DELETE /island_villagers/7](/docs/Screenshots/21.%20DELETE%20island%20villager%20doesn't%20exist.png)

**GET All Wanted Villagers**

Logged in as User Kate
- HTTP verb: GET
- Route: http://localhost:8081/wanted_villagers
- Any required body (json) or header data (auth/jwt):
    - Auth Bearer Token/JWT required - User Kate

JSON body:
```
-
```
Correct user/jwt - Logged in as User Kate
Response:
```
[
	{
		"island": {
			"id": 1,
			"island_name": "Zorlandia"
		},
		"villager": {
			"id": 381,
			"name": "Gloria",
			"gender": "Female",
			"species": "Duck",
			"personality": "Snooty",
			"birthday": "12-Aug",
			"catchphrase": "quacker",
			"hobbies": "Fashion"
		},
		"id": 1,
		"notes": []
	},
	{
		"island": {
			"id": 1,
			"island_name": "Zorlandia"
		},
		"villager": {
			"id": 125,
			"name": "Gwen",
			"gender": "Female",
			"species": "Penguin",
			"personality": "Snooty",
			"birthday": "23-Jan",
			"catchphrase": "h-h-h-hon",
			"hobbies": "Fashion"
		},
		"id": 2,
		"notes": []
	}
]
```

- A logged in User can view their own wanted villagers list
![Insomnia test: GET /wanted_villagers](/docs/Screenshots/22.%20GET%20wanted%20villagers.png)

Logged in as admin
Response:
```
[
	{
		"island": {
			"id": 1,
			"island_name": "Zorlandia"
		},
		"villager": {
			"id": 381,
			"name": "Gloria",
			"gender": "Female",
			"species": "Duck",
			"personality": "Snooty",
			"birthday": "12-Aug",
			"catchphrase": "quacker",
			"hobbies": "Fashion"
		},
		"id": 1,
		"notes": [
			{
				"notes": "She has purple hair & pretty makeup.",
				"id": 1
			}
		]
	},
	{
		"island": {
			"id": 1,
			"island_name": "Zorlandia"
		},
		"villager": {
			"id": 125,
			"name": "Gwen",
			"gender": "Female",
			"species": "Penguin",
			"personality": "Snooty",
			"birthday": "23-Jan",
			"catchphrase": "h-h-h-hon",
			"hobbies": "Fashion"
		},
		"id": 2,
		"notes": [
			{
				"notes": "She has purple hair & pretty makeup too.",
				"id": 2
			}
		]
	},
	{
		"island": {
			"id": 2,
			"island_name": "PuppyLand"
		},
		"villager": {
			"id": 188,
			"name": "Ankha",
			"gender": "Female",
			"species": "Cat",
			"personality": "Snooty",
			"birthday": "22-Sep",
			"catchphrase": "me meow",
			"hobbies": "Nature"
		},
		"id": 3,
		"notes": [
			{
				"notes": "Kitty!",
				"id": 3
			}
		]
	},
	{
		"island": {
			"id": 2,
			"island_name": "PuppyLand"
		},
		"villager": {
			"id": 137,
			"name": "Cookie",
			"gender": "Female",
			"species": "Dog",
			"personality": "Peppy",
			"birthday": "18-Jun",
			"catchphrase": "arfer",
			"hobbies": "Fashion"
		},
		"id": 4,
		"notes": [
			{
				"notes": "She's a pink cutie",
				"id": 4
			}
		]
	}
]
```

- Admin can view all wanted villagers of all islands
![Insomnia test: GET /wanted_villagers](/docs/Screenshots/23.%20GET%20wanted%20villagers%20admin.png)

Logged in as Isaboo
Response:
```
[
	{
		"island": {
			"id": 2,
			"island_name": "PuppyLand"
		},
		"villager": {
			"id": 188,
			"name": "Ankha",
			"gender": "Female",
			"species": "Cat",
			"personality": "Snooty",
			"birthday": "22-Sep",
			"catchphrase": "me meow",
			"hobbies": "Nature"
		},
		"id": 3,
		"notes": [
			{
				"notes": "Kitty!",
				"id": 3
			}
		]
	},
	{
		"island": {
			"id": 2,
			"island_name": "PuppyLand"
		},
		"villager": {
			"id": 137,
			"name": "Cookie",
			"gender": "Female",
			"species": "Dog",
			"personality": "Peppy",
			"birthday": "18-Jun",
			"catchphrase": "arfer",
			"hobbies": "Fashion"
		},
		"id": 4,
		"notes": [
			{
				"notes": "She's a pink cutie",
				"id": 4
			}
		]
	}
]
```
- A logged in User can view their own wanted villagers list
![Insomnia test: GET /wanted_villagers](/docs/Screenshots/24.%20GET%20wanted%20villagers%20isaboo.png)

**Get One Wanted Villager**

Logged in as User Kate
- HTTP verb: GET
- Route: http://localhost:8081/wanted_villagers/1
- Any required body (json) or header data (auth/jwt):
    - Auth Bearer Token/JWT required - User Kate

JSON body:
```
-
```
Response:
```
{
	"island": {
		"id": 1,
		"island_name": "Zorlandia"
	},
	"villager": {
		"id": 381,
		"name": "Gloria",
		"gender": "Female",
		"species": "Duck",
		"personality": "Snooty",
		"birthday": "12-Aug",
		"catchphrase": "quacker",
		"hobbies": "Fashion"
	},
	"id": 1,
	"notes": []
}
```
- A logged in User can view their own wanted villagers


![Insomnia test: GET /wanted_villagers/1](/docs/Screenshots/25.%20GET%20one%20wanted%20villager.png)

Fail: Wrong user/jwt accessing another user's wanted villager
- HTTP verb: GET
- Route: http://localhost:8081/wanted_villagers/1
- Any required body (json) or header data (auth/jwt):
    - Auth Bearer Token/JWT required - User Isaboo
Response:
```
{
	"error": "You do not have permission to view this wanted villager."
}
```
![Insomnia test: GET /wanted_villagers/1](/docs/Screenshots/25.%20GET%20one%20wanted%20villager%20wrong%20jwt.png)

**Add New Wanted Villager**

Logged in as User Kate
- HTTP verb: POST
- Route: http://localhost:8081/wanted_villagers
- Any required body (json) or header data (auth/jwt):
    - Auth Bearer Token/JWT required - User Kate

JSON body:
```
{
	"island_id": 1,
	"villager_name": "Mathilda"
}
```
Response:
```
{
	"island": {
		"id": 1,
		"island_name": "Zorlandia"
	},
	"villager": {
		"id": 162,
		"name": "Mathilda",
		"gender": "Female",
		"species": "Kangaroo",
		"personality": "Snooty",
		"birthday": "12-Nov",
		"catchphrase": "wee baby",
		"hobbies": "Fitness"
	},
	"id": 5,
	"notes": []
}
```

![Insomnia test: POST /wanted_villagers](/docs/Screenshots/26.%20POST%20wanted%20villagers.png)

Fail: Tries to add Wanted Villager to Island ID that does not exist
JSON body:
```
{
	"island_id": 3,
	"villager_name": "Mathilda"
}
```
Response:
```
{
	"error": "Island with id 3 not found"
}
```
![Insomnia test: POST /wanted_villagers](/docs/Screenshots/26.%20POST%20wanted%20villagers%20fail.png)

**Update Wanted Villager**

Logged in as User Kate
- HTTP verb: PATCH
- Route: http://localhost:8081/wanted_villagers/1
- Any required body (json) or header data (auth/jwt):
    - Auth Bearer Token/JWT required - User Kate

JSON body:
```
-
```
Response:
```
{
	"error": "Updating wanted villager entries is not allowed, as this section is ID's only. You may update notes for your wanted villagers instead."
}
```
- Updating wanted villager section not allowed as it's just ID's for database storing purposes

![Insomnia test: PATCH /wanted_villagers](/docs/Screenshots/27.%20PATCH%20wanted%20villagers.png)

**Delete Wanted Villager**

Logged in as User Kate
- HTTP verb: DELETE
- Route: http://localhost:8081/wanted_villagers/8
- Any required body (json) or header data (auth/jwt):
    - Auth Bearer Token/JWT required - User Kate

Correct jwt/correct wanted_villager_id
JSON body:
```
{
	"wanted_villagers_id": 8
}
```
Response:
```
{
	"message": "'Mathilda' deleted successfully from your Wanted List"
}
```
- A logged in user may delete their own wanted villagers

![Insomnia test: DELETE /wanted_villagers/8](/docs/Screenshots/28.%20DELETE%20wanted%20villagers.png)

Fail: Wanted Villager id doesn't exist
Response:
```
{
	"error": "Wanted villager entry not found"
}
```
![Insomnia test: DELETE /wanted_villagers/8](/docs/Screenshots/29.%20DELETE%20wanted%20villager%20id%20doesn't%20exist.png)

Fail: Wanted Villager ID not belonging to you
Response:
```
{
	"error": "You are not the owner of this island's wanted villager list."
}
```
![Insomnia test: DELETE /wanted_villagers/4](/docs/Screenshots/30.%20DELETE%20wanted%20villager%20not%20yours.png)

**Create note about Wanted Villager**

Logged in as User Kate
- HTTP verb: POST
- Route: http://localhost:8081/wanted_villagers/1/notes
- Any required body (json) or header data (auth/jwt):
    - Auth Bearer Token/JWT required - User Kate

Correct jwt
JSON body:
```
{
	"villager_name": "Gloria",
	"notes": "She has purple hair and pretty makeup!!"

}
```
Response:
```
{
	"wanted_villager": {
		"island": {
			"id": 1,
			"island_name": "Zorlandia"
		},
		"villager": {
			"id": 381,
			"name": "Gloria",
			"gender": "Female",
			"species": "Duck",
			"personality": "Snooty",
			"birthday": "12-Aug",
			"catchphrase": "quacker",
			"hobbies": "Fashion"
		},
		"id": 1
	},
	"notes": "She has purple hair and pretty makeup",
	"id": 3
}
```
- A logged in user can add notes to their own wanted villagers

![Insomnia test: POST /wanted_villagers/1/notes](/docs/Screenshots/31.%20POST%20notes.png)

Incorrect JSON body data
JSON body:
```
{

	"notes": "She has purple hair and pretty makeup!!"

}
```
Response:
```
{
    "error": "Either wanted_villagers_id or villager_name must be provided"
}
```
![Insomnia test: POST /wanted_villagers/1/notes](/docs/Screenshots/32.%20POST%20notes%20incorrect%20body%20data.png)

Incorrect jwt/wrong user
JSON body:
```
{
	"villager_name": "Gloria",
	"notes": "She has purple hair & she's pretty"
}
```
Response:
```
{
    "error": "You are not the owner of this island's wanted villager list"
}
```

![Insomnia test: POST /wanted_villagers/1/notes](/docs/Screenshots/33.%20POST%20notes%20wrong%20user.png)

**Update note about Wanted Villager**

Logged in as User Kate
- HTTP verb: PATCH
- Route: http://localhost:8081/wanted_villagers/1/notes/1
- Any required body (json) or header data (auth/jwt):
    - Auth Bearer Token/JWT required - User Kate


JSON body:
```
{
	"villager_name": "Gloria",
	"notes": "She has purple hair & she's pretty"
}
```
Correct JWT

Response:
```
{
	"wanted_villager": {
		"island": {
			"id": 1,
			"island_name": "Zorlandia"
		},
		"villager": {
			"id": 381,
			"name": "Gloria",
			"gender": "Female",
			"species": "Duck",
			"personality": "Snooty",
			"birthday": "12-Aug",
			"catchphrase": "quacker",
			"hobbies": "Fashion"
		},
		"id": 1
	},
	"notes": "She has purple hair & she's pretty",
	"id": 1
}
```
- A logged in user can update their own notes on their own wanted villagers


![Insomnia test: PATCH /wanted_villagers/1/notes/1](/docs/Screenshots/34.%20PATCH%20notes.png)

Incorrect jwt/wrong user

Response:
```
{
    "error": "You are not the owner of this island's wanted villager list"
}
```
![Insomnia test: PATCH /wanted_villagers/1/notes](/docs/Screenshots/35.%20PATCH%20notes%20incorrect%20jwt.png)

Incorrect JSON body data/wrong villager name for the wanted villager id

JSON body:
```
{
	"villager_name": "Gwen",
	"notes": "She has purple hair & she's pretty"
}
```
Response:
```
{
    "Note with id 1 not found for the specified wanted villager"
}
```
![Insomnia test: POST /wanted_villagers/1/notes/1](/docs/Screenshots/36.%20PATCH%20notes%20wrong%20villager%20name.png)

**Delete note about Wanted Villager**

Logged in as User Kate
- HTTP verb: DELETE
- Route: http://localhost:8081/wanted_villagers/1/notes/1
- Any required body (json) or header data (auth/jwt):
    - Auth Bearer Token/JWT required - User Kate

Correct jwt
JSON body:
```
-
```
Response:
```
{
	"message": "Note 'She has purple hair & she's pretty' deleted successfully"
}
```
- A logged in user can delete their own notes on their own wanted villagers

![Insomnia test: DELETE /wanted_villagers/1/notes/1](/docs/Screenshots/37.%20DELETE%20note.png)

Incorrect jwt/wrong user

Response:
```
{
    "error": "You are not the author or this note" 
}
```
![Insomnia test: DELETE /wanted_villagers/1/notes](/docs/Screenshots/38.%20DELETE%20note%20incorrect%20jwt.png)

