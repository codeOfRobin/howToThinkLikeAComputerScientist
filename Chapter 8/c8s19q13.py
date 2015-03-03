import string#unique solution
def count(x,y):
	return y.split(x)
def remove(x,y):
	l1=y.split(x)
	z=""
	a=0
	for subParts in l1:
		if subParts==x:
			l1.remove(a)
			break
		a=a+1
	for subParts in l1:
		z=z+subParts
	return z
print remove("an", "banana")