def addVectors(l1,l2):
    l3=[]
    if len(l1)==len(l2):
        for i in range(0,len(l1)):
            l3.append(l1[i]+l2[i])
    return l3
print addVectors([1, 1], [1, 1])
print addVectors([1, 2], [1, 4])
