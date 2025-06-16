#Functions

'''
1.to perform tasks without repeating code again and again
2. we can return the value using return statement
3. we should call the function
4.function parameters(define values) and function arguments(actual values)
'''

def getResult(a):
    
    return(f"Hi  i am sora, i am {a} years old")
    
finalResult = getResult(200000)

print(f"The robot bio is: {finalResult}")


# Default Paramaters

def getName(name = 'srinivas'):

    return f"My name is {name}"

userName1 = getName('talari') # takes this name as a value

userName2 = getName()  # takes default value

print(userName1)
print(userName2)


# Recursion (calling function itself)

def factorial(n):
    if n == 0:        # Base case
        return 1
    else:
        return n * factorial(n - 1)  # Recursive case

getResult = factorial(5)

print(getResult)
