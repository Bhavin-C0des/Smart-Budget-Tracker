from app import app, db
from models import User, Expense

def init_db():
    with app.app_context():
        db.create_all()

init_db()