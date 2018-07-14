a=[1,3,5,7,0,8,6]
max1=max2=float('-inf')
for num in a:
	if(num>max1):
		max2 = max1
		max1 = num
	elif(num>max2 and num<max1):
		max2=num
print max1,max2