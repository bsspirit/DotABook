# -*- coding: utf-8 -*-
from create import db, Item, Item_Skill, Item_Compound

#-----------------------------------------
#Item:vid, name,namecn, picture, price, shop, category, description, info, id=0
db.session.add(Item(1, 'Assault Cuirass', '强袭装甲', '1.jpg', 5500, '保护领地', 'C', '增加10点的护甲,提升35%的攻击速度','', 1))
db.session.add(Item(1, 'Heart of Tarrasque', '魔龙之心', '2.jpg', 5500, '保护领地', 'C', '增加40点的力量，300点的生命,提高2%/秒的被动生命值回复,只能在战场之外为您提供恢复能力（6秒内不能受到来自敌方英雄的攻击）','不可叠加',2))
db.session.add(Item(1, 'Black King Bar', '黑皇杖', '3.jpg', 3900, '保护领地',  'C', '增加10点的力量,增加24点的攻击力','',3))
db.session.add(Item(1, 'Aegis of the Immortal', '不朽盾', '4.jpg', 0, '保护领地',  'A', '英雄死亡后将在3秒后原地复活','得到十分钟后如果未被使用将被回收',4))
db.session.add(Item(1, 'Shiva\'s Guard', '希瓦的守护', '5.jpg', 4700, '保护领地',  'C', '增加30点的智力，增加15点的护甲','',5))
db.session.add(Item(1, 'Bloodstone', '血精石', '6.jpg', 5050, '保护领地',  'C', '增加450点的生命增加400点的魔法提高200%的魔法回复速度提高8点/秒的生命回复速度','',6))
db.session.add(Item(1, 'Linken\'s Sphere', '林肯法球', '7.jpg', 5175, '保护领地',  'C', '增加15点所有属性,提升6点/秒的生命回复速度,提升150%的魔法回复速度','',7))
db.session.add(Item(1, 'Vanguard', '先锋盾', '8.jpg', 2225, '保护领地',  'C', '增加275点的生命，提高6点/秒的生命回复速度，受到普通攻击时有70%的几率抵挡40点的伤害（远程先锋盾：70%抵挡20点伤害）','',8))
db.session.add(Item(1, 'Blade Mail', '刃甲', '9.jpg', 2200, '保护领地',  'C', '增加5点的护甲,增加22点的攻击力,增加10点智力','',9))
db.session.add(Item(1, 'Soul Booster', '振魂石', '10.jpg', 3300, '保护领地',  'C', '增加500点的生命,增加400点的魔法,提高100%的魔法回复速度和4点/秒的生命回复速度','',10))
db.session.add(Item(1, 'Hood of Defiance', '挑战头巾', '11.jpg', 2200, '保护领地', 'C', '提高30%的魔法抗性，提高8点/秒的生命回复速度','',11))
db.session.add(Item(1, 'Guinsoo\'s Scythe of Vyse', 'Guinsoo的邪恶镰刀', '12.jpg', 5675, '秘法圣所', 'C', '增加35点的智力,增加10点的力量,增加10点的敏捷,提高200%的魔法回复速度','',12))
db.session.add(Item(1, 'Orchid Malevolence', '紫怨', '13.jpg', 5025, '秘法圣所',  'C', '增加20点的智力,增加45点的攻击力,提高30%的攻击速度,提高225%的魔法回复速度','',13))
db.session.add(Item(1, 'Eul\'s Scepter of Divinity', 'Eul的神圣法杖', '14.jpg', 2800, '秘法圣所',  'C', '增加10点的智力,提升125%的魔法回复速度,提升25的移动速度','',14))
db.session.add(Item(1, 'Force Staff', '弹射法杖', '15.jpg', 2200, '秘法圣所',  'C', '增加10点攻击力,增加10点智力,提升10%的攻击速度','',15))
db.session.add(Item(1, 'Dagon', 'Dagon之神力', '16.jpg', 2805, '秘法圣所',  'C', '增加3点的所有属性,增加12点的智力,增加9点的攻击力','',16))
db.session.add(Item(1, 'Necronomicon', '死灵书', '17.jpg', 2700, '秘法圣所',  'C', '增加15点的智力，增加6点的力量','',17))
db.session.add(Item(1, 'Aghanim\'s Scepter ', 'Aghanim的神杖', '18.jpg', 4200, '秘法圣所',  'C', '提升10点的所有属性,提高200点生命上限,提高150点魔法上限','',18))
db.session.add(Item(1, 'Refresher Orb', '刷新球', '19.jpg', 5300, '秘法圣所',  'C', '提高5点/秒的生命回复速度，提高200%的魔法回复速度，增加40点的攻击力','',19))
db.session.add(Item(1, 'Mekansm', '梅肯斯姆', '20.jpg', 2306, '支援法衣',  'C', '增加5点的所有属性,增加5点的护甲','',20))
db.session.add(Item(1, 'Vladmir\'s Offering', '吸血鬼祭品', '21.jpg', 2050, '支援法衣',  'C', '','',21))
db.session.add(Item(1, 'Arcane Boots', '秘法鞋', '22.jpg', 1500, '支援法衣',  'C', '增加65点移动速度，增加250魔法值','',22))
db.session.add(Item(1, 'Flying Courier', '飞行信使', '23.jpg', 370, '支援法衣',  'C', '非常好用的飞行运输单位','',23))
db.session.add(Item(1, 'Nathrezim Buckler', '玄冥盾牌', '24.jpg', 803, '支援法衣',  'C', '增加5点的护甲,增加2点的所有属性','',24))
db.session.add(Item(1, 'Ring of Basilius', '圣殿指环', '25.jpg', 500, '支援法衣',  'C', '增加6点的攻击力','',25))
db.session.add(Item(1, 'Khadgar\'s Pipe of Insight', '卡嘉之洞察长笛', '26.jpg', 3653, '支援法衣',  'C', '提升10点每秒的生命回复速度,增加30%的魔抗性','',26))
db.session.add(Item(1, 'Urn of Shadows', '影之灵龛', '27.jpg', 875, '支援法衣',  'C', '增加6点力量,增加50%魔法回复速度','',27))
db.session.add(Item(1, 'Headdress of Rejuvenation', '回复头巾', '28.jpg', 603, '支援法衣',  'C', '增加2点的所有属性','',28))
db.session.add(Item(1, 'Medallion of Courage', '勇气勋章', '29.jpg', 1075, '支援法衣',  'C', '增加6点护甲，增加50%魔法回复速度','',29))
db.session.add(Item(1, 'Ancient Janggo of Endurance', '古之忍耐姜歌', '30.jpg', 1725, '支援法衣',  'C', '增加8点所有属性，增加8点攻击力，增加5%攻击速度和移动速度光环','',30))
db.session.add(Item(1, 'Divine Rapier', '圣剑', '31.jpg', 6200, '远古兵器',  'C', '增加250点的攻击力','',31))
db.session.add(Item(1, 'Monkey King Bar', '金箍棒', '32.jpg', 5400, '远古兵器',  'C', '增加80点的攻击力,提升15%的攻击速度','',32))
db.session.add(Item(1, 'Radiance', '浑耀', '33.jpg', 5150, '远古兵器',  'C', '增加60点的攻击力','',33))
db.session.add(Item(1, 'The Butterfly', '蝴蝶', '34.jpg', 6000, '远古兵器',  'C', '增加30点的敏捷,增加30点的攻击力,提升30%的攻击速度,30%的闪避','',34))
db.session.add(Item(1, 'Buriza-do Kyanon', '大炮', '35.jpg', 5800, '远古兵器',  'C', '增加81点的攻击力','',35))
db.session.add(Item(1, 'Cranium Basher', '碎骨锤', '36.jpg', 3100, '远古兵器',  'C', '增加40点的攻击力,增加3点的力量','',36))
db.session.add(Item(1, 'Battle Fury', '狂战斧', '37.jpg', 4350, '远古兵器',  'C', '增加65点的攻击力,提高150%的魔法回复速度,6点/秒的生命回复速度','',37))
db.session.add(Item(1, 'Manta Style', '幻影斧', '38.jpg', 4950, '远古兵器',  'C', '增加15%攻击速度,提升10点的所有属性,增加16点敏捷,提升10%的移动速度','',38))
db.session.add(Item(1, 'Crystalys', '水晶剑', '39.jpg', 2150, '远古兵器',  'C', '增加35点的攻击力','',39))
db.session.add(Item(1, 'Armlet of Mordiggian', '食尸鬼的臂章', '40.jpg', 2600, '远古兵器',  'C', '增加9点的攻击力,增加5点的护甲,提升15%的攻击速度,提高3点/秒的生命回复速度','',40))
db.session.add(Item(1, 'Lothar\'s Edge', '洛萨之锋', '41.jpg', 3400, '远古兵器',  'C', '增加38点的攻击力,增加10%攻速','',41))
db.session.add(Item(1, 'Ethereal Blade', '虚灵刀', '42.jpg', 5360, '远古兵器',  'C', '增加40点敏捷，增加10点力量,增加10点智力','',42))
db.session.add(Item(1, 'Sange and Yasha', '散华＆夜叉', '43.jpg', 4400, '魅惑遗物',  'C', '增加12点的攻击力,增加16点的力量,增加16点的敏捷,提升12%的移动速度,提升15%的攻击速度','',43))
db.session.add(Item(1, 'Satanic', '撒旦之邪力', '44.jpg', 6150, '魅惑遗物',  'C', '增加25%的吸血。增加25点的力量，5点的护甲','',44))
db.session.add(Item(1, 'Mjollnir', '雷神之锤', '45.jpg', 5500, '魅惑遗物',  'C', '增加20点的攻击力,增加70点攻击速度','',45))
db.session.add(Item(1, 'Eye of Skadi', '斯嘉蒂之眼', '46.jpg', 5900, '魅惑遗物',  'C', '增加25点的所有属性,增加200点的生命,增加150点的魔法','',46))
db.session.add(Item(1, 'Sange', '散华', '47.jpg', 2200, '魅惑遗物',  'C', '增加10点的攻击力，增加16点的力量','',47))
db.session.add(Item(1, 'Helm of the Dominator', '支配头盔', '48.jpg', 1850, '魅惑遗物',  'C', '增加20点的攻击力，5点的护甲,增加15%的吸血','',48))
db.session.add(Item(1, 'Maelstrom', '漩涡', '49.jpg', 3250, '魅惑遗物',  'C', '增加24点的攻击力,提升25%的攻击速度','',49))
db.session.add(Item(1, 'Stygian Desolator', '黯灭刀', '50.jpg', 4400, '魅惑遗物',  'C', '增加60点的攻击力','',50))
db.session.add(Item(1, 'Yasha', '夜叉', '51.jpg', 2200, '魅惑遗物',  'C', '增加16点的敏捷,提升15%的攻击速度,提升10%的移动速度','',51))
db.session.add(Item(1, 'Mask of Madness', '疯狂面具', '52.jpg', 1900, '魅惑遗物',  'C', '增加17%的吸血','',52))
db.session.add(Item(1, 'Diffusal Blade', '散失之刃', '53.jpg', 3300, '魅惑遗物',  'C', '增加22点敏捷,增加10点的智力','',53))
db.session.add(Item(1, 'Boots of Travel', '远行鞋', '54.jpg', 2700, '圣物关口',  'C', '提升95的移动速度','提升效果不能和速度之靴,动力鞋或者其它远行鞋叠加',54))
db.session.add(Item(1, 'Phase Boots', '相位之靴', '55.jpg', 1400, '圣物关口',  'C', '增加70点速度，24点攻击','',55))
db.session.add(Item(1, 'Power Treads', '假腿', '56.jpg', 1450, '圣物关口',  'C', '提升60的移动速度,增加25%的攻击速度,增加10点任意属性(可切换)','提升效果不能和速度之靴，远行鞋或者其他动力鞋叠加',56))
db.session.add(Item(1, 'Soul Ring', '灵魂之戒', '57.jpg', 800, '圣物关口',  'C', '增加3点/秒的生命回复速度，增加50%魔法回复速度','',57))
db.session.add(Item(1, 'Helm of the Dominator', '迈达斯之手', '58.jpg', 1900, '圣物关口',  'C', '提升30%的攻击速度','',58))
db.session.add(Item(1, 'Oblivion Staff', '空明杖', '59.jpg', 1675, '圣物关口',  'C', '增加6点的智力,增加15点的攻击力,提高75%的魔法回复速度,提升10%的攻击速度','',59))
db.session.add(Item(1, 'Perseverance', '坚韧球', '60.jpg', 1750, '圣物关口',  'C', '增加10点的攻击力，提高5点/秒的生命回复速度，提高125%的魔法回复速度','',60))
db.session.add(Item(1, 'Poor Man\'s Shield', '穷鬼盾', '61.jpg', 550, '圣物关口',  'C', '增加6点敏捷','',61))
db.session.add(Item(1, 'Bracer', '护腕', '62.jpg', 525, '圣物关口',  'C', '增加3点的属性,额外增加3点的力量','',62))
db.session.add(Item(1, 'Wraith Band', '幽灵系带', '63.jpg', 485, '圣物关口',  'C', '增加3点的属性,额外增加3点的敏捷','',63))
db.session.add(Item(1, 'Null Talisman', '无用挂件', '64.jpg', 505, '圣物关口',  'C', '增加3点的属性,额外增加3点的智力','',64))
db.session.add(Item(1, 'Magic Wand', '魔杖', '65.jpg', 509, '圣物关口',  'C', '','',65))
db.session.add(Item(1, 'Gloves of Haste', '加速手套', '66.jpg', 500, '奎尔瑟兰的密室', 'A','这双神奇的手套，似乎可以使武器变轻。提升15%的攻击速度','',66))
db.session.add(Item(1, 'Mask of Death', '死亡面具', '67.jpg', 900, '奎尔瑟兰的密室', 'A','再没比这个更拉风的了，增加15%的吸血','法球效果',67))
db.session.add(Item(1, 'Ring of Regeneration', '回复戒指', '68.jpg', 350, '奎尔瑟兰的密室', 'A','这个戒指，在侏儒们的眼里是个幸运符，因为它能提高2点/秒的生命回复速度','',68))
db.session.add(Item(1, 'Kelen\'s Dagger', '逃脱匕首', '69.jpg', 2150, '奎尔瑟兰的密室', 'A','传说中艾泽拉斯大陆上来去如风的刺客科勒所使用的匕首','复仇之魂和屠夫不能使用此物品',69))
db.session.add(Item(1, 'Sobi Mask', '艺人面罩', '70.jpg', 325, '奎尔瑟兰的密室', 'A','法师和术士们用来举办各种仪式的常用面具，提高50%的魔法回复速度','',70))
db.session.add(Item(1, 'Boots of Speed', '速度之靴', '71.jpg', 500, '奎尔瑟兰的密室', 'A','普通跑鞋，提升50的移动速度','提升效果不能和远行鞋，动力鞋或者其它速度之靴叠加',71))
db.session.add(Item(1, 'Gem of True Sight', '真视宝石', '72.jpg', 700, '奎尔瑟兰的密室', 'A','这块水晶带给英雄真视能力，6分钟进货时间','英雄死亡后掉落，不能出售',72))
db.session.add(Item(1, 'Planewalker\'s Cloak', '流浪法师斗篷', '73.jpg', 5500, '奎尔瑟兰的密室', 'A','以魔法材质制作的斗篷可以抵御法术攻击，提高15%的魔法抗性','',73))
db.session.add(Item(1, 'Magic Stick', '魔棒', '74.jpg', 200, '奎尔瑟兰的密室', 'A','','',74))
db.session.add(Item(1, 'Talisman of Evasion', '闪避护符', '75.jpg', 1800, '奎尔瑟兰的密室', 'A','提升25%的闪避','',75))
db.session.add(Item(1, 'Ghost Scepter ', '幽魂权杖', '76.jpg', 1600, '奎尔瑟兰的密室', 'A','增加7点所有属性','',76))
db.session.add(Item(1, 'Clarity Potion', '小净化药水', '77.jpg', 50, '奇迹古树/坟场', 'A','每瓶药水中都困着一个鲜活的小精灵，在30秒内恢复使用者100点的魔法值，受到攻击即失去效果','',77))
db.session.add(Item(1, 'Healing Salve', '瓶装蓝色药水', '78.jpg', 100, '奇迹古树/坟场', 'A','纯净深蓝的药水，在10秒内恢复一个友方单位400点的生命，受到攻击即失去效果','',78))
db.session.add(Item(1, 'Ancient Tango of Essifation', '艾西菲的远古祭祀', '79.jpg', 90, '奇迹古树/坟场', 'A','肉食者转变成素食者时所创的物品，允许使用者吞食树木，在25秒内回复175点的生命。可使用3次','',79))
db.session.add(Item(1, 'Empty Bottle', '空瓶', '80.jpg', 600, '奇迹古树/坟场', 'A','年代久远的魔瓶，或者储存基地的生命泉水供3次使用，每次使用，在3秒内恢复单位135点的生命和70点的魔法；又或者储存一个神符供必要时使用，最多储存120秒，使用神符后魔瓶会回至满','',80))
db.session.add(Item(1, 'Observer Wards', '侦查守卫*2', '81.jpg', 200, '奇迹古树/坟场', 'A','消耗5点魔法放置一个侦察守卫来监视一定的区域，不具有真视能力，持续6分钟，可使用3次','',81))
db.session.add(Item(1, 'Sentry Wards', '岗哨守卫*2', '82.jpg', 200, '奇迹古树/坟场', 'A','放置一个岗哨守卫来监视一定的区域，持续360秒，具有真视能力，可使用2次，真视范围：950','',82))
db.session.add(Item(1, 'Dust of Appearance', '显影之尘', '83.jpg', 190, '奇迹古树/坟场', 'A','真视范围1050，持续12秒，冷却时间60秒，可使用2次，显影效果不叠加，不具有开视野功能，只对英雄有效。','',83))
db.session.add(Item(1, 'Animal Courier', '小鸡', '84.jpg', 170, '奇迹古树/坟场', 'A','制造一个小巧而快速的单位，帮助携带物品，如果它死了，它所携带的物品会掉落','',84))
db.session.add(Item(1, 'Scroll of Town Portal', '回城卷轴', '85.jpg', 135, '奇迹古树/坟场', 'A','将你传送至友方建筑，目标建筑在传送期间无敌','',85))
db.session.add(Item(1, 'Smoke of Deceit', '诡计之雾', '86.jpg', 100, '奇迹古树/坟场', 'A','','',86))
db.session.add(Item(1, 'Gauntlets of Ogre Strength', '食人魔力量手套', '87.jpg', 150, '饰品商人', 'A','指节铜套--豪华版！增加3点的力量','',87))
db.session.add(Item(1, 'Slippers of Agility', '敏捷便鞋', '88.jpg', 150, '饰品商人', 'A','用蜘蛛皮做的皮靴，能使你感到些许刺痛，增加3点的敏捷','',88))
db.session.add(Item(1, 'Mantle of Intelligence', '智力斗篷', '89.jpg', 150, '饰品商人', 'A','穿上去像花花公子的蓝色斗篷；这个季节非常流行，增加3点的智力','',89))
db.session.add(Item(1, 'Ironwood Branch', '铁树枝干', '90.jpg', 53, '饰品商人', 'A','带上它们会确保一场好局，增加1点所有属性','',90))
db.session.add(Item(1, 'Belt of Giant Strength', '巨人力量腰带', '91.jpg', 450, '饰品商人', 'A','这条巨大的腰带是在法师战争中，从倒下的泰坦身上剥下的，能提高携带者6点的力量','',91))
db.session.add(Item(1, 'Boots of Elvenskin', '精灵皮靴', '92.jpg', 450, '饰品商人', 'A','增加6点的敏捷','',92))
db.session.add(Item(1, 'Robe of the Magi', '法师长袍', '93.jpg', 450, '饰品商人', 'A','这件长袍会腐蚀使用者的灵魂，但作为回报，会提高6点的智力','',93))
db.session.add(Item(1, 'Circlet of Nobility', '贵族圆环', '94.jpg', 185, '饰品商人', 'A','为人类公主们所设计的雅致头环，增加2点的所有属性','',94))
db.session.add(Item(1, 'Ogre Axe', '半兽人之斧', '95.jpg', 1000, '饰品商人', 'A','只是握着它就感觉自己变得更加强壮，增加10点力量','',95))
db.session.add(Item(1, 'Blade of Alacrity', '欢欣之刃', '96.jpg', 1000, '饰品商人', 'A','充盈着时光魔法的长剑，增加10点的敏捷','',96))
db.session.add(Item(1, 'Staff of Wizardry', '魔力法杖', '97.jpg', 1000, '饰品商人', 'A','一位堕落法师曾使用过的强力法杖，增加10点的智力','',97))
db.session.add(Item(1, 'Ultimate Orb', '极限法球', '98.jpg', 2100, '饰品商人', 'A','一个包含着生命本质的神秘球体，增加10点的所有属性','',98))
db.session.add(Item(1, 'Blades of Attack', '攻击之爪', '99.jpg', 450, '武器商人', 'A','虐待狂们的可选武器之一，增加9点的攻击力','',99))
db.session.add(Item(1, 'Broadsword', '阔剑', '100.jpg', 1200, '武器商人', 'A','想做个称职的骑士的话，就该买上一把，增加18点的攻击力','',100))
db.session.add(Item(1, 'Quarterstaff', '短棍', '101.jpg', 900, '武器商人', 'A','要4根短棍才能组成一根普通的棍子，增加10点的攻击力，提升10%的攻击速度','',101))
db.session.add(Item(1, 'Claymore', '大剑', '102.jpg', 1400, '武器商人', 'A','一把宝剑，既能够用来砍护甲，也可以用来切土豆，增加21点的攻击力','',102))
db.session.add(Item(1, 'Ring of Protection', '守护指环', '103.jpg', 175, '武器商人', 'A','也许是它尺寸太小的缘故，大多数人想戴上它的话会有点困难，增加2点的护甲','',103))
db.session.add(Item(1, 'Stout Shield', '圆盾', '104.jpg', 250, '武器商人', 'A','受到普通攻击时有60%的概率抵挡20点伤害(远程英雄使用抵挡10点伤害)','',104))
db.session.add(Item(1, 'Javelin', '标枪', '105.jpg', 1500, '武器商人', 'A','与其说是标枪，倒更加像标准的长矛。用来攻击的时候能够穿透敌人的铠甲，增加21点的攻击力，攻击中有20%的几率造成40点的额外伤害','',105))
db.session.add(Item(1, 'Mithril Hammer', '玄铁锤', '106.jpg', 1600, '武器商人', 'A','由纯粹的密银打造而成的锤子，增加24点攻击力','',106))
db.session.add(Item(1, 'Chain Mail', '锁子甲', '107.jpg', 550, '武器商人', 'A','金属锁链制成的编织甲，增加5点的护甲，边路商店可以购买','',107))
db.session.add(Item(1, 'Helm of Iron Will', '铁意头盔', '108.jpg', 950, '武器商人', 'A','一位战死沙场的传奇般的武士使用过的头盔，增加5点的护甲并且提高3点/秒的生命回复速度','',108))
db.session.add(Item(1, 'Plate Mail', '板甲', '109.jpg', 1400, '武器商人', 'A','厚实的板甲能保护整个身体，增加10点的护甲','',109))
db.session.add(Item(1, 'Quelling Blade', '压制之刀', '110.jpg', 225, '武器商人', 'A','','',110))
db.session.add(Item(1, 'Demon Edge', '恶魔刀锋', '111.jpg', 2400, '黑市商人', 'A','恶魔军团的堕落统领所使用的武器，充满着邪恶的力量，增加46点的攻击力','',111))
db.session.add(Item(1, 'Eaglehorn', '鹰角弓', '112.jpg', 3300, '黑市商人', 'A','用这把轻巧的弓进行攻击是如此的精准，就好像它自己会瞄准目标一样，增加25点的敏捷','',112))
db.session.add(Item(1, 'Messerschmidt\'s Reaver', '希梅斯特的掠夺', '113.jpg', 3200, '黑市商人', 'A','这把巨斧能够劈开一整条山脉，增加25点的力量','',113))
db.session.add(Item(1, 'Sacred Relic', '圣者遗物', '114.jpg', 3800, '黑市商人', 'A','自远古就存在的强大的武器，你很难说清圣者遗物到底是什么，一般认为这是一柄剑。增加60点的攻击力','',114))
db.session.add(Item(1, 'Hyperstone', '振奋宝石', '115.jpg', 2100, '黑市商人', 'A','一块刻有神秘纹路的石头，能够提高携带者的激情，提升55%的攻击速度','',115))
db.session.add(Item(1, 'Ring of Health', '治疗指环', '116.jpg', 875, '黑市商人', 'A','在一个半身人肥仔的尸体上找到的闪闪发光的戒指，提高5点/秒的生命回复速度','',116))
db.session.add(Item(1, 'Void Stone', '虚无宝石', '117.jpg', 875, '黑市商人', 'A','这块宝石看起来蕴藏着无穷的能量，提高100%的魔法回复速度','',117))
db.session.add(Item(1, 'Aghanim\'s Scepter', '神秘法杖', '118.jpg', 2700, '黑市商人', 'A','这根谜一般的法杖是由最贵重的水晶做成的，增加25点的智力','',118))
db.session.add(Item(1, 'Energy Booster', '能量之球', '119.jpg', 1000, '黑市商人', 'A','这件精致的艺术品据说是由纯粹的能量构成的，增加250点的魔法','',119))
db.session.add(Item(1, 'Point Booster', '精气之球', '120.jpg', 1200, '黑市商人', 'A','这颗神秘的宝石能够全面发掘英雄的潜能，增加150点魔法和200点生命','',120))
db.session.add(Item(1, 'Vitality Booster', '活力之球', '121.jpg', 1100, '黑市商人', 'A','据说，它能带给神选之人以不朽，至于别人嘛，它增加250点的生命','',121))
db.session.add(Item(1, 'Orb of Venom', '淬毒之珠', '122.jpg', 500, '黑市商人', 'A','毒性攻击3点/秒的持续性伤害，持续3秒，远程英雄使用减速4%，近战英雄使用减速12%','法球效果',122))



