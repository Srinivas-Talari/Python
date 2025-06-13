from functools import reduce

l = [1,2,38,5,6,4]

def add(a,b) :
    if(a>b):
         return a
    return b

s =  reduce(add,l)

print(s)

# print(max(l))  # 2nd method

# maxNum = l[0]

# for i in l:

#     if(maxNum < i):

#         maxNum = i
# print(maxNum)
