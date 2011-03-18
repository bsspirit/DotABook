from flask import Flask
from flaskext.sqlalchemy import SQLAlchemy
app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/conan/workspace/app/DotABook/db/dota.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://dotabook:dota@localhost/dotabook'

db = SQLAlchemy(app)

class Version(db.Model):
	__tablename__ = 't_dota_version'
	id = db.Column(db.Integer, primary_key=True)
	version = db.Column(db.String(16), unique=True)
	description = db.Column(db.Text)
	
	def __init__(self, version, description , id=0):
		if id != 0: self.id = id
		self.version = version
		self.description = description

	def __repr__(self):
		return 'Version %s: %s' % (self.version, self.description)

class Hero(db.Model):
	__tablename__ = 't_dota_hero'
	id = db.Column(db.Integer, primary_key=True)
	vid = db.Column(db.Integer)
	name = db.Column(db.String(64))
	namecn = db.Column(db.String(64))
	description = db.Column(db.Text)
	
	def __init__(self, vid, name, namecn, description, id=0):
		if id != 0: self.id = id
		self.vid = vid
		self.name = name
		self.namecn = namecn
		self.description = description
	
	def __repr__(self):
		return '%s(%s): %s' % (self.namecn, self.name, self.description)
	
	def json(self):
		return '{"hid":%s,"name":"%s","namecn":"%s","description":"%s","vid":%s}' % (self.id, self.name, self.namecn, self.description, self.vid)

class Hero_Attr(db.Model):
	__tablename__ = 't_dota_hero_attr'
	id = db.Column(db.Integer, primary_key=True)
	hid = db.Column(db.Integer)
	hp = db.Column(db.Integer)
	mp = db.Column(db.Integer)
	basic = db.Column(db.String(1))
	affilication = db.Column(db.String(1))
	damage = db.Column(db.String(16))
	armor = db.Column(db.Float)
	move_speed = db.Column(db.Integer)
	attack_range = db.Column(db.Integer)
	attack_animation = db.Column(db.String(16))
	casting_animation = db.Column(db.String(16))
	attack_time = db.Column(db.Float)
	missile_speed = db.Column(db.Integer)
	sight_range = db.Column(db.String(16))
	intelligence = db.Column(db.Integer)
	agility = db.Column(db.Integer)
	strength = db.Column(db.Integer)
	goup_intelligence = db.Column(db.Float)
	goup_agility = db.Column(db.Float)
	goup_strength = db.Column(db.Float)
	
	def __init__(self, hid, basic, hp, mp, affilication, damage, armor, move_speed, attack_range, attack_animation, casting_animation, attack_time,
				missile_speed, sight_range, intelligence, agility, strength, goup_intelligence, goup_agility, goup_strength, id=0):
		if id != 0: self.id = id
		self.hid = hid
		self.basic = basic
		self.hp = hp
		self.mp = mp
		self.affilication = affilication
		self.damage = damage
		self.armor = armor
		self.move_speed = move_speed
		self.attack_range = attack_range
		self.attack_animation = attack_animation
		self.casting_animation = casting_animation
		self.attack_time = attack_time
		self.missile_speed = missile_speed
		self.sight_range = sight_range
		self.intelligence = intelligence
		self.agility = agility
		self.strength = strength
		self.goup_intelligence = goup_intelligence
		self.goup_agility = goup_agility
		self.goup_strength = goup_strength
	
	def __repr__(self):
		return '%s(%s): speed(%s)' % (self.hid, self.basic, self.move_speed)
	
	def json(self):
		return '{"hid":%s,"basic":"%s","move_speed":%s,"attack_range":%s,"strength":%s,"agility":%s,"intelligence":%s,"goup_strength":%s,"goup_agility":%s,"goup_intelligence":%s}' % (self.hid, self.basic, self.move_speed, self.attack_range, self.strength, self.agility, self.intelligence, self.goup_strength, self.goup_agility, self.goup_intelligence)

class Hero_Image(db.Model):
	__tablename__ = 't_dota_hero_image'
	id = db.Column(db.Integer, primary_key=True)
	hid = db.Column(db.Integer)
	image45 = db.Column(db.String(128))
	image64 = db.Column(db.String(128))
	comic = db.Column(db.String(128))
	
	def __init__(self, hid, image45, image64, comic):
		self.hid = hid
		self.image45 = image45
		self.image64 = image64
		self.comic = comic
	
	def __repr__(self):
		return '45(%s),64(%s),comic(%s)' % (self.image45, self.image64, self.comic)
	
	def json(self):
		return '{"hid":%s,"image45":"%s","image64":"%s","comic":"%s"}' % (self.hid, self.image45, self.image64, self.comic)
	

class Hero_Skill(db.Model):
	__tablename__ = 't_dota_hero_skill'
	id = db.Column(db.Integer, primary_key=True)
	hid = db.Column(db.Integer)
	name = db.Column(db.String(64))
	namecn = db.Column(db.String(64))
	hotkey = db.Column(db.String(1))
	ability = db.Column(db.String(16))
	target = db.Column(db.String(16))
	image = db.Column(db.String(128))
	description = db.Column(db.Text(2048))
	note = db.Column(db.Text(2048))
	
	def __init__(self, hid, name, namecn, hotkey, ability, target, image, note, description, id=0):
		if id != 0: self.id = id
		self.hid = hid
		self.name = name
		self.namecn = namecn
		self.hotkey = hotkey
		self.ability = ability
		self.target = target
		self.image = image
		self.note = note
		self.description = description
	
	def __repr__(self):
		return '%s(%s): %s' % (self.namecn, self.name, self.description)
	
	def json(self):
		return '{"hid":%s,"name":"%s","namecn":"%s"}' % (self.hid, self.name, self.namecn)
	

