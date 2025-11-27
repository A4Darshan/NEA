from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import secrets

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = secrets.token_hex(32)
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)

@app.route('/')
def index():
    return render_template('index_flask.html')

@app.route('/save_data', methods=['POST'])
def save_data():
    username = request.form.get('username')
    password = request.form.get('password')
    first_name = request.form.get('first_name')
    surname = request.form.get('surname')

    new_user = User(username=username, password=password, first_name=first_name, surname=surname)
    db.session.add(new_user)
    db.session.commit()

    return f"Data saved. ID: {new_user.id}"

@app.route('/login', methods=['POST'])
def login():
    entered_username = request.form.get('entered_username')
    entered_password = request.form.get('entered_password')
    user_id = int(request.form.get('user_id'))

    user = User.query.get(user_id)

    if user and user.username == entered_username and user.password == entered_password:
        return f"Login successful. First Name: {user.first_name}"
    else:
        return "Incorrect username or password"

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)