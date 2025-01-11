from flask import Flask, render_template, request, session
from models.models import db, User
from routes import register_blueprints
import os
import dotenv

dotenv.load_dotenv()

app = Flask(__name__)

app.secret_key = os.getenv("app_secret_key")

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

db.init_app(app)

register_blueprints(app)

@app.route("/")
def index():
    return render_template("index.html")

if '__main__' == __name__:
    app.run(debug=True)