import math
from decimal import Decimal
inp = '7 5'
n,q = inp.split()
arr = '-2 4 16 -4 5 80000 100000'
arr = arr.split()
numbers = [int(i) for i in arr]
for i in range(int(q)):
    query = '6 7'.split()
    value=1
    neg = False
    for i in numbers[int(query[0])-1:int(query[1])]:
    	 value = value*i
    if(value<0):
    	value = -value
    	neg = True
    cube_root = round(value**Decimal(1/3.0))
    sq_root = int(math.sqrt(value))
    if (math.pow(cube_root,3)==value):
        if(math.pow(sq_root,2)==value and not neg):
            print 'Both'
        else:
            print 'Cube'
    elif (math.pow(sq_root,2)==value and not neg):
        print 'Square'
    else:
        print 'None'