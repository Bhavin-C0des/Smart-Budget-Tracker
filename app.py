from flask import Flask, render_template, request, session
from models import db, User

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

db.init_app(app)

@app.route("/")
def index():
    return render_template("index.html")

if '__main__' == __name__:
    app.run(debug=True)