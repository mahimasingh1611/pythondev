# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print ("Hello World");
# print without new line by defaault
print("Hello World", end='')
print("Hello World", end=', ')
print("Hello World", end='\n')

# Python is an indentation language for defining scope

# python data types -
# int, float, str, list, dict, tup, set, bool 
# list = [10, "Hello", 10.0] # list can have multiple types of data types
# dict = {"key1":"value1", "key2": "value2"}
# tuples = objects cannot be changed, like lists (10, "Hello", 10.0)
# set= unordered collections of unique objects in unordered collection ("a","b")
# bool = True, False

# modulus - for remainder
# 7%4 = 3
# power - 2**3 = 8

# Why doesn't 0.1+0.2-0.3 equal 0.0 ?
# This has to do with floating point accuracy and computer's 
# abilities to represent numbers in memory

var = 10
# cannot start with number, and cannot use symbols

# Python uses dynamic typing, means data type can be changed after re-assigning
var = 10
var = "Vishwadeep"
var = ["hello",20]
# this is sometime risky

var = 10;
print (var);
print (type(var)) # <class 'int'>
var = "Vishwadeep"
print (type(var)) # <class 'str'>
var = ["hello",20]
print (type(var)) # <class 'list'>
var = 10.0
print (type(var)) # <class 'float'>
var = {"key1":"value1", "key2": "value2"}
print (type(var)) # <class 'dict'>

# STRINGS
#:TODO all string object member functions
var = "Vishwadeep" # ordered sequqnce of characters
# string can be saved in single quotes also
print (var[0])
print (var[1])
# for reversing
print (var[-1]) # last letter
print (var[-2]) # second last character

# slicing var[start:stop:step]
print (var[1:5:1]) # before till 5th item with step size 1
print (var[1:-1:1]) # before till last item
print (var[1::1]) # if not provided, means till end
print (var[:5:1]) # if not provided, means from start till 5th
print (var[::]) # this is whole string, means start till end with step size 1
# jump size is 2
print (var[::2]) # this is whole string, means start till end with step size 2
print (var[::-1]) # this will reverse the string

# length of string
print (len(var)) # length of string
print (len(var[1:5:1])) # length of string

# strings are immutable
#var[1] = 'X' # this will give runtime error

# string concatenations
var1 = var[1:3] + var[4:]
print (var1)
print ('2'+'3') # 23
# below will compilation error, as both datatype different
# print ('2'+3) # 23

# string upper case
print (var.upper())
print (var.lower()) # all lowercase
lvar = var.split() # default split with white space and return list
print (lvar)
var = "Hello, world, how, are, you";
lvar = var.split(',')# split using comma
print (lvar)

# string format
var = "Vishwadeep"
print ('This is a string {}'.format(var))
print ('This is a string {} {} {}'.format(var,'fox', 'quick'))
# index also can be decided
print ('This is a string {2} {1} {0}'.format(var,'fox', 'quick'))
print ('This is a string {0} {0} {0}'.format(var,'fox', 'quick'))
# variable type assignment is also possible
print ('This is a string {f} {i} {i}'.format(f=var,i='fox', j='quick'))

result = 100/777
print ("return is {r}".format(r=result)) # result = 0.1287001287001287
# {value:width.precision f} // width for characters and precision for result
print ("return is {r:1.3f}".format(r=result)) # result = 0.129
print ("return is {0:1.3f}".format(result)) # result = 0.129


# string format direct
name = "Vishwadeep"
print (f"Hello my name is {name}")
phone = 741111
print (f"Hello my name is {name} and phone is {phone}")
fl = 10.3
print ("My name is %s and %d and %f" %(name,phone, fl)) # using data

# LISTS, can have mixed data types
# they are in square brackets
#:TODO all list object member functions
mylist = [1,2,3]
print (mylist[1])
mylist[1] = "Vishwadeep" # not immutable, we can change value
print (mylist[1]) 
print (len(mylist)) # print length of list
print (mylist[1:]) # slicing like string, from 1 till end
# list concatenation
mynewlist = mylist + [1,2,3]
print (mynewlist)

