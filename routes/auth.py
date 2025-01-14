from flask import Blueprint, render_template, request, session, redirect, url_for
from flask_bcrypt import Bcrypt
from models import db, User

auth_bp = Blueprint('auth', __name__)
bcrypt = Bcrypt()

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        monthly_income = request.form['monthly_income']
        if User.query.filter_by(username=username).first():
            error = 'Username already exists!'
            return render_template('signup.html', error=error)
        else:
            user = User(username=username, password=bcrypt.generate_password_hash(password).decode('utf-8'), monthly_income=monthly_income)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth.login'))
    return render_template('signup.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if 'user_id' in session:
        return redirect(url_for('dashboard.dashboard'))
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            session['user_id'] = user.id
            session['username'] = user.username
            return redirect(url_for('dashboard.dashboard'))
        else:
            error = 'Invalid credentials'
            return render_template('login.html', error=error)
    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('username', None)
    return redirect(url_for('index'))