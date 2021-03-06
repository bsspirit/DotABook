# -*- coding: utf-8 -*-
from flask import Module, session, request, redirect, current_app, url_for
from weibopy.auth import OAuthHandler
from sinaAPI import sinaAPI, consumer_key, consumer_secret
from db.create import User, db

view = Module(__name__)

class WebOAuthHandler(): 
	def __init__(self):
		self.back_url = current_app.config['SERVER_PATH']+'oauth/callback'
		self.oauth = OAuthHandler(consumer_key, consumer_secret)
	def get_authorizate_url(self):
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
	
	api = sinaAPI(session['token'].key, session['token'].secret)
	user = api.getUser_byScreen(o.get_username())
	session['user'] = user
	session['login'] = True

	session['admin'] = False
	if user.uid==1999250817:
		session['admin'] = True

	
	db_user = User.query.filter(User.uid==user.uid).first()
	if db_user == None:
		db.session.add(User(user.uid, user.name, user.screen, 'sina', session['token'].key, session['token'].secret))
	else:
		db_user.username = user.name
		db_user.nickname = user.screen
		db.session.merge(db_user)	
	db.session.commit()


	backurl = current_app.config['SERVER_PATH']
	if session.get('backurl', None) != None:
		backurl = session['backurl']
	return redirect(backurl)
