print "        1   2   3   4   5   6   7   8   9  10  11  12"
print "  :--------------------------------------------------"
import string
for x in range(1,13):
	print string.rjust( "{0}".format(x),2),
	for y in range(1,13):
		print string.rjust("{0}".format(x*y),4),
	print "\n"