def sum_factors(limit):
	total = 0
	for num in range(limit):
		if(num%3==0 or num%5==0):
			total=total+num
	return total

def get_duplicates(arr):
	dups = set()
	for i in arr:
		if arr.count(i) >= 2:
			dups.add(i)
	return dups    

def doOverlap(topLeft1,topLeft2,bottomRight1,bottomRight2):
	if(topLeft1[0]>bottomRight2[0] or bottomRight1[0]>topLeft2[0]):
		return 'Not overlapping rectangles'
	if(topLeft1[1]<bottomRight2[1] or bottomRight1[1]<topLeft2[1]):
		return 'Not overlapping rectangles'
	return 'Overlapping rectangles'


def get_factorial(num):
	if (num==0):
		return 1
	else:
		return num*get_factorial(num-1)

def stdinRead(num):
	import sys
	print 'Input:',
	a = sys.stdin.readline()
	return a[-(num+1):]

print 'Sum of the factors of 3 and 5 are {}'.format(sum_factors(1000))
print 'Duplicates in the array are: {}'.format(get_duplicates([2 ,4 , 6, 8, 4, 6, 12]))
print doOverlap([0, 10],[10, 0],[5,5],[15,0])
print 'Factorial of {} is {}'.format(4,get_factorial(4))
print 'Last {} characters are {}'.format(4,stdinRead(4))