#------------------------------------------------------

db.session.add(Item(1, 'Assault Cuirass Reel', '强袭装甲合成书', '1.jpg', 1500, '保护领地', 'R', '强袭装甲合成书','',123))
db.session.add(Item(1, 'Heart of Tarrasque Reel', '魔龙之心合成书', '2.jpg', 1200, '保护领地', 'R','魔龙之心合成书','',124))
db.session.add(Item(1, 'Black King Bar Reel', '黑皇杖合成书', '3.jpg', 1300, '保护领地', 'R','黑皇杖合成书','',125))
db.session.add(Item(1, 'Shiva\'s Guard Reel', '希瓦的守护合成书', '5.jpg', 600, '保护领地', 'R','希瓦的守护合成书','',126))
db.session.add(Item(1, 'Linken\'s Sphere Reel', '林肯法球合成书', '7.jpg', 1325, '保护领地', 'R','林肯法球合成书','',127))
db.session.add(Item(1, 'Boots of Travel', 'Eul的神圣法杖合成书', '14.jpg', 600, '秘法圣所', 'R','Eul的神圣法杖合成书','',128))
db.session.add(Item(1, 'Force Staff Reel', '弹射法杖合成书', '15.jpg', 300, '秘法圣所', 'R','弹射法杖合成书','',129))
db.session.add(Item(1, 'Dagon Reel', 'Dagon之神力合成书', '16.jpg', 1300, '秘法圣所', 'R','Dagon之神力合成书','',130))
db.session.add(Item(1, 'Necronomicon Reel', '死灵书合成书', '17.jpg', 1250, '秘法圣所', 'R','死灵书合成书','',131))
db.session.add(Item(1, 'Refresher Orb Reel', '刷新球合成书', '19.jpg', 1875, '秘法圣所', 'R','刷新球合成书','',132))
db.session.add(Item(1, 'Mekansm Reel', '梅肯斯姆合成书', '20.jpg', 900, '支援法衣', 'R','梅肯斯姆合成书','',133))
db.session.add(Item(1, 'Vladmir\'s Offering Reel', '吸血鬼祭品合成书', '21.jpg', 300, '支援法衣', 'R','吸血鬼祭品合成书','',134))
db.session.add(Item(1, 'Flying Courier Reel', '飞行信使合成书', '23.jpg', 200, '支援法衣', 'R','飞行信使合成书','',135))
db.session.add(Item(1, 'Nathrezim Buckler Reel', '玄冥盾牌合成书', '24.jpg', 200, '支援法衣', 'R','玄冥盾牌合成书','',136))
db.session.add(Item(1, 'Boots of Travel', '卡嘉之洞察长笛合成书', '26.jpg', 900, '支援法衣', 'R','卡嘉之洞察长笛合成书','',137))
db.session.add(Item(1, 'Urn of Shadows Reel', '影之灵龛合成书', '27.jpg', 250, '支援法衣', 'R','影之灵龛合成书','',138))
db.session.add(Item(1, 'Headdress of Rejuvenation Reel', '回复头巾合成书', '28.jpg', 200, '支援法衣', 'R','回复头巾合成书','',139))
db.session.add(Item(1, 'Medallion of Courage Reel', '勇气勋章合成书', '29.jpg', 200, '支援法衣', 'R','勇气勋章合成书','',140))
db.session.add(Item(1, 'Boots of Travel', '古之忍耐姜歌合成书', '30.jpg', 750, '支援法衣', 'R','古之忍耐姜歌合成书','',141))
db.session.add(Item(1, 'Boots of Travel', '辉耀合成书', '33.jpg', 1350, '远古兵器', 'R','辉耀合成书','',142))
db.session.add(Item(1, 'Boots of Travel', '大炮合成书', '35.jpg', 1200, '远古兵器', 'R','大炮合成书','',143))
db.session.add(Item(1, 'Boots of Travel', '碎骨锤合成书', '36.jpg', 1150, '远古兵器', 'R','碎骨锤合成书','',144))
db.session.add(Item(1, 'Boots of Travel', '幻影斧合成书', '38.jpg', 600, '远古兵器', 'R','幻影斧合成书','',145))
db.session.add(Item(1, 'Crystalys Reel', '水晶剑合成书', '39.jpg', 1800, '远古兵器', 'R','蝴蝶合成书','',146))
db.session.add(Item(1, 'Boots of Travel', '食尸鬼的臂章合成书', '40.jpg', 700, '远古兵器', 'R','食尸鬼的臂章合成书','',147))
db.session.add(Item(1, 'Boots of Travel', '洛萨之锋合成书', '41.jpg', 1100, '远古兵器', 'R','洛萨之锋合成书','',148))
db.session.add(Item(1, 'Satanic Reel', '撒旦之邪力合成书', '44.jpg', 1100, '魅惑遗物', 'R','撒旦之邪力合成书','',149))
db.session.add(Item(1, 'Boots of Travel', '雷神之锤合成书', '45.jpg', 400, '魅惑遗物', 'R','雷神之锤合成书','',150))
db.session.add(Item(1, 'Sange Reel', '散华合成书', '47.jpg', 750, '魅惑遗物', 'R','散华合成书','',151))
db.session.add(Item(1, 'Maelstrom Reel', '漩涡合成书', '49.jpg', 900, '魅惑遗物', 'R','漩涡合成书','',152))
db.session.add(Item(1, 'Boots of Travel', '黯灭刀合成书', '50.jpg', 1200, '魅惑遗物', 'R','黯灭刀合成书','',153))
db.session.add(Item(1, 'Yasha Reel', '夜叉合成书', '51.jpg', 750, '魅惑遗物', 'R','夜叉合成书','',154))
db.session.add(Item(1, 'Mask of Madness Reel', '疯狂面具合成书', '52.jpg', 1000, '魅惑遗物', 'R','疯狂面具合成书','',155))
db.session.add(Item(1, 'Diffusal Blade Reel', '散失之刃合成书', '53.jpg', 850, '魅惑遗物', 'R','散失之刃合成书','',156))
db.session.add(Item(1, 'Boots of Travel Reel', '远行鞋合成书', '54.jpg', 2200, '圣物关口', 'R','远行鞋合成书','',157))
db.session.add(Item(1, 'Soul Ring Reel', '灵魂之戒合成书', '57.jpg', 125, '圣物关口', 'R','灵魂之戒合成书','',158))
db.session.add(Item(1, 'Boots of Travel', '迈达斯之手合成书', '58.jpg', 1400, '圣物关口', 'R','迈达斯之手合成书','',159))
db.session.add(Item(1, 'Bracer Reel', '护腕合成书', '62.jpg', 190, '圣物关口', 'R','护腕合成书','',160))
db.session.add(Item(1, 'Wraith Band Reel', '幽灵系带合成书', '63.jpg', 150, '圣物关口', 'R','幽灵系带合成书','',161))
db.session.add(Item(1, 'Null Talisman Reel', '无用挂件合成书', '64.jpg', 170, '圣物关口', 'R','无用挂件合成书','',162))
db.session.add(Item(1, 'Magic Wand', '魔杖合成书', '65.jpg', 150, '圣物关口', 'R','魔杖合成书','',163))

