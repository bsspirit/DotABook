# -*- coding: utf-8 -*-
from create import db, Map

def insert(db):
	#Map:version, namecn, category, filename, url, desc
	db.session.add(Map('6.68b_en', 'DotA V6.68b 英文版', 'N', 'DotA v6.68b.w3x', 'http://media.playdota.com/maps/eng/DotA v6.68b.w3x', 'DotA V6.68B 英文版'))
	db.session.add(Map('6.68b_cn', 'DotA V6.68b 中文版', 'N', 'DotA v6.68b.w3x', 'http://media.playdota.com/maps/chi/DotA v6.68b.w3x', 'DotA V6.68B 中文版'))
	db.session.add(Map('6.68c_en', 'DotA V6.68C 英文版', 'N', 'DotA v6.68c.w3x', 'http://media.playdota.com/maps/eng/DotA v6.68c.w3x', 'DotA V6.68C 英文版'))
	db.session.add(Map('6.68c_cn', 'DotA V6.68C 中文版', 'N', 'DotA v6.68c.w3x', 'http://media.playdota.com/maps/chi/DotA v6.68c.w3x', 'DotA V6.68C 中文版'))
	db.session.add(Map('6.70c_en', 'DotA V6.70C 英文版', 'N', 'DotA v6.70c.w3x', 'http://media.playdota.com/maps/eng/DotA v6.70c.w3x', 'DotA V6.70C 英文版'))
	db.session.add(Map('6.70c_cn', 'DotA V6.70C 中文版', 'N', 'DotA v6.70c.w3x', 'http://media.playdota.com/maps/chi/DotA v6.70c.w3x', 'DotA V6.70C 中文版'))
	db.session.add(Map('6.71b_en', 'DotA V6.71B 英文版', 'N', 'DotA v6.71b.w3x', 'http://media.playdota.com/maps/eng/DotA v6.71b.w3x', 'DotA V6.71B 英文版'))
	db.session.add(Map('6.71b_cn', 'DotA V6.71B 中文版', 'N', 'DotA v6.71b.w3x', 'http://media.playdota.com/maps/chi/DotA v6.71b.w3x', 'DotA V6.71B 中文版'))


if __name__ == '__main__':
	insert(db)
	db.session.commit()
