from flask import Blueprint, render_template, request, session, redirect, url_for
from models import db, User, Expense
from datetime import datetime
from sqlalchemy import desc
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from features.graphs import create_pie_chart
from features.ocr import upload_bill
from features.bill_analysis import analyse_bill


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
    extracted_text = None
    if 'user_id' in session:
        if request.method == 'POST':
            action = request.form.get('action')

            if action == 'add_expense':
                title = request.form['title']
                amount = request.form['amount']
                description = request.form['description']
                uid = session['user_id']
                category = request.form['category']
                expense = Expense(title=title, amount=amount, description=description, uid=uid, category=category)
                db.session.add(expense)
                db.session.commit()
                           
            elif action == 'upload_bill':
                if 'bill_image' in request.files:
                    file = request.files['bill_image']
                    extracted_text = upload_bill(file)
                    result = analyse_bill(extracted_text)
                    title = result['title']
                    amount = result['amount']
                    amount = amount.replace(',', '')
                    description = result['description']
                    category = result['category']
                    uid = session['user_id']
                    expense=Expense(title=title, amount=amount, description=description, uid=uid, category=category)
                    db.session.add(expense)
                    db.session.commit()


        return render_template('add_expense.html')
    return redirect(url_for('auth.login'))


@dashboard_bp.route('/expenses')
def expenses():
    if 'user_id' in session:
        uid = session['user_id']
        expenses_by_category = {}
        expenses = Expense.query.filter_by(uid=uid).order_by(desc(Expense.date)).all()
        print(expenses)
        expenses_by_category = get_expenses_by_category(expenses)
        print(expenses_by_category)
        pie_chart_html = create_pie_chart(expenses_by_category)
        return render_template('expenses.html', expenses=expenses, expenses_by_category=expenses_by_category, pie_chart_html=pie_chart_html)
    return redirect(url_for('auth.login'))