#Item_Compound:iid1,iid2
db.session.add(Item_Compound(1,107))
db.session.add(Item_Compound(1,109))
db.session.add(Item_Compound(1,115))
db.session.add(Item_Compound(1,123))
db.session.add(Item_Compound(2,113))
db.session.add(Item_Compound(2,121))
db.session.add(Item_Compound(2,124))
db.session.add(Item_Compound(3,95))
db.session.add(Item_Compound(3,106))
db.session.add(Item_Compound(3,125))
db.session.add(Item_Compound(5,109))
db.session.add(Item_Compound(5,118))
db.session.add(Item_Compound(5,126))
db.session.add(Item_Compound(6,10))
db.session.add(Item_Compound(6,60))
db.session.add(Item_Compound(7,98))
db.session.add(Item_Compound(7,60))
db.session.add(Item_Compound(7,127))
db.session.add(Item_Compound(8,104))
db.session.add(Item_Compound(8,116))
db.session.add(Item_Compound(8,121))
db.session.add(Item_Compound(9,93))
db.session.add(Item_Compound(9,100))
db.session.add(Item_Compound(9,107))
db.session.add(Item_Compound(10,119))
db.session.add(Item_Compound(10,120))
db.session.add(Item_Compound(10,121))
db.session.add(Item_Compound(11,68))
db.session.add(Item_Compound(11,68))
db.session.add(Item_Compound(11,73))
db.session.add(Item_Compound(11,116))

