from app import app, db
from models import Task

with app.app_context():
    db.create_all()
    print("Database and tables created successfully.")
