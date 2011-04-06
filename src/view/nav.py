# -*- coding: utf-8 -*-
from flask import Module, render_template, session, redirect, url_for, current_app
from db.create import Upgrade
import util.mydate as mydate

view = Module(__name__)

@view.route('/home')
def index():
	if session.get('path',False):
		redirect(url_for('init_session'))

#	tweets = Sina_Tweet.query.order_by(Sina_Tweet.id.desc()).all()
#	ts = [t.json() for t in tweets]
	
	return render_template('index.html')

@view.route('/logout')
def logout():
	session['login']=False
	session['admin']=False
	session.pop('backurl')
	session.pop('user')
	session.pop('token')
	return redirect(url_for('index'))

@view.route('/contact')
def contact():
	return render_template('contact.html')
	
@view.route('/about')
def about():
	return render_template('about.html')
	
@view.route('/')
def init_session():
	if session.get('path',False):
		session['login']=session.get('login',False)
		session['admin']=session.get('admin',False)
	
		path = {}
		path['STATIC'] = current_app.config['STATIC_PATH']
		path['SERVER'] = current_app.config['SERVER_PATH']
		path['LOCAL'] = current_app.config['LOCAL_PATH']
		session['path']=path
	
	return redirect(url_for('index'))	
