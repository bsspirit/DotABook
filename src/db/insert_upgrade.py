# -*- coding: utf-8 -*-
from create import db, Upgrade

def insert(db):
	#Upgrade:datetag, title, desc
	db.session.add(Upgrade(20110324,'在首页增加新浪登录提示','在首页增加新浪登录提示'))
	db.session.add(Upgrade(20110324,'增加英雄评分发布到微博提示','增加英雄评分发布到微博提示'))
	db.session.add(Upgrade(20110325,'增加每日更新提示','增加每日更新提示'))
	db.session.add(Upgrade(20110325,'英雄详细信息界面更新','英雄详细信息界面更新'))
	db.session.add(Upgrade(20110327,'增加英雄评论','增加英雄评论'))


if __name__ == '__main__':
	insert(db)
	db.session.commit()
