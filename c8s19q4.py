def countLetter(string,letter,count):
	if not(string):
		return count
	else:	
		if string[0]==letter:
			return countLetter(string[1:],letter,count+1)
		else:
			return countLetter(string[1:],letter,count)
print countLetter("banana","a",0)
	