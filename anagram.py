import sys
frequency1 = {}
frequency2 = {}
word1 ='hi'
word2 ='ih'
length = len(word1)
if (length != len(word2)):
	print 'Not anagrams'
	sys.exit(0)
for i in range(length):
	char = word1[i]
	if char in frequency1:
		frequency1[char] += 1
	else:
		frequency1[char] = 1
	char2 = word2[i]
	if char2 in frequency2:
		frequency2[char2] +=1
	else:
		frequency2[char2] = 1

if (len(frequency2)!=len(frequency1)):
	print 'Not anagram'
	sys.exit(0)

for i in frequency1:
	if(frequency1[i] != frequency2[i]):
		print 'Not anagram'
		sys.exit(0)
print 'anagram'