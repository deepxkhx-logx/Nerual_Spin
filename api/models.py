from werkzeug.security import generate_password_hash
from config import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = generate_password_hash(password)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    image_file = db.Column(db.LargeBinary, nullable=True)  # Changed to LargeBinary

    user = db.relationship('User', backref=db.backref('projects', lazy=True))

    @property
    def author(self):
        return self.user.username

    def __init__(self, title, description, user_id, image_file=None):
        self.title = title
        self.description = description
        self.user_id = user_id
        self.image_file = image_file