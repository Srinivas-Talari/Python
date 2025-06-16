# Variables

#Container to stores the values or data

a = 20

"""
Here 'a' is a variable name

'=' is a assignment operator

'20' is a data or value we are assigning

"""

# Variable name Rules

'''
1.We should not use keywords and identifiers as a variable names

2.Only start with alphabet or underscore(_)

3.Should not start with a  number and symbol should not be contains in variable names

'''
# Data Types (type of data we are assigning to the variable)

# integers, floating numbers , strings, boolean, none

# To know the type of data, we have a in-built func called "type"

a = 200

print(a,type(a))

b = 200.23

print(b,type(b))

c = 'Artificial Intelligence'

print(c,type(c))

d = True #False

print(d,type(d))

e = None

print(e,type(e))


#Type Casting (Changing one type of data into another type)

f = 20

print(f,type(f))

g = 20

h = str(20) # Changing int to str here

print(h,type(h))

i = int('30') # Changing str to int here

print(i,type(i))


# input (Allows to take data or values from the users)

'''
Input value by default it a string type to change it as per our requirement we can do type casting concept here
'''

a = input('Enter number')

print(a,type(a)) # a is a string because input is a string type..

a = int(input('Enter number')) # Here i changed str type input to integer input by using type casting concept

print(a,type(a))


# Operators

# Arithmetic  Operators (+,-,*,%,/ **)

a = 30

b = 20

print(a + b) # adding
print(a - b) # subtract
print(a * b) # multiplying
print(a % b) # division which gives remainder as an output
print(a / b) # division which gives quotient as an output
print(a ** b) # to find power

# Asignment operators (Assigning a value to variable name)

a = 40

a *=20  # using all operators(a+=20,a-=20,a%=20,a/=20)

print(a)

# Comparison Operators (Comparing the values or data)

a = 20

b = 40

print(a == b) # checks two values are equal or not
print(a != b) # checks two values are  not equal or not
print(a > b) # checks a is greater than b
print(a < b) # checks a is less than b
print(a >= b) # checks a is greater than or equals to b
print(a <= b) # checks a is less than b or equals to b

# Logical Operators


a = 20

b = 40

# Logical 'OR'

if(a > b or a < b): # 'or' means either one value should be true then it is true otherwise false

    print('Yes')
else:
    print('No')

# Logical 'AND'

if(a > b or a < b): # 'and' means both  values should be true then it is true otherwise false

    print('Yes')
else:
    print('No')









