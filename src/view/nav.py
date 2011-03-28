# -*- coding: utf-8 -*-
from flask import Module, render_template, session, redirect, url_for, current_app
from db.create import Upgrade
import util.mydate as mydate

view = Module(__name__)

@view.route('/')
def index():
	return render_template('index.html',STATIC=current_app.config['STATIC_PATH'], SERVER=current_app.config['SERVER_PATH'])

@view.route('/contact')
def contact():
	return render_template('contact.html',STATIC=current_app.config['STATIC_PATH'])
	
@view.route('/about')
def about():
	upgrade = {'today':mydate.toString2(mydate.yesterday()).decode('utf8')}
	upgrade['up'] = Upgrade.query.filter(Upgrade.datetag==mydate.toInt(mydate.yesterday())).all()
	return render_template('about.html',STATIC=current_app.config['STATIC_PATH'],upgrade=upgrade)
	
@view.route('/xd.html')
def xd():
	return render_template('xd.html')
