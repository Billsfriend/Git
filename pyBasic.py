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
print(PI) # print 3.14159265359
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
