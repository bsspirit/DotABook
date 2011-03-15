def filter(a):
	char1 = "unicode('"
	char2 = "')"

	a1=a.find(char1)
	a2=a1+len(char1)

	if a1==-1:
		return a

	b1=a1+a[a1:].find(char2)
	b2=b1+len(char2)
	return filter(a[:a1]+"'"+a[a2:b1]+"'"+a[b2:])


texts=[]
fp = open('insert_hero_skill.py','r')
for line in fp.readlines():
	texts.append(filter(line))

fp.close()


wp = open('write.py','w')
for t in texts:
	wp.write(t)
wp.close()

