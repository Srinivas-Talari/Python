# # 1. Walrus Operator (:=)

if(n := len([1,2,3,4,5])) > 3:

    print(f"List is too long {n} elements expected <=3")

 

#  2. Type Hints  (Explicitly defining type of a data)

# using (:) for variables

age : int = 25

name : str = 'srinivas'

isValid : bool = True

# using (->) for variables

def getValue(a : int,b : int) -> int:

    print(a + b)

getValue(100,89)

from typing import List,Tuple,Dict,Union

number : List[int] = [1,2,3,4,5,6]  # List of integers

bio : Tuple[str,int] = (1,2,3,4,5,'AI')  # Tuple of strings and integers

scores : Dict[str,int] = {'alice': 100, 'ABC' : 200} # Dict of data in form of key and values

identifier : Union[int,str] = 'ID123' # Union types which holds multiple types

identifier = 12345 # Also valid


# #Match (Matches the user entered case and provide output a/c to it)

def work(role) : 

    match role :

        case 'designer':

            return 'He designs the site'
        
        case 'developer':

            return 'He develops the site'
        
        case 'tester':

            return 'He tests the site'
        case 'cybersecurity':

            return 'He protects the site'

print(work('designer'))
print(work('cybersecurity'))
print(work('developer'))
print(work('tester'))

# # Operator(|) to merge the dictionaries

dict1 = {'a' : 1, 'b' : 2,'c':3}

dict2 = {'a':10,'b':20,'c':30}

print(dict1 | dict2)

#  Use multiple context managers in a single with statement using parenthesis

with(

    open('file1.txt') as f1,
    open('file2.txt') as f2
):
    
    # process files



# Error Handling

try:  # Code you think that might get error

    a = 10

    b = int(input("Enter the number"))

    print(a/b)

except Exception as f:  # code to find error

    print(f)

except ZeroDivisionError:  # error says result is not possbile if value is 0

    print('b cannot be 0')

except ValueError:  # checks if user enter wrong data (here str instead of int)

    print('b cant be string')

else:  # only runs when try is succesful

    print(a + b)

finally :  # always runs irrespective of above result

    print('Process completed')

print(__name__)  # modules __name__ and __main__


# Global keyword changes global variable

a = 20

def result():


    global a

    a = 100

    print(a)

result()

print(a)

#enumerate 

l = [100,101,102,103,105,105]

# Normal method

index = 0  

for i in l:


    print(f'the value at {index} is {i}')

    index+=1

# with enumerator

for index,i in enumerate(l):
        print(f'the value at {index} is {i}')

# List comprehension

#normal method

l = [1,2,3,4,5,6]

nl = []

for i in l:
     
     if(i > 0):
          
          nl.append(i**2)

print(nl)

# List Comprehension method

l = [1,2,3,4,5,6]

nl = [i**2 for i in l]

print(nl)

# lambda

#Syntax Lamba argument: expressions

square = lambda x : x ** 3

print(square(3))
print(square(13))
print(square(23))

add = lambda a,b,c : a + b +c

print(add(456,45,234))

print(add(234,78987,234235))

#JOIN (join string with user specified data)

l = ['apple','mango','grapes']

nl = ", and ,".join(l)

print(nl)

#format method

name = 'ABC'

age = 100

print("My name is {} and i am {} years old".format(name,age))


# map,filter,reduce

# Map

l = [1,2,3,4,5]

squ = lambda x : x * x

sqList = map(squ,l)

print(list(sqList))


#filter


def even(n):

    if(n % 2==0):
        return True
    return False

fiList = filter(even,l)

print(list(fiList))


# reduce

from functools import reduce

def sum(a,b):

    return a + b

print(reduce(sum,l))


          




