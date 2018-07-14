n = 1024
output = ''
while((n/128)>127):
    i = n%128
    n = n/128
    output = '{}.{}'.format(output,i)
output = '{}.{}'.format(n/128,n%128)
k = len(output.split('.'))
while k<=4:
	k=k+1
	output = '{}.{}'.format(0,output)
print output