import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app, db

def clear_db():
    with app.app_context():
        db.drop_all()
        db.create_all()

clear_db()