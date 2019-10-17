#from app import db
import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
	__tablename__ = 'users'

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(300),unique=True,nullable=False)
	password = db.Column(db.String(300),nullable=False)
	registered_on = db.Column(db.DateTime, nullable=True)
	texts = db.relationship('Text', backref='users', lazy=True)

	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.registered_on = datetime.datetime.now()

	def dictionarize(self):
		return {
			"id": self.id,
			"username": self.username,
			"texts": self.texts
		}

class Text(db.Model):
	__tablename__ = 'texts'

	id = db.Column(db.Integer, primary_key=True)
	text = db.Column(db.String(140),nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'),
        nullable=False)

	texted_on = db.Column(db.DateTime, nullable=True)

	def __init__(self, text, user_id):
		self.user_id = user_id
		self.text = text
		self.texted_on = datetime.datetime.now()

	def dictionarize(self):
		return {
			"id": self.id,
			"text": self.text,
			"user_id": self.user_id,
			"username": User.query.filter_by(id=self.user_id).first().username,
			"texted_on": self.texted_on
		}