db.session.add(Item_Compound(12,98))
db.session.add(Item_Compound(12,117))
db.session.add(Item_Compound(12,118))
db.session.add(Item_Compound(13,59))
db.session.add(Item_Compound(13,59))
db.session.add(Item_Compound(13,59))
db.session.add(Item_Compound(14,70))
db.session.add(Item_Compound(14,97))
db.session.add(Item_Compound(14,117))
db.session.add(Item_Compound(14,128))
db.session.add(Item_Compound(15,97))
db.session.add(Item_Compound(15,101))
db.session.add(Item_Compound(15,129))
db.session.add(Item_Compound(16,64))
db.session.add(Item_Compound(16,97))
db.session.add(Item_Compound(16,130))
db.session.add(Item_Compound(17,91))
db.session.add(Item_Compound(17,97))
db.session.add(Item_Compound(17,131))
db.session.add(Item_Compound(18,95))
db.session.add(Item_Compound(18,96))
db.session.add(Item_Compound(18,97))
db.session.add(Item_Compound(18,120))
db.session.add(Item_Compound(19,59))
db.session.add(Item_Compound(19,60))
db.session.add(Item_Compound(19,132))

db.session.add(Item_Compound(20,24))
db.session.add(Item_Compound(20,28))
db.session.add(Item_Compound(20,133))
db.session.add(Item_Compound(21,25))
db.session.add(Item_Compound(21,67))
db.session.add(Item_Compound(21,68))
db.session.add(Item_Compound(21,134))
db.session.add(Item_Compound(22,71))
db.session.add(Item_Compound(22,119))
db.session.add(Item_Compound(23,84))
db.session.add(Item_Compound(23,135))
db.session.add(Item_Compound(24,90))
db.session.add(Item_Compound(24,107))
db.session.add(Item_Compound(24,136))
db.session.add(Item_Compound(25,70))
db.session.add(Item_Compound(25,103))
db.session.add(Item_Compound(26,11))
db.session.add(Item_Compound(26,28))
db.session.add(Item_Compound(26,137))
db.session.add(Item_Compound(27,70))
db.session.add(Item_Compound(27,87))
db.session.add(Item_Compound(27,87))
db.session.add(Item_Compound(27,138))
db.session.add(Item_Compound(28,68))
db.session.add(Item_Compound(28,90))
db.session.add(Item_Compound(28,139))
db.session.add(Item_Compound(29,70))
db.session.add(Item_Compound(29,107))
db.session.add(Item_Compound(29,140))
db.session.add(Item_Compound(30,62))
db.session.add(Item_Compound(30,93))
db.session.add(Item_Compound(30,141))

