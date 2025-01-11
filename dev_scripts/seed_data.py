import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app, db
from models import Expense
from datetime import datetime

def seed_data():
    expense1 = Expense(uid=1, amount=50.0, title='Groceries', description='Weekly groceries', category='Groceries', date=datetime(2025, 1, 5))
    expense2 = Expense(uid=1, amount=20.0, title='Transport', description='Bus fare', category='Transport', date=datetime(2025, 1, 6))
    
    expense3 = Expense(uid=2, amount=100.0, title='Rent', description='Monthly rent', category='Housing', date=datetime(2025, 1, 1))
    expense4 = Expense(uid=2, amount=30.0, title='Dining Out', description='Dinner with friends', category='Dine-outs', date=datetime(2025, 1, 3))

    db.session.add(expense1)
    db.session.add(expense2)
    db.session.add(expense3)
    db.session.add(expense4)

    db.session.commit()

    print("Expenses seeded successfully!")

with app.app_context():
    seed_data()
