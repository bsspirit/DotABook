# -*- coding: utf-8 -*-
from flask import Module
from db.create import Hero, Hero_Attr, Hero_Image, Hero_Skill

view = Module(__name__)

@view.route('/hero/<hid>')
def hero_all_json(hid):
	hero = Hero.query.filter(Hero.id == hid).first()
	attr = Hero_Attr.query.filter(Hero_Attr.hid == hid).first()
	skills = Hero_Skill.query.filter(Hero_Skill.hid == hid).all()
	
	j_hero = '"info":%s' % hero.json()
	j_attr = '"attr":%s' % attr.json()
	
	j_skill = ''
	for skill in skills:
		j_skill += ',' + skill.json()
	j_skill = '[' + j_skill[1:] + ']'
	
	j_skills = '"skills":%s' % j_skill
	
	return '{%s,%s,%s}' % (j_hero, j_attr, j_skills)

@view.route('/hero/image/<hid>')
def hero_image_json(hid):
	image = Hero_Image.query.filter(Hero_Image.hid == int(hid)).first()
	return image.json()

@view.route('/hero/attr/<hid>')
def hero_attr_json(hid):
	attr = Hero_Attr.query.filter(Hero_Attr.hid == hid).first()
	return attr.json()	

@view.route('/hero/skill/<hid>')
def hero_skill_json(hid):
	skills = Hero_Skill.query.filter(Hero_Skill.hid == hid).all()
	json = ''
	for skill in skills:
		json += ',' + skill.json()
	json = '[' + json[1:] + ']'
	return json

@view.route('/hero/html/<hid>')
def hero_all_html(hid):
	hero = Hero.query.filter(Hero.id == hid).first()
	attr = Hero_Attr.query.filter(Hero_Attr.hid == hid).first()
	skills = Hero_Skill.query.filter(Hero_Skill.hid == hid).all()
	
	li_strength = ''
	if attr.basic == 'S':
		li_strength = "<span style=\'color:red;\'>力量:</span>"
	else:
		li_strength = "<span style=\'color:blue;\'>力量:</span>"
	li_strength += str(attr.strength) + "+" + str(attr.goup_strength)
	
	li_agility = ''
	if attr.basic == 'A':
		li_agility = "<span style=\'color:red;\'>敏捷:</span>"
	else:
		li_agility = "<span style=\'color:blue;\'>敏捷:</span>"
	li_agility += str(attr.agility) + "+" + str(attr.goup_agility)
	
	li_intelligence = ''
	if attr.basic == 'I':
		li_intelligence = "<span style=\'color:red;\'>智力:</span>"
	else:
		li_intelligence = "<span style=\'color:blue;\'>智力:</span>"
	li_intelligence += str(attr.intelligence) + "+" + str(attr.goup_intelligence)
	
	content  = "<div class='tooltip_hero'>"
	content += "<h3>"+hero.namecn.encode('utf8')+" - "+hero.name.encode('utf8')+"</h3>"
	content += "<p>"+hero.description.encode('utf8')+"</p>"
	content += "<ul>"
	content += "<li>"+li_strength+"</li>"
	content += "<li>"+li_agility+"</li>"
	content += "<li>"+li_intelligence+"</li>"
	content += "</ul>"
	content += "<br/>可以学习："+skills[0].namecn.encode('utf8')+"，"+skills[1].namecn.encode('utf8')+"，"+skills[2].namecn.encode('utf8')+"和<span style=\'color: #FF9000;\'>"+skills[3].namecn.encode('utf8')+"</span>"
	content += "<br/><br/>移动速度"+str(attr.move_speed)+"，射程"+str(attr.attack_range)
	content += "</div>"

	return content

