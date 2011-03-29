from flask import Flask
from flaskext.sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://dotabook:dota@localhost/dotabook'

db = SQLAlchemy(app)

class Sina_User(db.Model):
	__tablename__ = 't_sina_user'
	id = db.Column(db.Integer, primary_key=True)
	uid = db.Column(db.BigInteger, unique=True)
	screen = db.Column(db.String(64), unique=True)
	name = db.Column(db.String(64))
	province = db.Column(db.String(64))
	city = db.Column(db.Integer)
	location = db.Column(db.String(64))
	description = db.Column(db.String(256))
	url = db.Column(db.String(256))
	profile_image_url = db.Column(db.String(256))
	domain = db.Column(db.String(64))
	gender = db.Column(db.String(1))
	followers_count = db.Column(db.Integer)
	friends_count = db.Column(db.Integer)
	statuses_count = db.Column(db.Integer)
	favourites_count = db.Column(db.Integer)
	create_at = db.Column(db.DateTime)
	verified = db.Column(db.String(1))
	
	def __init__(self, user):
		self.uid=user.uid
		self.screen=user.screen_name
		self.name=user.name
		self.province=user.province
		self.city=user.city
		self.location=user.location
		self.description=user.description
		self.url=user.url
		self.profile_image_url=user.profile_image_url
		self.domain=user.domain
		self.gender=user.gender
		self.follow_count=user.followers_count
		self.fans_count=user.friends_count
		self.tweet_count=user.statuses_count
		self.favourite_count=user.favourites_count
		self.create_at=user.create_at
		self.verified=user.verified

	def __repr__(self):
		return '%s(%s)' % (self.screen_name, self.uid)

class Sina_tweet(db.Model):
	__tablename__ = 't_sina_tweet'
	id = db.Column(db.Integer, primary_key=True)
	tid = db.Column(db.BigInteger, unique=True)
	uid = db.Column(db.BigInteger)
	content = db.Column(db.String(256))
	bmiddle = db.Column(db.String(256)) 
	thumbnail = db.Column(db.String(256))
	original = db.Column(db.String(256))
	source = db.Column(db.String(256))
	create_at = db.Column(db.DateTime)
	retid = db.Column(db.BigInteger)
	
	def __init__(self,tweet):
		self.tid=tweet.id
		self.uid=tweet.user.id
		self.content=tweet.text
		self.bmiddle=tweet.bmiddle_pic
		self.thumbnail=tweet.thumbnail_pic
		self.original=tweet.original_pic
		self.source=tweet.source
		self.create_at=tweet.create_at
		self.retid=0
		
	def __repr__(self):
		return '%s,%s' % (self.tid,self.content)
	

if __name__ == '__main__':
	db.drop_all()
	db.create_all()
