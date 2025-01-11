from flask import Blueprint, render_template, request, session, redirect, url_for
from models import db, User, Expense
from datetime import datetime

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/dashboard')
def dashboard():
    if 'user_id' in session:
        return render_template('dashboard.html')
    return redirect(url_for('auth.login'))

@dashboard_bp.route('/add-expense', methods=['GET', 'POST'])
def add_expense():
    if 'user_id' in session:
        if request.method == 'POST':
            title = request.form['title']
            amount = request.form['amount']
            description = request.form['description']
            uid = session['user_id']
            print(uid)
            category = request.form['category']
            expense = Expense(title=title, amount=amount, description=description, uid=uid, category=category)
            db.session.add(expense)
            db.session.commit()
            return redirect(url_for('dashboard.dashboard'))
        return render_template('add_expense.html')
    return redirect(url_for('auth.login'))



