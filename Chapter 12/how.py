# import random

# # Create a black box object that generates random numbers
# rng = random.Random()

# dice_throw = rng.randrange(1,7)   # Return an int, one of 1,2,3,4,5,6
# delay_in_seconds = rng.random() * 5.0 
# print(dice_throw)
# cards=list(range(10))
# rng.shuffle(cards)
# print(cards)

# def makeRandomNumbers(num,lowerBound,UpperBound):
# 	rng = random.Random()
# 	listThing=[]
# 	for i in range(0,num):
# 		listThing.append(rng.randrange(lowerBound,UpperBound))

# 	return listThing

# print(makeRandomNumbers(3,1,10))
import time

def sumItBitches(x):
	sum=0
	for v in x:
		sum+=v
	return sum

s=10000000
xd=range(s)

t0=time.clock()
meraAnswer=sumItBitches(xd)
t1=time.clock()

print("my_result = {0} (time taken = {1:.4f} seconds)"
	.format(meraAnswer, t1-t0))

t2 = time.clock()
their_result = sum(xd)
t3 = time.clock()
print("their_result = {0} (time taken = {1:.4f} seconds)"
        .format(their_result, t3-t2))