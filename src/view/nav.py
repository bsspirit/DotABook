# -*- coding: utf-8 -*-
from flask import Module, render_template, session, redirect, url_for, current_app

view = Module(__name__)

@view.route('/')
def index():
	return render_template('index.html',STATIC=current_app.config['STATIC_PATH'])

@view.route('/contact')
def contact():
	return render_template('contact.html',STATIC=current_app.config['STATIC_PATH'])
	
@view.route('/about')
def about():
	return render_template('about.html',STATIC=current_app.config['STATIC_PATH'])
