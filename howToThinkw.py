prefixes="JKLMNOPQ"
suffixes="ack"

for letter in prefixes:
	if letter=="Q" or letter=="O":
		print letter+"u"+suffixes
		