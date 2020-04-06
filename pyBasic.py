#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# this lesson is based on python 3.8

# ====BASIC I/O====
print('hello world') # basic output: print(). use '' or "" to fold string

print('The quick brown fox', 'jumps over', 'the lazy dog') # link different string with auto-add space

print(100+200) # print 300

name = input() # save input string to variable

name = input('please enter your name:') # add a string as prompt

print('hello,', name)

sciNote = 1.2e9 / 2.4e8 # can use scientific notation

print("I'm OK.") 
print('I\'m \"King\"!') # if a string contains '' and "", use \ to note these special symbol. print `I'm "King"!`

print('first line \n second line') # \n as escape character, line continuation
# for note, \t as tab, \\ as \
print(r'first line \n second line') # in `r''`, cancel any special escape character

print('''If you miss the train I'm on
you will know that I'm gone
you can hear the whistle blow
one hundred miles''') # use '''...''' to note multiple lines


# ====VARIABLE AND TYPE====

# boolean characters are `True` and `False`. note the capitalization
if True:
    print(1<0) # print `False`
	# use 4 space as indentation
else:
    print(True and False, True or False, not True) # 3 boolean operators: and, or, not. print `False True False`

None # a special value, not equal to 0.

var = 1 # variable name has to be composed of a-z, A-Z, 0-9, _ and cannot start with a number
var = 2.7
var = 'hi'
var = True 
# Python is a dynamic language, since its variable type is not static. 
# In static language like C and Java, variable type has to be claimed when it is defined, and cannot be changed.

# constant variable is usually all capitalized, like this preset constant variable, PI (need import math?)
#print(PI) # print 3.14159265359
# actually, you can change its value as you will.

print(10/3) # print `3.333333333`. division `/` always lead to precise float result
print(4/2) # print `2.0`.
print(5//2) # print `2`. this division operator `//` always lead to integer result, like in C
print(5%1) # print `1`. `%` gets the left number

# ====STRINGS AND ENCODE====

print('Python3以Unicode编码，所以支持中文')
print(ord('0')) # print `48`. ord() return unicode code of a one-character string
print(chr(48)) # print '0'. chr() do the opposite of ord()

print('\u4e2d\u6587') # print '中文'. you can use \+unicode to print string

'abc'.encode('ascii') # print b'abc'. use .encode() to encode a string to bytes form for transmission and storage
'中文'.encode('utf-8') # print b'\xe4\xb8\xad\xe6\x96\x87'. in bytes form (b'').
b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8') # print '中文'. use .decode() to transform bytes back to string

print('hello, %s'% 'bill') # use % to format. %s for string, %d for integer

# ====LIST AND TUPLE====

newlist = [1, '42', True]
print(newlist[0]) # print 1. use index to fetch item in list
print(newlist[-1]) # print True. -1 as index of last item
print(newlist[-2]) # print '42'.

print(len(newlist)) # print 3. len() to get number of items/characters/bytes in list/string/code

newlist.append(3.14) # .append() add item to the end of list
newlist.insert(1, 'obj') # .insert() insert item to a specific index
newlist.pop() # .pop() delete the last item
newlist.pop(0) # delete the item at a specific index
newlist[2] = False # directly reassign an item in the list
print(newlist) # print ['obj', '42', False]

newlist.append([-23, 'sdor*ca']) # list can be an item of another list

print(newlist[-1][-2]) # fetch item in the sublist. print -23.

noveltuple = ('vsc', 0)
# tuple is defined with (). it is just like list except it cannot be reassigned. it has no methods like .append()  
onetuple = ('lonely',) # to define a tuple with only one item, add a ',' to avoid misintepretation
print(onetuple) # print ('lonely',)

muttuple = (newlist, ' ')
newlist[0] = 'mutone' # tuple items' pointer cannot be reassigned, but the content is mutable.
print(muttuple) # print (['mutone', '42', True, [-23, 'sdor*ca']], ' ')


# ====CONDITIONAL====

if 1+1 == 2:
    print('that is right.') # use 4 spaces to indent subclause
elif input() == 'password': # caution: in if-elif-else, once a condition is fulfilled, all following will be ignored
    print('you got that.')
elif 'false': # any non-null string/number/variable can serve as a True
    print('any *true value* will be a boolean True condition')
else:
    print(None)

if int(input('type in a integer: ')) > 0: # use int() to convert string into integer
    print('it is positive')


# ====LOOPS====

for item in newlist: # for loop can easily use on list & tuple
    print(item)

sum = 0
for num in list(range(10)): # range() generate a 0-x integer succession. list() convert it to a list
    sum = sum + num

while sum == 55:
    sum = sum + 1
    if 'I want to continue':
        continue # use continue to forcibly end this round and start next round
    break # use break to break out of one layer of loops



# ====DICT AND SET====

newdict = {'HP': 100, 'MP': 20, 'EXP': 55} # key-value set. can quickly fetch value for a specific key
print(newdict['HP']) # print 100.
newdict['MP'] = 25 # reassign value of a key

print('ATK' in newdict) # print False. use `in` to see whether a key exist in the tuple
print(newdict.get('ATK', -1)) # print -1. use .get() to get the value of a key. 
# if the key do not exist, it will return a default value (None if a second argument is not there)

newdict.pop('MP') # use .pop() to delete a key and its value. note that dict is unordered

# compare to list, dict occupy more space, but is much faster
# key in dict must be unmutable object, like number or string. list cannot be dict's key

newset = set([1, 2, 3, 1]) # set take a list to initialize. it is a collection of unordered unique keys
print(newset) # print {1, 2, 3}. it stores unique keys
newset.add(4) # .add() to add new keys. if you add old key, that actuall do not change anything
newset.remove(1) # .remove() to remove keys

set2 = set([3, 5, 2])
print(set2 & newset) # print {2, 3}. mathmatical intersection
print(set2 | newset) # print {2, 3, 4, 5}. mathmatical union

# key in set also must be unmutable object

# ====UNMUTABLE OBJECT====
# why strings are unmutable?
strA = 'mutant'
print(strA.replace('a', 'A')) # print 'mutAnt'
print(strA) # print 'mutant'
# the string methods can only work on string and return a new one, but cannot change it