from math import sqrt
import sys,re
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = 3
m = '8 7 6'
nums = []
low = m.replace(' ','0')
nums = re.findall('\d+',m)
low = int(low)
min_root = sqrt(low)
def rootIncludes(min_root):
	value = pow(min_root,2)
	value_str = str(value)
	j = 0
	for i in nums:
		if(value_str[j] != i):
			return False
		j = j+2
	return True

min_root = int(min_root)
while(1):
	if(int(nums[-1])%2==min_root%2):
		if(rootIncludes(min_root)):
			print min_root
			sys.exit(0)
	min_root = min_root+1