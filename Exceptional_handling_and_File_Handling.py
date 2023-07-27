# File Handling

import os
os.getcwd()

os.chdir('D:\\Data')

# file handling #
# the open function takes two parameters filename and model #

# there are 4 different methods for opening a file #
# "r" - reads a default value
# "a" - opens the file for append and creates a file if it does not exist
# "w" - write - opens a file for writing
# "x" - creates a file 

# syntax #
# to open a file or read a file 

f = open("demo1.txt") 
f

# another way to open file
with open("demo1.txt") as file:
  xy  = file.read()

xy

f = open("demo1.txt", "w")
f.write("Adding new lines")
f.close()

f = open("demo1.txt")
f.readline()   # one line at a time  --> fist line

print(f.readline())   # --> second line
print(f.readline())   # --> third line
print(f.readline())   # --> forth line

f = open("demo1.txt", mode = 'r')
print(f.readlines()) # outputs each line separated with comma and all the lines at once
f.close()

f = open("demo1.txt") 
f.read(5) # reads first 5 characters

# write to an existing file #
f = open("demo1.txt", "a")   # create or append
f.write("\nNow the file has more content!")
f.close()

f = open("demo1.txt", "r")
f.read() #observe one extra line is added

# creating a new file #
f = open("demo2.txt", "x")   # create
f.write(' New file')
f.close()

f = open('demo2.txt', 'r')
print(f.read())

f.close()

#Delete a File
#To delete a file, you must import the OS module, and run its os.remove() function:
import os
os.remove("demo2.txt")

f = open(r'D:\Data\education.csv','r')
print(f.read())

f.close()

# Exception Handling

x = eval(input("enter the 1st value = "))

# try: and except: are keywords for exceptional handling, try: provide the code ; except: except the error with a proper statement

#Ex - 1:
try:
    x = eval(input("enter the 1st value = "))
    y = eval(input("enter the 2nd value = "))
    results = x + y
    print(results)
except:
    print("please enter a valid number")


6/0

#Ex - 2: 
try:
    x = eval(input("enter the 1st value = "))
    y = eval(input("enter the 2nd value = "))
    results = x/y
    print("final results = ", results)
except(ZeroDivisionError):
    print("please enter a non-zero value for the divisor")
except(NameError):
    print("Please enter valid number")
except(TypeError):
    print("Please enter both same type")


##In Python, keywords 'else' and 'finally' can also be used along with the 'try' and 'except' clauses while the 'except' block is executed
##if the exception occurs inside the 'try' block, the 'else' block gets processed if the 'try' block is found to be exception free.
try:
    print("try block")
    x = int(input('Enter a number: '))
    y = int(input('Enter another number: '))
    z = x/y
except ZeroDivisionError:
    print("except ZeroDivisionError block")
    print("Division by 0 not accepted")
else:
    print("else block")
    print("Division = ", z)
finally:
    print("finally block")
    x = 0
    y = 0
print ("Out of try, except, else and finally blocks." )

## Built-in Exceptions

## There are plenty of built-in exceptions in Python that are raised when corresponding errors occur. 
## We can view all the built-in exceptions using the built-in local() function as follows:
print(dir(locals()['__builtins__']))

## User Defined Exceptions

x = int(input('Enter the number: '))
if x < 18:
  raise Exception("Sorry, You are not eligible for voting, register once you become 18 years old")
else:
    print('you entered: ', x)