mynewlist.append(10) # append at the end
#by default, location is -1, which means last item
item = mynewlist.pop() # remove last item from the list, and returns also the item
item = mynewlist.pop(3) # remove 3rd items and return as well

mylist = [1,8,3,2,4,0]
mylist.sort() # this doesnot return, but sort and save there only
print (mylist)

# if print (value) = gives you "None", means function/value doesnot returns anything
mylist.reverse() # this doesnot return, but reverse and save there only
print (mylist)

# nested list
mylist = [1,2,[3,4]]
print (mylist[1]) # gives 2
print (mylist[2][1]) # gives 4


"""
Python List Methods
append() - Add an element to the end of the list
extend() - Add all elements of a list to the another list
insert() - Insert an item at the defined index
remove() - Removes an item from the list
pop() - Removes and returns an element at the given index
clear() - Removes all items from the list
index() - Returns the index of the first matched item
count() - Returns the count of number of items passed as an argument
sort() - Sort items in a list in ascending order
reverse() - Reverse the order of items in the list
copy() - Returns a shallow copy of the list

"""

#DICTIONARIES
#:TODO all dict object member functions
# unordered and cannot be sorted
# they are in curly braces
# Keys of a Dictionary must be unique and of immutable data type such as Strings, Integers and tuples
var = {"key1":"value1","key2":10,"key3":1.01}
print (var["key1"])
print (var["key2"])
print (var["key3"])
var["key3"] = "Vishwadeep Singh"
print (var["key3"])
# print keys of dictionary
print (var.keys())
# print values of dictionary
print (var.values())
# print keys and values as tuples of dictionary
print (var.items()) # this will return list of tuples
var["key4"] = [1,2,3,4] # append new key with list
var["key5"] = {"key1":"value1","key2":10,"key3":1.01} # append new key with new dictionary
print (var["key5"]["key3"]) # this will give 1.01
var[5] = 100
print (var[5])

"""
Method	                     Description
clear()	                      Remove all items form the dictionary.
copy()	                      Return a shallow copy of the dictionary.
fromkeys(seq[, v])	          Return a new dictionary with keys from seq and value equal to v (defaults to None).
get(key[,d])                     	Return the value of key. If key doesnot exit, return d (defaults to None).
items()	                     Return a new view of the dictionary's items (key, value).
keys()	                     Return a new view of the dictionary's keys.
pop(key[,d])	                     Remove the item with key and return its value or d if key is not found. If d is not provided and key is not found, raises KeyError.
popitem()	                     Remove and return an arbitary item (key, value). Raises KeyError if the dictionary is empty.
setdefault(key[,d])	                     If key is in the dictionary, return its value. If not, insert key with a value of d and return d (defaults to None).
update([other])	                     Update the dictionary with the key/value pairs from other, overwriting existing keys.
values()	                     Return a new view of the dictionary's values
all()	                     Return True if all keys of the dictionary are true (or if the dictionary is empty).
any()	                     Return True if any key of the dictionary is true. If the dictionary is empty, return False.
len()	                     Return the length (the number of items) in the dictionary.
cmp()	                     Compares items of two dictionaries.
sorted()	                     Return a new sorted list of keys in the dictionary.
"""

#TUPLES
#:TODO all tuples object member functions
# they are immutable, cannot be mutated/changed
# they are in round brackets

var = (1,2,3)
print (len(var)) # print length of tuple
# var[1] = 100 # this will give runtime error
print (var[1])
print (var[-1]) # print last item of tuple
print (var.count(1)) # print occurence of 1 in tuple var
print (var.index(2)) # print first occurence of 2 in tuple var



#SETS
#:TODO all sets object member functions
# they are unique in one set
var = set()
var.add(1)
var.add(2)
var.add(3)
var.add(4)
var.add(4) # this will not add, as 4 already exists
print (var)