db.session.add(Item_Compound(31,111))
db.session.add(Item_Compound(31,114))
db.session.add(Item_Compound(32,105))
db.session.add(Item_Compound(32,105))
db.session.add(Item_Compound(32,111))
db.session.add(Item_Compound(33,114))
db.session.add(Item_Compound(33,142))
db.session.add(Item_Compound(34,75))
db.session.add(Item_Compound(34,101))
db.session.add(Item_Compound(34,112))
db.session.add(Item_Compound(35,39))
db.session.add(Item_Compound(35,111))
db.session.add(Item_Compound(35,143))
db.session.add(Item_Compound(36,91))
db.session.add(Item_Compound(36,105))
db.session.add(Item_Compound(36,144))
db.session.add(Item_Compound(37,60))
db.session.add(Item_Compound(37,100))
db.session.add(Item_Compound(37,102))
db.session.add(Item_Compound(38,51))
db.session.add(Item_Compound(38,98))
db.session.add(Item_Compound(38,145))
db.session.add(Item_Compound(39,99))
db.session.add(Item_Compound(39,100))
db.session.add(Item_Compound(39,146))
db.session.add(Item_Compound(40,66))
db.session.add(Item_Compound(40,99))
db.session.add(Item_Compound(40,108))
db.session.add(Item_Compound(40,147))
db.session.add(Item_Compound(41,101))
db.session.add(Item_Compound(41,102))
db.session.add(Item_Compound(41,148))
db.session.add(Item_Compound(42,76))
db.session.add(Item_Compound(42,112))

