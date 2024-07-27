### To install: Run the following commands in your terminal:

Create virtual environment:
```
python3 -m venv .venv
```
Activate virtual environment:
```
source .venv/bin/activate
```
Clone this Git repository

Open a psql terminal & create a database in Postgres:
```
CREATE DATABASE acnh_db;
```
Create psql database user & grant database priveleges to user:
```
CREATE USER acnh_admin WITH PASSWORD '123456';
GRANT ALL PRIVILEGES ON DATABASE acnh_db TO acnh_admin;
GRANT ALL ON SCHEMA public TO acnh_admin;
```
Create a .env file and include the variables needed from .env.sample, e.g.
```
DATABASE_URL=
JWT_SECRET_KEY=
```
In terminal, Install requirements:
```
pip3 install -r requirements.txt
```
Create & seed tables:
```
flask db create
flask db seed
```
Run flask app:
```
python3 -m flask run
```
If in need of dropping data:
```
flask db drop
```