import string#unique solution
def count(x,y):
	return len(y.split(x))-1

print count("an", "banana")
