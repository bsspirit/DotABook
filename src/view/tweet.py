# -*- coding: utf-8 -*-
from flask import Module, current_app, session, jsonify, request
from db.create_sina import Sina_User,Sina_Tweet
import util.mydate as mydate
from sina.sinaAPI import sinaAPI

view = Module(__name__)

@view.route('/tweets')
def tweet():
	p,count = int(request.args.get('p','1')),10
	
	tweets_page = Sina_Tweet.query.order_by(Sina_Tweet.id.desc()).paginate(p,count)
	page={'p':p,'count':count,'total':tweets_page.total}
	
	ts,users,rets = [],{},{}
	for t in tweets_page.items:
		users[t.uid] = Sina_User.query.filter(Sina_User.uid==t.uid).first().json()
		ts.append(t.json())
		
		if t.retid:
			rets[t.retid] = Sina_Tweet.query.filter(Sina_Tweet.tid==t.retid).first().json()
	
	return jsonify(tweets=ts, retweets=rets, users=users, page=page)


