word= 'aba'
length = len(word)
check = 1
for i in range(length/2):
	if(word[i]!=word[length-i-1]):
		check=0
if(check==1):
	print 'Polindrome'
else:
	print 'Not Polindrome'