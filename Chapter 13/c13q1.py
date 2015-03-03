f = open("friends.txt", "r")
xs = f.readlines()
f.close()

xs.reverse()

g = open("reverseFriends.txt", "w")
for v in xs:
    g.write(v)
g.close()