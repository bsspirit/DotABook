# -*- coding: utf-8 -*-
from flask import Module, render_template, request, jsonify, session, redirect, current_app
from db.create import db, Map

view = Module(__name__)

@view.route('/')
def maps():
	maps = Map.query.order_by(Map.id.desc()).all()
	return render_template('map/maps.html', maps=maps, STATIC=current_app.config['STATIC_PATH'])
