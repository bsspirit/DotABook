# -*- coding: utf-8 -*-
from flask import current_app
from weibopy.auth import OAuthHandler, API
from db.create_sina import db,Sina_User

consumer_key = '2967452232'
consumer_secret = '0fb77c003faf71cc503751829f118057'

def save_sina_user(user, uid=None, screen=None):
	db_user=None
	if uid == None:
		db_user = Sina_User.query.filter(Sina_User.screen==screen).first()
	else:
		db_user = Sina_User.query.filter(Sina_User.uid==uid).first()
	
	if db_user == None:
		db.session.add(user)
	else:
		db_user.setSame(user)
		db.session.merge(db_user)
		db.session.flush()
	db.session.commit()

class sinaAPI():
	def __init__(self, token, tokenSecret):
		self.auth = OAuthHandler(consumer_key, consumer_secret)
		self.auth.setToken(token, tokenSecret)
		self.api = API(self.auth)
		
	# basic
	def getTweet_ById(self, tid):
		return self.api.get_status(id=tid)
	
	def sendTweet(self, tweet):
		return self.api.update_status(status=tweet)
	
	def sendTweetImage(self,tweet,file):
		return self.api.upload(filename=file, status=tweet)
	
	# user
	def getUser_byScreen(self, screen):
		sina_user = Sina_User(self.api.get_user(screen_name=screen))
		current_app.logger.info(sina_user.verified)
		save_sina_user(user=sina_user,screen=screen)
		return sina_user

	def getUser_byId(self, uid):
		sina_user = Sina_User(self.api.get_user(id=uid))
		save_sina_user(user=sina_user,uid=uid)	
		return sina_user
	

if __name__ == '__main__':
	import random
	api = sinaAPI('0f58140e570dcab866a6d892b34b10d5', 'c2d600a6836929a9ce82489846caea2e')
	
	#basic
	tid = api.sendTweet('测试DotABook应用--%s' % random.randint(0, 100 * 100)).id
#	print api.getTweet_ById(tid)
	
	#user
	u = api.getUser_byId(1999250817)
	print '%s' % (api.getUser_byScreen('Conan_Z').screen_name)
#	print '%s' % (api.getUser_byId(1999250817).screen_name)

	
	
#	//basic
#    String getTweetById(long id) throws WeiboException;
#    String sendTweet(String text) throws WeiboException;
#    String sendTweetImage(String text, ImageItem image) throws WeiboException;//TODO: NOT DONE
#    String deleteTweetById(long id) throws WeiboException;
#
#    // Comment
#    String commentTweetById(String comment, long tid) throws WeiboException;
#    String getCommentById(long tid) throws WeiboException;
#    String getCommentById(long tid, int page, int count) throws WeiboException;
#    String commentTweetByIdAndCid(String comment, long tid, long cid) throws WeiboException;
#    String replyTweetByIdAndCid(String comment, long tid, long cid) throws WeiboException;
#    String repostTweet(long tid, String Comment) throws WeiboException;
#
#    // timeline
#    String homeTimeline() throws WeiboException;
#    String homeTimeline(int page, int count, long sinceId, long maxId) throws WeiboException;
#    String publicTimeline() throws WeiboException;
#    String publicTimeline(long sinceId) throws WeiboException;
#    String friendsTimeline() throws WeiboException;
#    String friendsTimeline(int page, int count, long sinceId, long maxId) throws WeiboException;
#    String userTimeline(int uid) throws WeiboException;
#    String userTimeline(int uid, int page, int count, long sinceId, long maxId) throws WeiboException;
#    String commentsTimeline() throws WeiboException;
#    String commentsTimeline(String source, int page, int count, long sinceId, long maxId) throws WeiboException;
#    
#    //status
#    String unread() throws WeiboException,JSONException ;
#    String counts(String ids) throws WeiboException;
#    String mentions() throws WeiboException;
#    
#    //user
#    String getFollow() throws WeiboException;
#    String getFollowIdsById(int uid) throws WeiboException;
#    String getFollowIds() throws WeiboException;
#    String getFans() throws WeiboException;
#    String getFansIdsById(int uid) throws WeiboException;
#    String getFansIds() throws WeiboException;
#    String getUserById(int uid) throws WeiboException;
#    String followUser(int uid) throws WeiboException;
#    String unfollowUser(int uid) throws WeiboException;
#    String relateUser(int sourceId, int targetId) throws WeiboException;
#    String relateUser(int uid) throws WeiboException;
#    
#    //account
#    String updateProfile(String name, String email, String url, String location, String description) throws WeiboException;//name,description
#    String uploadPortrait(File portrait) throws WeiboException;
#    String logout() throws WeiboException;
#    String register(String email, String password, String ip,String nick, String gender) throws WeiboException;//not work
#    String credentials() throws WeiboException;
#    String logon() throws WeiboException;
#    String logon(String username, String password) throws WeiboException;
#    
#    //favorite
#    String getFavorites() throws WeiboException;
#    String favorite(long tid) throws WeiboException;
#    String unfavorite(long tid) throws WeiboException;
#    
#    //message
#    String getMessages() throws WeiboException ;
#    String getMessages(int page, int count, long sinceId, long maxId) throws WeiboException;
#    String getSendBoxMessages() throws WeiboException;
#    String sendMessage(int uid, String text) throws WeiboException;
#    String deleteMessages(int mid) throws WeiboException;