class Hero_Skill_Level(db.Model):
	__tablename__ = 't_dota_hero_skill_level'
	id = db.Column(db.Integer, primary_key=True)
	sid = db.Column(db.Integer)
	level = db.Column(db.Integer)
	mana_cost = db.Column(db.Integer)
	cooldown = db.Column(db.Integer)
	casting_range = db.Column(db.Integer)
	area = db.Column(db.Integer)
	duration = db.Column(db.String(64))
	target = db.Column(db.String(16))
	effect = db.Column(db.Text(2048))
	
	def __init__(self, sid, level, mana_cost, cooldown, casting_range, area, duration, target, effect, id=0):
		if id != 0: self.id = id
		self.sid = sid
		self.level = level
		self.mana_cost = mana_cost
		self.cooldown = cooldown
		self.casting_range = casting_range
		self.area = area
		self.duration = duration
		self.target = target
		self.effect = effect
	
	def __repr__(self):
		return '%s(%s): %s' % (self.sid, self.level, self.effect)
		
class Item(db.Model):
	__tablename__ = 't_dota_item'
	id = db.Column(db.Integer, primary_key=True)
	vid = db.Column(db.Integer)
	name = db.Column(db.String(64))
	namecn = db.Column(db.String(64))
	picture = db.Column(db.String(512))
	price = db.Column(db.Integer)
	shop = db.Column(db.String(64))
	category = db.Column(db.String(16))
	description = db.Column(db.Text(2048))
	info = db.Column(db.Text(2048))
	
	def __init__(self,vid, name,namecn, picture, price, shop, category, description,info, id=0):
		if id != 0: self.id = id
		self.vid = vid
		self.name = name
		self.namecn = namecn
		self.picture = picture
		self.price = price
		self.shop=shop
		self.description = description
		self.info = info
		self.category = category #(reel:r,composite:c,atom:a)
		
	def __repr__(self):
		return '%s(%s): %s,%s' % (self.namecn, self.name, self.price, self.description)
		
class Item_Compound(db.Model):
	__tablename__ = 't_dota_item_compound'
	id = db.Column(db.Integer, primary_key=True)
	iid_1 = db.Column(db.Integer)
	iid_2 = db.Column(db.Integer)
	
	def __init__(self, iid1, iid2):
		self.iid_1=iid1
		self.iid_2=iid2
		
	def __repr__(self):
		return '%s - %s' % (self.iid_1, self.iid_2)
	
class Item_Skill(db.Model):
	__tablename__='t_dota_item_skill'
	id = db.Column(db.Integer,primary_key=True)
	iid = db.Column(db.Integer)
	name = db.Column(db.String(64))
	namecn = db.Column(db.String(64))
	ability = db.Column(db.String(16))
	mana_cost = db.Column(db.Integer)
	cooldown = db.Column(db.Integer)
	duration = db.Column(db.String(64))
	casting_range = db.Column(db.Integer)
	area = db.Column(db.Integer)
	description = db.Column(db.Text)
	note = db.Column(db.Text)
	
	
	def __init__(self,iid, name, namecn, ability, mana_cost, cooldown, casting_range, area, duration, description,note):
		self.iid = iid
		self.name = name
		self.namecn = namecn
		self.ability = ability
		self.mana_cost = mana_cost
		self.cooldown = cooldown
		self.duration = duration
		self.casting_range = casting_range
		self.area=area
		self.description = description
		self.note=note
		
	def __repr__(self):
		return '%s(%s): %s' % (self.namecn, self.name, self.description)
	
class User(db.Model):
	__tablename__ = 't_user'
	id = db.Column(db.Integer, primary_key=True)
	uid = db.Column(db.BigInteger, unique=True)
	username = db.Column(db.String(64))
	nickname = db.Column(db.String(64))
	source = db.Column(db.String(32))
	token_key = db.Column(db.String(64))
	token_secret = db.Column(db.String(64))
	
	def __init__(self, uid, username, nickname, source, token_key, token_secret, id=0):
		if id != 0: self.id = id
		self.uid = uid
		self.username = username
		self.nickname = nickname
		self.source = source
		self.token_key = token_key
		self.token_secret = token_secret
		
	def __repr__(self):
		return '%s(%s) %s,%s' % (self.username, self.nickname, self.uid, self.source)

class Grade(db.Model):
	__tablename__ = 't_dota_grade'
	id = db.Column(db.Integer, primary_key=True)
	uid = db.Column(db.BigInteger)
	hid = db.Column(db.Integer)
	score = db.Column(db.Float)
	catalog = db.Column(db.String(32))#dps,pull,gank,assist,defend
	
	def __init__(self, uid, hid, score, catalog, id=0):
		if id != 0: self.id = id
		self.uid = uid
		self.hid = hid
		self.score = score
		self.catalog = catalog
		
	def __repr__(self):
		return '%s:%s,%s,%s' % (self.hid, self.score, self.catalog, self.uid)
	
class Config(db.Model):
	__tablename__ = 't_dota_config'
	id = db.Column(db.Integer, primary_key=True)
	key = db.Column(db.String(64), unique=True)
	value = db.Column(db.String(512))
	
	def __init__(self, key, value):
		self.key = key
		self.value = value
	
	def __repr__(self):
		return '%s: %s' % (self.key, self.value) 


if __name__ == '__main__':
	db.drop_all()
	db.create_all()
