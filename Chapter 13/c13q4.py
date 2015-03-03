f = open("numberedFriends.txt", "r")
xs = f.readlines()
f.close()

g = open("unumberedFriends.txt", "w")
i=1


for v in xs:
	v=v[5:]
	g.write(v)
	
g.close()