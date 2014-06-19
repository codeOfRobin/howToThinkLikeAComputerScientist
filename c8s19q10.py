def reverse(x):
	if len(x)<=1:
		return x
	return reverse(x[1:])+x[0]

def isPalindrome(x):
	if reverse(x)==x:
		return True
	else:
		return False

print isPalindrome("abba")