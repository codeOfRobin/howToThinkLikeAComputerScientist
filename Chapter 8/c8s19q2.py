# s="adsnonfh"

# """
#   >>> len(s)
#   8
#   >>> s[4:6] == 'on'
#   True
# """



# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()


prefixes = "JKLMNOPQ"
suffix = "ack"

for letter in prefixes:
    if letter=="O" or letter=="Q":
    	print(letter+"u"+suffix)
    else:
    	print(letter + suffix)
