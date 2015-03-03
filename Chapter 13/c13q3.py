f = open("friends.txt", "r")
xs = f.readlines()
f.close()

g = open("numberedFriends.txt", "w")
i=1


for v in xs:
	g.write('{0:4d} '.format(i))
	g.write(v)
	i+=1
g.close()