def countLetter(a,x):
	count=0
	for letter in a:
		if letter==x:
			count+=1
	return count

print countLetter("banana","a")
	