db.session.add(Item_Compound(43,47))
db.session.add(Item_Compound(43,51))
db.session.add(Item_Compound(44,48))
db.session.add(Item_Compound(44,113))
db.session.add(Item_Compound(44,149))
db.session.add(Item_Compound(45,49))
db.session.add(Item_Compound(45,115))
db.session.add(Item_Compound(45,150))
db.session.add(Item_Compound(46,98))
db.session.add(Item_Compound(46,98))
db.session.add(Item_Compound(46,120))
db.session.add(Item_Compound(46,122))
db.session.add(Item_Compound(47,91))
db.session.add(Item_Compound(47,95))
db.session.add(Item_Compound(47,151))
db.session.add(Item_Compound(48,67))
db.session.add(Item_Compound(48,108))
db.session.add(Item_Compound(49,66))
db.session.add(Item_Compound(49,106))
db.session.add(Item_Compound(49,152))
db.session.add(Item_Compound(50,106))
db.session.add(Item_Compound(50,106))
db.session.add(Item_Compound(50,153))
db.session.add(Item_Compound(51,92))
db.session.add(Item_Compound(51,96))
db.session.add(Item_Compound(51,154))
db.session.add(Item_Compound(52,67))
db.session.add(Item_Compound(52,155))
db.session.add(Item_Compound(53,93))
db.session.add(Item_Compound(53,96))
db.session.add(Item_Compound(53,96))
db.session.add(Item_Compound(53,156))

db.session.add(Item_Compound(54,71))
db.session.add(Item_Compound(54,157))
db.session.add(Item_Compound(55,71))
db.session.add(Item_Compound(55,99))
db.session.add(Item_Compound(55,99))
db.session.add(Item_Compound(56,66))
db.session.add(Item_Compound(56,71))
db.session.add(Item_Compound(56,91))
db.session.add(Item_Compound(56,92))
db.session.add(Item_Compound(56,93))
db.session.add(Item_Compound(57,68))
db.session.add(Item_Compound(57,70))
db.session.add(Item_Compound(57,158))
db.session.add(Item_Compound(58,66))
db.session.add(Item_Compound(58,159))
db.session.add(Item_Compound(59,70))
db.session.add(Item_Compound(59,93))
db.session.add(Item_Compound(59,101))
db.session.add(Item_Compound(60,116))
db.session.add(Item_Compound(60,117))
db.session.add(Item_Compound(61,88))
db.session.add(Item_Compound(61,88))
db.session.add(Item_Compound(61,104))
db.session.add(Item_Compound(62,87))
db.session.add(Item_Compound(62,94))
db.session.add(Item_Compound(62,160))
db.session.add(Item_Compound(63,88))
db.session.add(Item_Compound(63,94))
db.session.add(Item_Compound(63,161))
db.session.add(Item_Compound(64,89))
db.session.add(Item_Compound(64,94))
db.session.add(Item_Compound(64,162))
db.session.add(Item_Compound(65,74))
db.session.add(Item_Compound(65,90))
db.session.add(Item_Compound(65,90))
db.session.add(Item_Compound(65,90))
db.session.add(Item_Compound(65,163))




