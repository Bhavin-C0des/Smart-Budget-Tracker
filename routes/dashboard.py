from flask import Blueprint, render_template, request, session, redirect, url_for
from models.models import db, User

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/dashboard')
def dashboard():
    if 'user_id' in session:
        return render_template('dashboard.html')
    return redirect(url_for('auth.login'))



