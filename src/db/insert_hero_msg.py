# -*- coding: utf-8 -*-
from create import db, Msg, Msg_Operate

def insert(db):
	#Msg:uid, hid, floor, content
	db.session.add(Msg(1999250817, 8, 1, '小小好利害啊！！'))
	db.session.add(Msg(1999250817, 8, 2, '我不在会有小小！！'))
	db.session.add(Msg(1999250817, 8, 3, '测试测试！！'))
	db.session.add(Msg(1999250817, 8, 4, '测试测试！！'))
	db.session.add(Msg(1999250817, 8, 5, '测试测试！！'))
	db.session.add(Msg(1999250817, 8, 6, '测试测试！！'))
	db.session.add(Msg(1999250817, 8, 7, '测试测试！！'))
	db.session.add(Msg(1999250817, 8, 8, '测试测试！！'))
	db.session.add(Msg(1999250817, 8, 9, '测试测试！！'))
	db.session.add(Msg(1999250817, 8, 10, '测试测试！！'))
	
	#Msg_Operate: uid, mid, action, content=None
	db.session.add(Msg_Operate(1999250817,1,'up'))
	db.session.add(Msg_Operate(1999250817,1,'down'))
	
if __name__ == '__main__':
	insert(db)
	db.session.commit()
