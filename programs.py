import re
import datetime
import sys
total_chars = 256
def check_anagram(word1,word2):#1
    word1 = word1.lower()
    word2 = word2.lower()

    w1_length = len(word1)
    w2_length = len(word2)
    frequency1 = [0]*total_chars
    frequency2 = [0]*total_chars
    if(w1_length!=w2_length):
        return False
    for i in word1:
        frequency1[ord(i)] += 1
    for i in word2:
        frequency2[ord(i)] += 1
    for i in xrange(total_chars):
        if (frequency2[i]!=frequency1[i]):
            return False  
    return True
# Testing Anagrams;
print 'Anagram' if check_anagram('bat','tab') else 'Not Anagram' #Anagram
print 'Anagram' if check_anagram('GOD','dog') else 'Not Anagram' #Anagram
print 'Anagram' if check_anagram('ab','ac') else 'Not Anagram'   #Not Anagram


def parseDate(date_text):#2
    try:
        dt = datetime.datetime.strptime(date_text, '%m/%d/%Y')
        return dt.strftime('%Y %m %d')
    except ValueError:
        raise ValueError("Incorrect data format, should be M/D/YYYY")
print 'Formatted date is: {}'.format(parseDate('12/2/2017')) #Formatted date is: 2017 12 02


def check_frequency(text,given_word):#3
    count = len(re.findall(given_word,text))
    return count
text = 'The quick brown fox jumps over the lazy dog.The quick brown fox jumps over the lazy dog.'
given_word = 'dog'
print '{} occured in the given text {} times'.format(given_word,check_frequency(text,given_word)) #dog occured in the given text 2 times


class Node: #4
    #Node for a LinkedList
    def __init__(self, data):
        self.data = data
        self.next = None
 
class LinkedList:
 
    # Initializing head
    def __init__(self):
        self.head = None
 
    # Reverse the linked list
    def reverseList(self):
        prev = None
        current = self.head
        while(current!=None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
         
    # Insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
 
    # Print LinkedList
    def displayList(self):
        temp = self.head
        while(temp):
            print temp.data,
            temp = temp.next
 
 
# Testing
llist = LinkedList()
llist.push(7)
llist.push(9)
llist.push(11)
llist.push(80)
 
print "Linked List"
llist.displayList()#80 11 9 7 
llist.reverseList()
print "\nReversed Linked List"
llist.displayList()#7 9 11 80 
print '\n'


def check_polindrome(word):#5
    word = word.lower()
    length = len(word)
    check = 1
    for i in range(length/2):
        if(word[i]!=word[length-i-1]):
            check=0
    if(check==1):
        return True
    else:
        return False
print 'Polindrome' if check_polindrome('pop') else 'Not Polindrome'  #Polindrome
print 'Polindrome' if check_polindrome('peep') else 'Not Polindrome' #Polindrome
print 'Polindrome' if check_polindrome('cat') else 'Not Polindrome'  #Not Polindrome


def get_max(array):#6
    max1=max2=float('-inf')
    for num in array:
        if(num>max1):
            max2 = max1
            max1 = num
        elif(num>max2 and num<max1):
            max2=num
    return (max1,max2)
print 'Biggest numbers in the list are :{}'.format(get_max([1,3,5,7,0,8,6])) #Biggest numbers in the list are :(8, 7)


def sum_factors(limit):#7
    total = 0
    for num in range(limit):
        if(num%3==0 or num%5==0):
            total=total+num
    return total


def get_duplicates(arr):#8
    dups = set()
    for i in arr:
        if arr.count(i) >= 2:
            dups.add(i)
    return dups    

def stdinRead(num):#9
    print 'Input:',
    a = sys.stdin.readline()
    return a[-(num+1):]

def doOverlap(topLeft1,topLeft2,bottomRight1,bottomRight2):#10
    if(topLeft1[0]>bottomRight2[0] or bottomRight1[0]>topLeft2[0]):
        return 'Not overlapping rectangles'
    if(topLeft1[1]<bottomRight2[1] or bottomRight1[1]<topLeft2[1]):
        return 'Not overlapping rectangles'
    return 'Overlapping rectangles'


def get_factorial(num):#11
    if (num==0):
        return 1
    else:
        return num*get_factorial(num-1)


print 'Sum of the factors of 3 and 5 are {}'.format(sum_factors(1000)) #Sum of the factors of 3 and 5 are 233168
print 'Duplicates in the array are: {}'.format(get_duplicates([2 ,4 , 6, 8, 4, 6, 12])) #Duplicates in the array are: set([4, 6])
print doOverlap([0, 10],[10, 0],[5,5],[15,0]) #Overlapping rectangles
print 'Last {} characters are {}'.format(4,stdinRead(4)) #Print last 4 chracters
print 'Factorial of {} is {}'.format(4,get_factorial(4)) #Factorial of 4 is 24