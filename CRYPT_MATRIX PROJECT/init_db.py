# init_db.py

from app import db
db.create_all()
print("Database initialized.")

