# -*- coding: utf-8 -*-
from flask import Module, render_template, session, redirect, url_for

view = Module(__name__)

@view.route('/')
def index():
	return render_template('index.html')

@view.route('/contact')
def contact():
	return render_template('contact.html')
