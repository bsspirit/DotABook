# -*- coding: utf-8 -*-
from create import db, Version

def insert(db):
	#Version:version, description , id=0
	db.session.add(Version('6.71b', 'DOTA 6.71b', 1))
	
if __name__ == '__main__':
	insert(db)
	db.session.commit()
