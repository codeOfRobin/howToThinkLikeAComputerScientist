def dotMultiplication(l1,l2):
	l3=0
	for i in range(0,len(l1)):
		l3=l3+l1[i]*l2[i]
	return l3
print dotMultiplication([1, 2], [1, 4])
	