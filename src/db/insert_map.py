# -*- coding: utf-8 -*-
from create import db, Map

#-----------------------------------------
#Map:version, namecn, category, filename, desc
db.session.add(Map('6.67b', 'DotA V6.67B 中文版', 'N', 'DotA Allstars v6.67b.w3x', 'DotA V6.67B 中文版'))
db.session.add(Map('6.67c', 'DotA V6.67C 中文版', 'N', 'DotA Allstars v6.67c.w3x', 'DotA V6.67C 中文版'))
db.session.add(Map('6.68b', 'DotA V6.68B 中文版', 'N', 'DotA v6.68b.w3x', 'DotA V6.68B 中文版'))
db.session.add(Map('6.68c', 'DotA V6.68C 中文版', 'N', 'DotA v6.68c.w3x', 'DotA V6.68C 中文版'))
db.session.add(Map('6.70c', 'DotA V6.70C 中文版', 'N', 'DotA v6.70c.w3x', 'DotA V6.70C 中文版'))
db.session.add(Map('6.71b', 'DotA V6.71B 中文版', 'N', 'DotA v6.71b.w3x', 'DotA V6.71B 中文版'))

#------------------------------------------
db.session.commit()
