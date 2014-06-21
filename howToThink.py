import string#unique solution
def count(x,y):
	return y.split(x)
def remove(x,y):
	l1=y.split(x)
	z=""
	x=0
	for subParts in l1:
		if subParts!=x:
			z=z+subParts

	return z

def something((x,y)):
	print x

something((8,9))