# -*- coding: utf-8 -*-
from flask import Module, session, request, redirect, current_app
from weibopy.auth import OAuthHandler
from sinaAPI import sinaAPI, consumer_key, consumer_secret
from db.create import User, db

view = Module(__name__)

class WebOAuthHandler(): 
	def __init__(self):
		self.back_url = current_app.config['SERVER_PATH']+'oauth/callback'
		self.oauth = OAuthHandler(consumer_key, consumer_secret)
	def get_authorizate_url(self):
		print self.back_url
		return self.oauth.get_authorization_url() + '&oauth_callback=' + self.back_url

@view.route('/')
def oauth(): 
	backurl = request.args.get('backurl')
	o = WebOAuthHandler()
	session['oauth'] = o.oauth 
	session['backurl'] = backurl  
	return redirect(o.get_authorizate_url())

@view.route('/callback')
def oauth_callback(): 
	verifier = request.args.get('oauth_verifier')
	o = session['oauth']
	session.pop('oauth', None) 
	session['token'] = o.get_access_token(verifier)
	session['screen'] = o.get_username()
	
	api = sinaAPI(session['token'].key, session['token'].secret)
	user = api.getUser_byScreen(o.get_username())
	session['uid'] = user.id
	session['user'] = user
	
	db_user = User.query.filter(User.uid==user.id).first()
	if db_user == None:
		db.session.add(User(user.id, user.name, user.screen_name, 'sina', session['token'].key, session['token'].secret))
	else:
		db_user.name = user.name
		db_user.screen_name = user.screen_name
		db.session.merge(db_user)
	db.session.commit()

	backurl = current_app.config['SERVER_PATH']
	if session.get('backurl', None) != None:
		backurl = session['backurl']

	return redirect(backurl)


