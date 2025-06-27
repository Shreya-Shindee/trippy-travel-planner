from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

class TravelPlan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    destination = db.Column(db.String(120), nullable=False)
    dates = db.Column(db.String(120), nullable=False)
    people_count = db.Column(db.Integer, nullable=False)
    interests = db.Column(db.Text, nullable=True)
    budget = db.Column(db.Float, nullable=True)
    itinerary = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    user = db.relationship('User', backref=db.backref('travel_plans', lazy=True))

    def __repr__(self):
        return f'<TravelPlan {self.destination} for user {self.user_id}>'
