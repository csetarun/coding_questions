text = raw_input('Enter article')#'OP explained in a comment that strings such as foo 08/13/2015 bar should not be automatically thrown away, and that the date should be extracted from them.To achieve that, we must first search for a candidate string in user'
count = 0
given_word = raw_input('Enter word to search')#'should'
count = [1 for word in text.split() if (word==given_word)]
print len(count)