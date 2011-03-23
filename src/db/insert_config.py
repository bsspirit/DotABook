# -*- coding: utf-8 -*-
from create import db, Config, Grade

def insert(db):
	#Config: key,value
	db.session.add(Config('hero.basic.S', '力量 '))
	db.session.add(Config('hero.basic.A', '敏捷 '))
	db.session.add(Config('hero.basic.I', '智力'))
	db.session.add(Config('hero.affiliation.S', '近卫'))
	db.session.add(Config('hero.affiliation.N', '中立'))
	db.session.add(Config('hero.affiliation.C', '天灾'))
	db.session.add(Config('hero.skill.ability.A', '主动技能'))
	db.session.add(Config('hero.skill.ability.P', '被动技能'))
	db.session.add(Config('hero.skill.ability.T', '开关技能'))
	db.session.add(Config('hero.skill.target.U', '单位'))
	db.session.add(Config('hero.skill.target.P', '点'))
	db.session.add(Config('hero.skill.target.A', '区域'))
	db.session.add(Config('hero.skill.target.I', '即时'))
	db.session.add(Config('hero.skill.target.G', '地面'))
	db.session.add(Config('hero.skill.target.N', '无条件'))
	db.session.add(Config('hero.skill.level.target.E', '敌方'))
	db.session.add(Config('hero.skill.level.target.S', '自己'))
	db.session.add(Config('hero.skill.level.target.A', '友方'))
	db.session.add(Config('hero.skill.level.target.H', '英雄'))
	db.session.add(Config('hero.skill.level.target.U', '单位'))
	db.session.add(Config('hero.skill.level.target.B', '建筑'))
	db.session.add(Config('hero.skill.level.target.N', '没有'))


	#Grade:uid, hid, score, catalog,
	#db.session.add(Grade(1, 1, 7, 'defend'))
	#db.session.add(Grade(1, 1, 8, 'dps'))
	#db.session.add(Grade(1, 1, 6, 'push'))
	#db.session.add(Grade(1, 1, 7, 'gank'))
	#db.session.add(Grade(1, 1, 2, 'assist'))

if __name__ == '__main__':
	insert(db)
	db.session.commit()

