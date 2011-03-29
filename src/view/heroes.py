# -*- coding: utf-8 -*-
from flask import Module, render_template, request, jsonify, session, redirect, current_app
from db.create import db, Hero, Hero_Attr, Hero_Image, Hero_Skill, Hero_Skill_Level, Grade, Item, Msg, Msg_Operate
from sina.sinaAPI import sinaAPI
import util.mydate as mydate

view = Module(__name__)

@view.route('/')
def heroes():
	heroes = Hero.query.all()
	h_images = {}
	for hero in heroes:
		h_images[hero.id] = Hero_Image.query.filter(Hero_Image.hid == hero.id).first()
	return render_template('hero/heroes.html', heroes=heroes, images=h_images, STATIC=current_app.config['STATIC_PATH'])

@view.route('/<name>')
def hero(name):
	if session.get('uid', None) == None:
		return redirect(current_app.config['SERVER_PATH']+'oauth/?backurl=' + request.url)
	
	hero = Hero.query.filter(Hero.name == name).first() 
	image = Hero_Image.query.filter(Hero_Image.hid == hero.id).first()
	attr = Hero_Attr.query.filter(Hero_Attr.hid == hero.id).first()
	skills = Hero_Skill.query.filter(Hero_Skill.hid == hero.id).all()
	
	levels = {}
	for skill in skills:
		level = Hero_Skill_Level.query.filter(Hero_Skill_Level.sid == skill.id).all()
		levels[skill.id] = level 
		
	return render_template('hero/hero.html', hero=hero, attr=attr, skills=skills, levels=levels, image=image,STATIC=current_app.config['STATIC_PATH'])
	
@view.route('/msg/<hid>',methods=['POST','GET'])
def hero_msgs(hid):
	uid = session['uid']
	api = sinaAPI(session['token'].key, session['token'].secret)
	user = api.getUser_byId(uid)
	
	if request.method=='POST':
		content = request.form['content']
		floor = Msg.query.filter(Msg.hid==hid).count()+1;
		db.session.add(Msg(uid, hid,floor, content))
		db.session.commit()
		
		if(request.form['send_sina']=='true'):
			hero = Hero.query.filter(Hero.id == hid).first()
			tweet  = "@"+user.screen_name.encode('utf8')
			tweet += " 对DOTA英雄 "+hero.namecn.encode('utf8')+" 评论："
			tweet += content.encode('utf8')
			tweet += " http://dotabook.info"
			
			api = sinaAPI(session['token'].key, session['token'].secret)
			api.sendTweet(tweet)
	
	page = int(request.args.get('p','1'))
	count = 10
	msgs_page = Msg.query.filter(Msg.hid==hid).order_by(Msg.id.desc()).paginate(page,count)	
	
	objs = []
	for msg in msgs_page.items:
		obj = {'hid':msg.hid,'mid':msg.id,'content':msg.content.encode('utf8'),'floor':msg.floor,'date':mydate.toString2(msg.create_date).encode('utf8')} 
		obj['uid'] = msg.uid
		obj['screen'] = user.screen_name.encode('utf8')
		obj['profile_image'] = user.profile_image_url

		ops = Msg_Operate.query.filter(Msg_Operate.mid==msg.id).all()
		ms_count = {'up':0,'down':0,'repost':0,'comment':0}
		for op in ops:
			if op.action=='up':ms_count['up']+=1
			elif op.action=='down':ms_count['down']+=1
			elif op.action=='repost':ms_count['repost']+=1
			elif op.action=='comment':ms_count['comment']+=1
			
		obj['count']=ms_count	
		objs.append(obj)
	return jsonify(msgs=objs,count=count,total=msgs_page.total, page=page)


@view.route('/msg/up/<int:mid>',methods=['GET','POST'])
def hero_msg_up(mid):
	submit = False
	if (request.method=='POST'):
		uid = session['uid']
		op = Msg_Operate.query.filter(Msg_Operate.mid==mid).filter(Msg_Operate.uid==uid).filter(Msg_Operate.action=='up').count()
		if op == 0:	
			db.session.add(Msg_Operate(uid,mid,'up'))
			db.session.commit()
		else :
			submit = True
	
	size = Msg_Operate.query.filter(Msg_Operate.mid==mid).filter(Msg_Operate.action=='up').count()
	return jsonify(mid=mid,size=size,submit=submit)
	
@view.route('/msg/down/<int:mid>',methods=['GET','POST'])
def hero_msg_down(mid):
	submit = False
	if (request.method=='POST'):
		uid = session['uid']
		op = Msg_Operate.query.filter(Msg_Operate.mid==mid).filter(Msg_Operate.uid==uid).filter(Msg_Operate.action=='down').count()
		if op == 0:
			db.session.add(Msg_Operate(uid,mid,'down'))
			db.session.commit()
		else:
			submit=True
	
	size = Msg_Operate.query.filter(Msg_Operate.mid==mid).filter(Msg_Operate.action=='down').count()
	return jsonify(mid=mid,size=size,submit=submit)



