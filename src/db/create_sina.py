from flask import Flask
from flaskext.sqlalchemy import SQLAlchemy
import datetime
from create import app

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
	follow_count = db.Column(db.Integer)
	fans_count = db.Column(db.Integer)
	tweet_count = db.Column(db.Integer)
	favourite_count = db.Column(db.Integer)
	create_at = db.Column(db.DateTime)
	following = db.Column(db.String(16))
	verified = db.Column(db.Integer)
	
	def __init__(self, user):
		self.uid=user.id
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
		self.follow_count=user.friends_count
		self.fans_count=user.followers_count
		self.tweet_count=user.statuses_count
		self.favourite_count=user.favourites_count
		self.following = user.following
		self.create_at=user.created_at
		self.verified= (lambda x:1 if x else 0)(user.verified)

	def __repr__(self):
		return '%s(%s)' % (self.screen, self.uid)
		
	def setSame(self,same):
		self.uid=same.uid
		self.screen=same.screen
		self.name=same.name
		self.province=same.province
		self.city=same.city
		self.location=same.location
		self.description=same.description
		self.url=same.url
		self.profile_image_url=same.profile_image_url
		self.domain=same.domain
		self.gender=same.gender
		self.follow_count=same.follow_count
		self.fans_count=same.fans_count
		self.tweet_count=same.tweet_count
		self.favourite_count=same.favourite_count
		self.following = same.following
		self.create_at=same.create_at
		self.verified=same.verified
		
	def json(self):
		obj = {'uid':self.uid, 'screen':self.screen, 'name':self.name}
		obj['province']=self.province
		obj['city']=self.city
		obj['location']=self.location
		obj['description']=self.description
		obj['url']=self.url
		obj['profile_image_url']=self.profile_image_url
		obj['domain']=self.domain
		obj['gender']=self.gender
		obj['follow_count']=self.follow_count
		obj['fans_count']=self.fans_count
		obj['tweet_count']=self.tweet_count
		obj['favourite_count']=self.favourite_count
		obj['following']=self.following
		obj['create_at']=str(self.create_at)
		obj['verified']=self.verified
		return obj

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
		self.create_at=tweet.created_at
		self.retid=0
		
	def __repr__(self):
		return '%s,%s' % (self.tid,self.content)
	

if __name__ == '__main__':
	db.drop_all()
	db.create_all()
