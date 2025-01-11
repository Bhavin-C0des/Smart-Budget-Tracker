from flask import Blueprint, render_template, request, session, redirect, url_for
from models import db, User, Expense
from datetime import datetime
from sqlalchemy import desc
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from features.graphs import create_pie_chart


dashboard_bp = Blueprint('dashboard', __name__)

expenses_by_category = {}

def get_expenses_by_category(expenses):
    for expense in expenses:
        if expense.category in expenses_by_category:
            expenses_by_category[expense.category] += expense.amount
        else:
            expenses_by_category[expense.category] = expense.amount
    return expenses_by_category

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


@dashboard_bp.route('/expenses')
def expenses():
    if 'user_id' in session:
        expenses = Expense.query.filter_by(uid=session['user_id']).order_by(desc(Expense.date)).all()
        expenses_by_category = get_expenses_by_category(expenses)
        pie_chart_html = create_pie_chart(expenses_by_category)
        return render_template('expenses.html', expenses=expenses, expenses_by_category=expenses_by_category, pie_chart_html=pie_chart_html)
    return redirect(url_for('auth.login'))


