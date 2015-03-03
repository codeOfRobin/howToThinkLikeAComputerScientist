f = open("friends.txt", "r")
xs = f.readlines()
f.close()


g = open("snakeFriends.txt", "w")
for v in xs:
	if v.find("snake")!=-1:
		g.write(v)
g.close()