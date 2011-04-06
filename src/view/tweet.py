# -*- coding: utf-8 -*-
from flask import Module, current_app, session, jsonify
from db.create_sina import Sina_User,Sina_Tweet
import util.mydate as mydate
from sina.sinaAPI import sinaAPI

view = Module(__name__)

@view.route('/tweets')
def tweet():
	tweets = Sina_Tweet.query.order_by(Sina_Tweet.id.desc()).all()
	ts = [t.json() for t in tweets]
	return jsonify(tweets=ts)


