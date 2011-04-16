# -*- coding: utf-8 -*-
from flask import Module, render_template, session, redirect, url_for, current_app, request
from db.create import Upgrade
from db.create_sina import Sina_Tweet,Sina_User
import util.mydate as mydate

view = Module(__name__)

@view.route('/home')
def index():
	if not session.get('path',False):redirect(url_for('init'))
	
	p,count = int(request.args.get('p','1')),10
	tweets_page = Sina_Tweet.query.order_by(Sina_Tweet.id.desc()).paginate(p,count)
	page={'p':p,'count':count,'total':tweets_page.total}
	
	ts,users,rets = [],{},{}
	for t in tweets_page.items:
		users[t.uid] = Sina_User.query.filter(Sina_User.uid==t.uid).first()
		ts.append(t.json())
		if t.retid:rets[t.retid] = Sina_Tweet.query.filter(Sina_Tweet.tid==t.retid).first()
		
	
	return render_template('index.html', tweets=ts, retweets=rets, users=users, page=page)

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
	if not session.get('path',False):redirect(url_for('init'))
	
	return render_template('contact.html')
	
@view.route('/about')
def about():
	if not session.get('path',False):redirect(url_for('init'))
	
	return render_template('about.html')
	
@view.route('/')
def init():
	if not session.get('path',False):
		current_app.logger.info('path false')
		session['login']=session.get('login',False)
		session['admin']=session.get('admin',False)
	
		path = {}
		path['STATIC'] = current_app.config['STATIC_PATH']
		path['SERVER'] = current_app.config['SERVER_PATH']
		path['LOCAL'] = current_app.config['LOCAL_PATH']
		session['path']=path
	
	return redirect(url_for('index'))	
