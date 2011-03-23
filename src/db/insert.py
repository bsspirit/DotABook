# -*- coding: utf-8 -*-
from create import db
from insert_version import insert as version
from insert_map import insert as map
from insert_item import insert as item
from insert_hero import insert as hero
from insert_hero_skill import insert as hero_skill
from insert_hero_skill_level import insert as hero_skill_level
from insert_config import insert as config


if __name__ == '__main__':
	version(db)
	hero(db)
	hero_skill(db)
	hero_skill_level(db)
	item(db)
	map(db)
	config(db)
	db.session.commit()

