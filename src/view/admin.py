# -*- coding: utf-8 -*-
from flask import Module, render_template, session, redirect, url_for, current_app, request
from db.create import db,Upgrade
import util.mydate as mydate

view = Module(__name__)

@view.route('/')
def admin():
	if not session.get('admin', False):
		return redirect(url_for('nav.index'))

	return render_template('admin/admin.html',STATIC=current_app.config['STATIC_PATH'], SERVER=current_app.config['SERVER_PATH'])
	
@view.route('/upgrade',methods=['POST','GET'])
def upgrade():
	if not session.get('admin', False):
		return redirect(url_for('nav.index'))
		
	if request.method == 'POST':
		db.session.add(Upgrade(request.form['datetag'], request.form['title'], request.form['description']))
		db.session.commit()
		
	return render_template('admin/admin_upgrade.html',STATIC=current_app.config['STATIC_PATH'], SERVER=current_app.config['SERVER_PATH'])