varlist = [1,1,1,2,2,2,3,3,3,4,4,4,4]
var = set(varlist) # this accepts iterable items
print (var) # gives unique {1, 2, 3, 4}

var = set('Vishwadeep')
print (var) # this will give unique characters in string

"""
Method	                     Description
add()	                     Adds an element to the set
clear()	                     Removes all elements from the set
copy()	                     Returns a copy of the set
difference()	                     Returns the difference of two or more sets as a new set
difference_update()	                     Removes all elements of another set from this set
discard()	                     Removes an element from the set if it is a member. (Do nothing if the element is not in set)
intersection()	                     Returns the intersection of two sets as a new set
intersection_update()                     	Updates the set with the intersection of itself and another
isdisjoint()	                     Returns True if two sets have a null intersection
issubset()                     	Returns True if another set contains this set
issuperset()	                     Returns True if this set contains another set
pop()	                     Removes and returns an arbitary set element. Raise KeyError if the set is empty
remove()	                     Removes an element from the set. If the element is not a member, raise a KeyError
symmetric_difference()	                     Returns the symmetric difference of two sets as a new set
symmetric_difference_update()	                     Updates a set with the symmetric difference of itself and another
union()	                            Returns the union of sets in a new set
update()	                     Updates the set with the union of itself and others
all()	                     Return True if all elements of the set are true (or if the set is empty).
any()	                     Return True if any element of the set is true. If the set is empty, return False.
enumerate()	                     Return an enumerate object. It contains the index and value of all the items of set as a pair.
len()	                     Return the length (the number of items) in the set.
max()	                     Return the largest item in the set.
min()	                     Return the smallest item in the set.
sorted()	                     Return a new sorted list from elements in the set(does not sort the set itself).
sum()	                     Retrun the sum of all elements in the set.

"""


"""
Advantages of Tuple over List
Since tuples are quite similar to lists, both of them are used in similar situations as well.
However, there are certain advantages of implementing a tuple over a list. Below listed are some of the main advantages:
We generally use tuple for heterogeneous (different) datatypes and list for homogeneous (similar) datatypes.
Since tuples are immutable, iterating through tuple is faster than with list. So there is a slight performance boost.
Tuples that contain immutable elements can be used as a key for a dictionary. With lists, this is not possible.
If you have data that doesn't change, implementing it as tuple will guarantee that it remains write-protected.
"""

#Booleans
# True/Flase
var = True
if var:
    print ("Hello there!")
    
print (type(var)) # <class 'bool'>


# None datatype
# There's no null in Python, instead there's None 
# The None keyword is used to define a null value, or no value at all.
# None is not the same as 0, False, or an empty string. None is a datatype of its own (NoneType) and only None can be None.
# :TODO needs to check uses of NoneType
x = None
print(x)
var = None
if var:
    print ("Hello there!")
elif var is None:
    print ("Hello It is NoneType!")
    
print (type(var)) # <class 'NoneType'> 

# File handling
#myfile = open('myfile.txt') #by default open in read mode
# if file not exists FileNotFoundError: [Errno 2] No such file or directory: 'myfile.txt'

# hence create the file
myfile = open('myfile.txt', 'w') # open in write
myfile.write("This is line 1\n")
myfile.write("This is line 2\n")
myfile.write("This is line 3\n")
myfile.write("This is line 4\n") # write to file
myfile.close() # close the file

# to read file whole in one string
myfile = open('myfile.txt')
contents = myfile.read(); 
print (contents) 
myfile.close()

# to read file line by line
myfile = open('myfile.txt')
line = myfile.readline(); 
print (line) 
line = myfile.readline(); 
print (line)
line = myfile.readline(); 
print (line)
myfile.seek(0) # this will move cursor to top
line = myfile.readline(); 
print (line) 
myfile.close()


# other modes
# 'r' - read mode, default
# 'w' - write mode
# 'a' - append mode
# 'r+' - reading and writing
# 'w+" - writing and reading, overwrites existing files and creates a new file


