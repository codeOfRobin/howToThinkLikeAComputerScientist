import string

x=""" 
This method returns a copy of the string in which all chars have been stripped from the beginning and the end of the string.
"""
x=string.strip(x)

punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

def remove_punctuation(s):
    s_sans_punct = ""
    for letter in s:
        if letter not in punctuation:
            s_sans_punct += letter
    return s_sans_punct

l1=remove_punctuation(x).split(" ")
count=0
for word in l1:
	for letter in word:
		if letter=="e":
			count=count+1
			break



print "There are {0} words, of which {1} contain the letter 'e' ".format(len(l1),count)