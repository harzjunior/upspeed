# comment 
# ==============================Keywords================================
# def, return, and, or, not, for, in, while, True, False, if, else, elif 
# import, as, class, continue, break, finally, from, pass, global, raise 
# try, except, del, assert, is, lambda, with, nonlocal

# Variable

# An integer assignment 
age = 30


# ==============================Data Types================================
# It represents the kind of value that tells what operations can be performed on a particular data
# Numeric --> Integer (x = 50), Float (x = 60.5), Complex Number (x = 3j)
# Dictionary (x = {"name": "Joe", "age": 24}), 
# Boolean (x = True), 
# Set ({"geeks", "for", "geeks"})
# Sequence Type --> String (x = "Hello World"), Tuple (x = ("geeks", "for", "geeks"))
#                   List (x = ["geeks", "for", "geeks"])

x = 50  # integer 
print(x, type(x))
x = 60.5  # float
print(x, type(x))
x = 3j  # complex
print(x, type(x))
x = {"name": "Suraj", "age": 24} # dict
print(x, type(x))
x = True  # bool
print(x, type(x))
x = {"geeks", "for", "geeks"} # set
print(x, type(x))
x = "Hello World" # string
print(x, type(x))
x = ("geeks", "for", "geeks")  # tuple
print(x, type(x))
x = ["geeks", "for", "geeks"]  # list
print(x, type(x))
x = b"Geeks" # bytes
print(x, type(x))




# ==============================Input/Output================================
# The type of the returned object always will be <class ‘str’>
# age = input('please enter your age: ')

# print(f'you are {age} years old {type(int(age))}')

# ==============================Operators================================
# Operators in general are used to perform operations on values and variables
# Precedence of Arithmetic Operators --> PEMDAS () ^ * / + -
a = 9
b = 4
add = a + b
sub = a - b
mul = a * b
mod = a % b 
p = a ** b

print(add)
print(sub)
print(mul)
print(mod)
print(p)

pem = 10+30*2/10-1**10
# 40*2/10-1**10
# 40*2/10-1
# 80/10-1
# 8-1
# 7

print(pem)

# ==============================Logical Operators================================
# perform Logical AND, Logical OR, and Logical NOT operations
a = True     # 1
b = False    # 0
print(a and b)
print(a or b)
print(not a)

# ==============================Bitwise Operators================================
# act on bits and perform bit-by-bit operations. These are used to operate on binary numbers.
a = 10
b = 4
print(a & b)  # and          --> 1010 and 0100 = 0000 => 0
print(a | b)  # or           --> 1010 or 0100 = 1110 => 14
print(~a)     # not          --> not 10 = -1011 => -11    //always add -ve and 1
print(a ^ b)  # xor          --> 1010 xor 0100 = 1110 => 14
print(a >> 2) # shift right  --> 1010 = 0010 => 2
print(a << 2) # shift left   --> 1010 = 101000 => 32 + 8 -> 40

# ==============================Assignment Operators================================
# are used to assign values to the variables.
a = 10
b = a  
print(b)    # b = a = 10
b += a      # 10 + 10 + 20
print(b)    # b = 20
b -= a      # b = 20 - 10 = 10
print(b)    # b = 10
b *= a      # b = 10 * 10 = 100
print(b)    # b = 100
b <<= a     # b = 01 1001 0000 0000 0000 -> 65536 + 32768 + 4096 => 102400
print(b)    # b 102400

# ==============================If Else================================
# if a condition is true it will execute a block of statements and if the condition is false it won’t

i = 20
val = 2101
if(i < val):
    print(f"{i} is smaller than {val}")  
    if(val % 2 == 0): 
        print("Block is Even value")
    else:
        print("Block is Odd value")
    print("I'm in if Block") 
else:
    print(f"{i} is greater than {val}")  
    print("I'm in else Block")

print("I'm not in if and not in else Block")


i = 20
if (i == 10): 
	print("i is 10") 
elif (i == 15): 
	print("i is 15") 
elif (i == 20): 
	print("i is 20") 
else: 
	print("i is not present") 

# ==============================For Loop================================
# It is used for iterating over an iterable like String, Tuple, List, Set, or Dictionary
for i in range(1, 11):
      print(i)

fruits_list = ['Banana', 'Kiwi', 'Peach', 'Plums', 'Pomegranate']
veggies_tuple = ('Spinach', 'Okra', 'Tomatoes', 'Bell-Pepper', 'Carrot')
cereals_set = {'Corn-Flakes', 'Coco-Pops', 'Rice-Flakes', 'Fruits-Flakes', 'Golden-Morn'}

for fruit in range(0, len(fruits_list)):
      print(fruits_list[fruit])

for veggie in range(0, len(veggies_tuple)):
      print(veggies_tuple[veggie])


# No, you cannot iterate over a set using an index because sets are unordered 
# collections in Python and do not support indexing
for cereal in cereals_set:
      print(cereal)

# convert the set to a list first, but this approach is not typical for sets
cereals_list_set = list(cereals_set)

for cereals in range(len(cereals_list_set)):
    print(cereals_list_set[cereals])


# ==============================While Loop================================
# the condition for while will be True as long as the counter variable (count) is always true

count = 1
while count <= 10:
      print(count)
      count = count + 1

x = 0
while x < 3:
      x = x + 1
      print(f'{x}: Python is fun')

# ==============================Functions================================
# Is a block of statements that return the specific task. The idea is to put some 
# commonly or repeatedly done tasks together and make a function so that instead of 
# writing the same code again and again for different inputs, we can do the function 
# calls to reuse code contained in it over and over again

# A simple Python function to check 
# whether x is even or odd 
def evenOdd(x): 
	if (x % 2 == 0): 
		print("even") 
	else: 
		print("odd") 


# Driver code to call the function 
evenOdd(2) 
evenOdd(3) 