"""
File handling methods
Method	Description
close()	Close an open file. It has no effect if the file is already closed.
detach()	Separate the underlying binary buffer from the TextIOBase and return it.
fileno()	Return an integer number (file descriptor) of the file.
flush()	Flush the write buffer of the file stream.
isatty()	Return True if the file stream is interactive.
read(n)	Read atmost n characters form the file. Reads till end of file if it is negative or None.
readable()	Returns True if the file stream can be read from.
readline(n=-1)	Read and return one line from the file. Reads in at most n bytes if specified.
readlines(n=-1)	Read and return a list of lines from the file. Reads in at most n bytes/characters if specified.
seek(offset,from=SEEK_SET)	Change the file position to offset bytes, in reference to from (start, current, end).
seekable()	Returns True if the file stream supports random access.
tell()	Returns the current file location.
truncate(size=None)	Resize the file stream to size bytes. If size is not specified, resize to current location.
writable()	Returns True if the file stream can be written to.
write(s)	Write string s to the file and return the number of characters written.
writelines(lines)	Write a list of lines to the file.
"""

#python directory - 
import os
print (os.getcwd())
#os.chdir('/home/vihswa')
#print(os.listdir())
#os.mkdir('test')
#os.rename('test','new_one')
#os.remove('old.txt')


# comparison operators
var1 = "Vishwadeep"
var2 = "Vishwadeep"
var3 = "Singh"
if (var1 == var2):
    print ("Equals")
    
if (var1 != var3):
    print ("Not Equals")

var4 = 100;
# this will not be equal, as data type will also be compared
if (var1 == var4):
    print ("Equals")

# using and, or, not
if ((var1 != var4) and ((var1 == var2) or (var1 == var4))):
    print ("Equals")
    
if (not (var1 != var2) ):
    print ("True")
    
if (1 == 2):
    print ("Here 1")
elif (2 == 2):
    print ("Here 2")
else:
    print ("Here 3")

# Loops (for loops)
# looping over iterables items like lists, dictionary

var = [1,2,3,4,5,6,7,8,9,10]

for item in var:
    print (item)

for _ in var:
    print ("Cool, here we are not using variable name")
# range is useful for range (start, stop[, step])
for i in range(0,6,1):
    print(i)

var = "Vishwadeep" # for loop with string
for item in var:
    print (item, end=',')
    
print ("")
# Tuple unpacking
tuplist = [(1,2),(3,4),(5,6)]
for item in tuplist:
    print (item)
# above witl give
#(1, 2)
#(3, 4)
#(5, 6)
# For Tuple unpacking
for a,b in tuplist:
    print (a)
    print (b)

var = {"key1":"value1","key2":10,"key3":1.01}
# iterate over keys
for item in var.keys():
    print (item)
# iterate over values
for item in var.values():
    print (item)
    
# iterate over items
for item in var.items():
    print (item) # this is tuples
    
# iterate over items as tuples
for key,value in var.items():
    print (value)

# Loops (while loops)
x = 0
while (x < 5):
    print (f'current value of x = {x}')
    x = x + 1; # x += 1
else:
    # this will get executed, when condition fails
    print ("Loop completed");

# loop breaking
# break
# continue
# pass; do nothing at all, This code does nothing.
# pass also can be used as for function which do noting 
# def function: pass
x = [1,2,3,4,5]
for item in x:
    pass; # means, do nothing at all, this will move to ahead statements
    print (item)
    print ("Looping now")
    if (item % 2) == 1:
        print ("here for continue")
        continue; # move to next iteration
    if (item == 4):
        print ("here for break")
        break; # breaks the iteration
        
#pass
"""
In Python programming, pass is a null statement. The difference between a comment and pass statement in Python is that, while the interpreter ignores a comment entirely, pass is not ignored.
However, nothing happens when pass is executed. It results into no operation (NOP).
We generally use it as a placeholder.
Suppose we have a loop or a function that is not implemented yet, but we want to implement it in the future. They cannot have an empty body. The interpreter would complain.
"""