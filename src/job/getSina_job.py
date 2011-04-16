# -*- coding: utf-8 -*-
import sys
sys.path.append("/home/conan/workspace/app/DotABook/src")

from flask import Flask
from flaskext.sqlalchemy import SQLAlchemy
from weibopy.auth import OAuthHandler, API
from db.create_sina import db,Sina_User,Sina_Tweet

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://dotabook:dota@localhost/dotabook'
db = SQLAlchemy(app)

consumer_key = '2967452232'
consumer_secret = '0fb77c003faf71cc503751829f118057'


class sinaAPI():
	def __init__(self, token, tokenSecret):
		self.auth = OAuthHandler(consumer_key, consumer_secret)
		self.auth.setToken(token, tokenSecret)
		self.api = API(self.auth)
				
	def attr(self,obj,key):
		try:
			return obj.__getattribute__(key)
		except Exception,e:
			#print e
			return ''
		
	# basic
	def getTweet_ById(self, tid):
		return self.api.get_status(id=tid)
	
	def sendTweet(self, tweet):
		return self.api.update_status(status=tweet)
	
	def sendTweetImage(self,tweet,file):
		return self.api.upload(filename=file, status=tweet)
	
	# user
	def getUser_byScreen(self, screen):
		user = Sina_User(self.api.get_user(screen_name=screen))
		return user

	def getUser_byId(self, uid):
		user = Sina_User(self.api.get_user(id=uid))
		return user
		
	# timeline
	def getFriendsLine(self,since=0):
		tweets=[]
		users=[]
		
		timelines={}
		if since !=0:timelines = self.api.friends_timeline(since_id=since,count=50)
		else:timelines = self.api.friends_timeline()
		
		for line in timelines:
			tweet = Sina_Tweet(line)
			retweet_obj = self.attr(line,'retweeted_status')
			
			user_obj = self.attr(line,'user')
			user = Sina_User(user_obj)
			users.append(user)
			
			if retweet_obj !='':
				try:
					retweet=Sina_Tweet(retweet_obj)
					tweets.append(retweet)
					tweet.retid = retweet.tid
					reuser = Sina_User(self.attr(retweet_obj,'user'))
					users.append(reuser)
				except Exception,e:
					print e
			tweets.append(tweet)
		return tweets,users

class save():
	def __init__(self):
		pass
		
	def user(self,user):
		db_user = Sina_User.query.filter(Sina_User.uid==user.uid).first()
	
		if db_user == None:
			db.session.add(user)
		else:
			db_user.setSame(user)
			db.session.merge(db_user)
			db.session.flush()
		db.session.commit()
		
	def tweet(self,tweet):
		db_tweet = Sina_Tweet.query.filter(Sina_Tweet.tid==tweet.tid).first()
		if db_tweet == None:
			db.session.add(tweet)
		db.session.commit()

if __name__ == '__main__':
	import random
	api = sinaAPI('ee7fb33c9ab706122a881a8a00ff9fab', 'a65cf2c36d34810cb8073bd72e039659')
	
	#timeline
	since_id=0
	sina_tweet = Sina_Tweet.query.order_by(Sina_Tweet.create_at.desc()).first()
	if sina_tweet!=None:since_id=sina_tweet.tid
	print since_id
	
	ts,us = api.getFriendsLine(since_id)
	save = save()
	for t in ts:save.tweet(t)
	for u in us:save.user(u)
	db.session.commit()
