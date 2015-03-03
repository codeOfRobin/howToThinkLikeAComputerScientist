def removeLetter(text,letter):#camel case FTW, fuck underscores
	y=""
	for x in text:
		if x!=letter:
			y=y+x
	return y

print removeLetter("happy","a")