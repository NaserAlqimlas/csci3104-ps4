
import numpy as np 
import random
import matplotlib as mplib
import matplotlib.pyplot as plot 


def func(x):
	letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	numbers = xrange(1, 27)

	for i, k in enumerate(letters):
		if x == k:
			return numbers[i]


data = open('assignmentNames.txt', 'r')
choose = random.sample(xrange(0, 88798), 44400)

buckets = 200
hashTable = [list() for x in range(buckets)]  
bucketLength = []
for i in range(buckets):
	bucketLength.append(0)

bucketNum = []
lines = data.readlines()
total = 0

for i in choose:
	total = 0
	entry = lines[i]
	name = entry.split()[0]

	for j in name:
		total += func(j)

	h = total % buckets

	bucketNum.append(h)
	hashTable[h].append(name)

for k, b in enumerate(hashTable):
	bucketLength[k] = len(b)

fig, ax = plot.subplots()
ax.hist(bucketNum, buckets, range = (0,buckets))
plot.title("Histogram")
plot.show()