@view.route('/grade_send_tweet',methods=['POST'])
def hero_grade_sendTweet():
	tweet = session.get('grade_tweet')
	api = sinaAPI(session['token'].key, session['token'].secret)
	if tweet != None:
		api.sendTweet(tweet)
	session.pop('grade_tweet',None)
	return ''
	

@view.route('/grade/<hid>', methods=['GET', 'POST'])
def hero_grade(hid):
	uid = session['uid']
	if request.method == 'POST':
		hero = Hero.query.filter(Hero.id == hid).first()
		myGrades = Grade.query.filter(Grade.hid == hid).filter(Grade.uid == uid).all()
		if len(myGrades) > 0:
			for my in myGrades:
				if my.catalog == 'gank':my.score = request.form['gank'] 
				if my.catalog == 'push':my.score = request.form['push']
				if my.catalog == 'dps':my.score = request.form['dps']
				if my.catalog == 'defend':my.score = request.form['defend']
				if my.catalog == 'assist':my.score = request.form['assist'] 
				db.session.merge(my)
			db.session.commit()
			tweet  = "@"+session['screen'].encode('utf8')
			tweet += " 给DOTA英雄 "+hero.namecn.encode('utf8')+" 打分，"
			tweet += "gank:"+request.form['gank'].encode('utf8')+"分，"
			tweet += "push:"+request.form['push'].encode('utf8')+"分，"
			tweet += "dps:"+request.form['dps'].encode('utf8')+"分，"
			tweet += "辅助:"+request.form['assist'].encode('utf8')+"分，"
			tweet += "肉盾:"+request.form['defend'].encode('utf8')+"分."		
			session['grade_tweet'] = tweet+'http://dotabook.info'

		else: 
			if int(request.form['gank']) != 0 and int(request.form['push']) != 0 and int(request.form['dps']) != 0 and int(request.form['assist']) != 0 and int(request.form['defend']) != 0:
				db.session.add(Grade(uid, hid, request.form['gank'], 'gank'))
				db.session.add(Grade(uid, hid, request.form['push'], 'push'))
				db.session.add(Grade(uid, hid, request.form['dps'], 'dps')) 
				db.session.add(Grade(uid, hid, request.form['assist'], 'assist'))
				db.session.add(Grade(uid, hid, request.form['defend'], 'defend')) 
				db.session.commit()
				
				tweet  = "@"+session['screen'].encode('utf8')
				tweet += " 给DOTA英雄 "+hero.namecn.encode('utf8')+" 打分，"
				tweet += "gank:"+request.form['gank'].encode('utf8')+"分，"
				tweet += "push:"+request.form['push'].encode('utf8')+"分，"
				tweet += "dps:"+request.form['dps'].encode('utf8')+"分，"
				tweet += "辅助:"+request.form['assist'].encode('utf8')+"分，"
				tweet += "肉盾:"+request.form['defend'].encode('utf8')+"分."
				session['grade_tweet'] = tweet+'http://dotabook.info'
	
	myGrades = Grade.query.filter(Grade.hid == hid).filter(Grade.uid == uid).all()
	userGrades = Grade.query.filter(Grade.hid == hid).all()
	myObj = {'gank':0, 'push':0, 'dps':0, 'defend':0, 'assist':0}	 
	if len(myGrades) > 0:  
		for my in myGrades:
			if my.catalog == 'gank':myObj['gank'] = my.score
			if my.catalog == 'push':myObj['push'] = my.score
			if my.catalog == 'dps':myObj['dps'] = my.score
			if my.catalog == 'defend':myObj['defend'] = my.score
			if my.catalog == 'assist':myObj['assist'] = my.score
	
	userObj = {'gank':0, 'push':0, 'dps':0, 'defend':0, 'assist':0, 'count':0}	 	
	size = len(userGrades)
	if size > 0:
		for user in userGrades:
			if user.catalog == 'gank':   userObj['gank'] += int(user.score)
			if user.catalog == 'push':   userObj['push'] += int(user.score)
			if user.catalog == 'dps':    userObj['dps'] += int(user.score)
			if user.catalog == 'defend': userObj['defend'] += int(user.score)
			if user.catalog == 'assist': userObj['assist'] += int(user.score)
		
		userObj['gank'] /= (size / 5)
		userObj['push'] /= (size / 5)
		userObj['dps'] /= (size / 5)
		userObj['defend'] /= (size / 5)
		userObj['assist'] /= (size / 5)
		userObj['count'] = (size / 5)
	
	return jsonify(my=myObj, user=userObj, tweet=session.get('grade_tweet')) 
