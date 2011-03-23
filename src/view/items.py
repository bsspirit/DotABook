# -*- coding: utf-8 -*-
from flask import Module, render_template, request, jsonify, session, redirect, current_app
from db.create import db, Item

view = Module(__name__)

@view.route('/')
def heroes():
	items = Item.query.filter(Item.category!='R').all()
	return render_template('item/items.html', items=items, STATIC=current_app.config['STATIC_PATH'])
