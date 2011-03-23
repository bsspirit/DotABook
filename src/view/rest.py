# -*- coding: utf-8 -*-
from flask import Module, current_app
from db.create import Hero, Hero_Attr, Hero_Image, Hero_Skill
from db.create import Item, Item_Compound, Item_Skill

view = Module(__name__)

@view.route('/hero/<hid>')
def hero_all_json(hid):
	#current_app.config['SERVER_PATH']
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
	
@view.route('/hero/html/all')
def hero_html_all():
	heroes = Hero.query.all()
	
	divs = 'var heroes = new Array();\n'
	for hero in heroes:
		hid = hero.id
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
		
		divs+='heroes[%s]="%s"\n' % (hid,content) 
		
	return divs
	
@view.route('/item/html/all')
def item_html_all():
	items = Item.query.all()
	
	items_map ={}
	for item in items:
		items_map["id"+str(item.id)]= item
		
	divs = 'var items = new Array();\n'
	for item in items:
		iid = item.id
		if item.category=='R':continue;		
		content =  "<div class='tooltip_item'>"
		content += "<h3>"+item.namecn.encode('utf8')+" - "+item.name.encode('utf8')+"</h3>"
		content += "<p>商店:"+item.shop.encode('utf8')+"<span class='price'>"+str(item.price)+"</span><p/>"
		content += "<h4>属性:</h4>"
		content += "<p>"+item.description.encode('utf8')+"<p/>"
		content += "<p class='info'>"+item.info.encode('utf8')+"<p/>"

		skills = Item_Skill.query.filter(Item_Skill.iid==item.id).all()		
		if len(skills)>0:
			content += "<h4>技能:</h4><br/>"
			content += "<ul>"
			for skill in skills:
				content += "<li>"+skill.namecn.encode('utf8')
				content += "（"
				if skill.ability.encode('utf8') == 'P':content += "被动"
				elif skill.ability.encode('utf8') == 'A':content += "主动"
				content += "）:<br/>"+skill.description.encode('utf8')+"</li>"
			content += "</ul>"

		content +="<br/>"
		if item.category=='C':
			content += "<h4>合成需要:</h4><br/>"
			content += "<ul>"
			coms = Item_Compound.query.filter(Item_Compound.iid_1==item.id).all()
			for com in coms:
				sub = items_map["id"+str(com.iid_2)]
				content += "<li>"+ "<img class='img20' src='"+current_app.config['STATIC_PATH']+"dota/image/items/38/"+sub.picture.encode('utf8')+"'/>"+sub.namecn.encode('utf8')
				content +=" <span class='price'>"+str(sub.price)+"</span>"
			content += "</ul>"	
			
		content +="</div>"
		
		divs+='items[%s]="%s"\n' % (iid,content) 
		
	return divs