#Item_Skill:iid, name, namecn, ability, mana_cost, cooldown, casting_range, area, duration, description,note
db.session.add(Item_Skill(1,'','专注光环','P', 0, 0, 0, 900, 'N','增加友方单位5点护甲',''))
db.session.add(Item_Skill(1,'','荒芜光环','P', 0, 0, 0, 900, 'N','减少非友方单位5点护甲',''))
db.session.add(Item_Skill(1,'','狂热光环','P', 0, 0, 0, 900, 'N','增加20％友方单位攻击速度',''))
db.session.add(Item_Skill(3,'','天神下凡','A', 0, 80, 0, 0, 'N','10/9/8/7/6/5秒的天神下凡（对魔法免疫）,80/75/70/65/60/55秒冷却时间',''))
db.session.add(Item_Skill(4,'','重生','P', 0, 0, 0, 0, '3s','英雄死亡后将在3秒后原地复活','得到十分钟后如果未被使用将被回收'))
db.session.add(Item_Skill(5,'','霜冷光环','P', 0, 0, 0, 1000, 'N','减少25%的攻击速度',''))
db.session.add(Item_Skill(5,'','极寒冲击','A', 100, 30, 0, 1000, '4s','范围内非友军单位受到200伤害并减少40%的移动速度',''))
db.session.add(Item_Skill(6,'','血焰灌输','P', 0, 0, 0, 1000, 'N','1000范围内有敌方英雄死亡时获得1点能量，死亡后失去1/3的能量，每点能量+1点/秒的魔法恢复速度，且充能可为神圣救赎提供更强大的效果（充能恢复效果不与按照百分比的魔法恢复速度挂钩）',''))
db.session.add(Item_Skill(6,'','救赎','P', 0, 0, 0, 1700, 'N','有能量时死亡：1700范围内的友方单位将恢复450+(30*血精石能量点)的生命值，自己死亡时金钱损失减少(25*血精石能量点)，复活时间减少(3*血精石能量点),得到死亡前所处范围内的经验',''))
db.session.add(Item_Skill(7,'','法术否定','P', 0, 0, 0, 0, '20s','每20秒抵挡一次指向性法术攻击',''))
db.session.add(Item_Skill(9,'','尖刺','A', 25, 22, 0, 0, '4s','将所受伤害100%反弹给攻击者(反弹属于神圣伤害，刃甲不再反弹来源为刃甲的伤害)',''))
db.session.add(Item_Skill(12,'','妖术','A', 100, 35, 700, 0, '3.5s','将目标变成一只绵羊，期间只能保留部分被动技能效果且不能攻击、只有缓慢的移动速度',''))
db.session.add(Item_Skill(13,'','灵魂燃烧','A', 100, 18, 700, 0, '5s','沉默目标，并额外受到20%的伤害',''))
db.session.add(Item_Skill(14,'','龙卷风','A', 25, 30, 700, 0, '2.5s','龙卷风 (造成对方停留在空中),可对自己使用',''))
db.session.add(Item_Skill(15,'','弹射','A', 25, 45, 800, 0, '20s','将一个单位向其面对的方向推进600距离','双击弹射法杖相当于对自己使用弹射'))
db.session.add(Item_Skill(16,'','能量冲击','A', 180, 40, 0, 600, 'N','增加3点所有属性，增加9点攻击，增加12/14/16/18/20智力，消耗180/160/140/120/100点的魔法，冷却时间40/36/32/28/24秒，造成400/500/600/700/800点的能量冲击伤害， 施法距离 600/650/700/750/800',' 可以通过购买卷轴升级; 最多能升级4次'))
db.session.add(Item_Skill(17,'','召唤死灵','A', 50, 90, 0, 0, 'N','增加8/12/16点的力量，增加15/21/24点的智力',''))
db.session.add(Item_Skill(17,'','复活死灵','A', 0, 0, 0, 0, '35s','召唤拥有特殊能力的 1 个恶魔战士 (400/600/800 的生命值，21/41/61 的普通攻击力，6/8/10 点的护甲，40%的魔法伤害减免，25/50/75 点/攻击的法力损毁 (同时减少60% 魔法损毁的生命值) ，对杀死它的单位造成200/400/600 点伤害的最后遗愿，第三级时拥有魔法岗哨 (视野 1000，具有真视能力))和1个恶魔射手 (400/600/800 的生命值，31/61/91 的穿刺攻击力，350/450/550 的攻击射程，6/8/10 点的护甲，40%的魔法伤害减免，+3%/6%/9% 攻击和移动速度的耐久光环 (400 有效范围) ，200/250/300 点的法力燃烧 (同时造成等量伤害，施法距离 250) ) 为你战斗(同一时间每人只能召唤一组','可以通过购买卷轴升级,最多能升2次'))
db.session.add(Item_Skill(18,'','奥义提升','P', 0, 0, 0, 0, '5s','提升某些英雄大招的威力',''))
db.session.add(Item_Skill(19,'','刷新','A', 375, 210, 0, 0, 'N','立刻 结束所有物品/技能的冷却进程 (不包括刷新球本身)',''))
db.session.add(Item_Skill(20,'','回复光环','P', 0, 0, 0, 500, 'N','增加4点/秒的生命回复速度',''))
db.session.add(Item_Skill(20,'','活力','A', 150, 45, 0, 750, '20s','周围友方单位恢复250点的生命，增加2点的护甲',''))
db.session.add(Item_Skill(21,'','攻击光环','P', 0, 0, 0, 900, 'N','增加15%的攻击力',''))
db.session.add(Item_Skill(21,'','吸血光环','P', 0, 0, 0, 900, 'N','增加16%吸血(仅近战攻击有效',''))
db.session.add(Item_Skill(21,'','辉煌光环','P', 0, 0, 0, 900, 'N','增加魔法回复0.8点/秒',''))
db.session.add(Item_Skill(21,'','专注光环','P', 0, 0, 0, 900, 'N','增加5点护甲',''))
db.session.add(Item_Skill(22,'','恢复魔法','A', 25, 45, 0, 600, 'N','为600范围的友军恢复135点魔法',''))
db.session.add(Item_Skill(24,'','防御提升','A', 50, 15, 0, 700, '15s','提升周围友方单位2点的护甲',''))
db.session.add(Item_Skill(25,'','专注光环','P', 0, 0, 0, 900, 'N','增加3点护甲',''))
db.session.add(Item_Skill(25,'','辉煌光环','P', 0, 0, 0, 900, 'N','增加0.65点／秒魔法回复速度',''))
db.session.add(Item_Skill(26,'','魔法屏障','A', 0, 60, 0, 700, '8s','神奇的人造品 能召唤能量立场保护附近的友军使他们可以抵挡400点法术伤害','50秒内不能叠加'))
db.session.add(Item_Skill(27,'','灵魂释放','A', 0, 10, 950, 0, 'N','释放一个储存的灵魂，在接下来的8秒内，回复/伤害一个友方/敌方英雄单位400/200点生命,附近1400范围内有敌方英雄死亡时自动充能，受到来自玩家的攻击驱散回复效果。每个英雄死亡只能给1个影之灵龛充能',''))
db.session.add(Item_Skill(28,'','回复光环','P', 0, 0, 0, 500, 'N','增加3点／秒生命回复速度',''))
db.session.add(Item_Skill(29,'','孤注一掷','P', 0, 7, 800, 0, '7s','指向敌人施法你和被施法单位同时降低6点护甲',''))
db.session.add(Item_Skill(30,'','战鼓','A', 0, 30, 800, 0, '6s','使用时为附近单位提供额外10%攻击速度，移动速度BUFF',''))
db.session.add(Item_Skill(32,'','精确打击','P', 0, 0, 0, 0, 'N','攻击不会落空（该技能与其它一些技能有冲突，点击可以切换开关状态）',''))
db.session.add(Item_Skill(32,'','猛击','P', 0, 0, 0, 0, 'N','在攻击中有35% 的几率造成0.01秒的眩晕，+100点的附加伤害',''))
db.session.add(Item_Skill(33,'','辉耀','P', 0, 0, 0, 650, 'N','献祭造成40点伤害/秒，对远古单位无效果',''))
db.session.add(Item_Skill(35,'','致命一击','P', 0, 0, 0, 0, 'N','20%的几率, 2.4倍伤害',''))
db.session.add(Item_Skill(36,'','重击','P', 0, 0, 0, 0, 'N','近身攻击有25% 的几率造成1.4秒的眩晕，远程攻击有10% 的几率造成1.4秒的眩晕，2秒不与任何被动击晕技能叠加',''))
db.session.add(Item_Skill(37,'','溅射攻击','P', 0, 0, 0, 200, 'N','135%的伤害，200 有效范围，仅近身单位使用时有效',''))
db.session.add(Item_Skill(38,'','幻影','A', 0, 50, 0, 0, '20s','制造两个幻影,拥有本体33%的攻击力,承受350%的伤害',''))
db.session.add(Item_Skill(39,'','致命一击','P', 0, 0, 0, 0, 'N','15%的几率, 1.75倍伤害',''))
db.session.add(Item_Skill(41,'','疾风步','A', 50, 18, 0, 0, '9s','使用者进入疾风步状态，期间增加其20%的移动和速度，显身一击附加125点伤害',''))
db.session.add(Item_Skill(42,'','以太冲击','A', 50, 18, 0, 0, '3s','对一个敌方英雄使用，使用者和目标同时进入虚无状态,目标受到75+2*使用者敏捷的魔法伤害（法术攻击·魔法伤害），且移动速度降低30%','与幽魂权杖共用冷却。可以对自己使用（无伤害，不减速）'))
db.session.add(Item_Skill(43,'','残废','P', 0, 0, 0, 0, '4s','攻击有15%的概率使目标残废',''))
db.session.add(Item_Skill(40,'','邪恶之力','A', 0, 0, 0, 0, '5s','增加40点攻击力，增加25%的攻击速度，增加5点护甲，减少35生命/秒的恢复速度，力量增加25点（生命上限+475）',''))
db.session.add(Item_Skill(44,'','不洁狂热','A', 0, 35, 0, 0, '3.5s','增加30点攻击力，额外增加175%吸血',''))
db.session.add(Item_Skill(45,'','连环闪电','P', 0, 0, 0, 0, 'N','攻击中有20%几率释放出跳跃4次,160点伤害的连环闪电,不衰减',''))
db.session.add(Item_Skill(45,'','静电冲击','A', 0, 35, 0, 0, '20s','受到攻击时有20%几率对攻击者及附近最多3个单位释放200点伤害的叉状闪电',''))
db.session.add(Item_Skill(46,'','霜冻攻击','P', 0, 0, 0, 0, '2s','减少20%的攻击速度，减少30%的移动速度',''))
db.session.add(Item_Skill(47,'','残废','P', 0, 0, 0, 0, '4s','在攻击中有15%的概率使目标残废',''))
db.session.add(Item_Skill(48,'','支配','A', 200, 300, 700, 0, 'N','长时间控制一个非英雄单位，并能获得英雄单位的魔法抗性,最高级别 6',''))
db.session.add(Item_Skill(49,'','连锁闪电','P', 0, 0, 0, 0, 'N','在攻击中有25%的概率放出能跳跃4次的连环闪电，造成120点伤害，不衰减','法球效果不可叠加'))
db.session.add(Item_Skill(50,'','腐蚀攻击','P', 0, 0, 0, 0, '5s','法球效果: 降低对方6点的护甲',''))
db.session.add(Item_Skill(52,'','狂热','A', 25, 25, 0, 0, '12s','增加100%的攻击速度，增加20%的移动速度，增加30%所受伤害将即时计算',''))
db.session.add(Item_Skill(53,'','反馈','P', 0, 0, 0, 0, 'N','每次攻击燃烧目标20点魔法,同时造成等量的伤害',''))
db.session.add(Item_Skill(53,'','净化','A', 75, 12, 600, 0, '3s','削除目标身上的魔法效果,将敌方单位的移动速度降低至1/5,持续4(15)秒直接消灭召唤生物','法球效果不可叠加,购买合成书可升级,最高2级.'))
db.session.add(Item_Skill(54,'','传送','A', 75, 60, 0, 0, '3s','传送至友方的一个建筑或非英雄单位',''))
db.session.add(Item_Skill(55,'','相位','A', 75, 60, 0, 0, '3s','增加16%的移动速度，碰撞体积为0（可以穿人，但不能无视地形），攻击或使用技能后buff消失',''))
db.session.add(Item_Skill(57,'','牺牲','A', 0, 30, 600, 0, '10s','使用者瞬间牺牲150点生命，来为自己提供150点额外魔法，但额外魔法只持续10秒，持续时间内任何魔法需求都会优先从牺牲获得 的额外魔法中取的',''))
db.session.add(Item_Skill(58,'','炼制','A', 25, 100, 600, 0, 'N','最高可将6级非远古野怪转化为金钱',''))
db.session.add(Item_Skill(61,'','伤害抵挡','P', 0, 0, 0, 0, 'N','受到普通攻击抵挡20点英雄造成的伤害(远程英雄使用抵挡10点英雄造成的伤害),同时有60%的概率抵挡20点非英雄造成的伤害',''))
db.session.add(Item_Skill(65,'','充能','A', 0, 0, 0, 1500, '17s','使用后为你补充生命和魔法（补充效果取决于能量点数，每个能量点补充15点生命与魔法）；附近1500范围有敌方英雄单位施展技能时会自动充能（上限15次）',''))
db.session.add(Item_Skill(69,'','瞬间移动','A', 75, 14, 1200, 0, 'N','只有在3秒内没有受到英雄伤害时才能使用',''))
db.session.add(Item_Skill(74,'','充能','A', 25, 17, 600, 1500, 'N','使用后为你补充生命和魔法（补充效果取决于能量点数，每个能量点补充15点生命与魔法）,附近1500范围有敌方英雄单位施展技能时会自动充能','上限10次'))
db.session.add(Item_Skill(76,'','幽魂形态','A', 75, 25, 1200, 0, '4s','你将进入灵魂形态4秒 会受到44%的额外魔法伤害,但是对物理攻击免疫',''))
db.session.add(Item_Skill(85,'','传送','A', 75, 65, 0, 0, '3s','将你传送至任意友方建筑','双击回城卷轴会自动将你传送至泉水区域'))

db.session.add(Item_Skill(110,'','压制','P', 0, 0, 0, 0, 'N','远程英雄使用对非英雄单位额外造成12%的伤害,近程英雄使用对非英雄单位额外造成32%的伤害',''))
db.session.add(Item_Skill(110,'','砍树','A', 0, 5, 0, 0, 'N','砍掉一棵树','船长不可以使用'))

#-----------------------------------------

db.session.commit()
