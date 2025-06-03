# Dictionary (Used to store multiples values just like lists and tuples but here in the form of name and value pairs)

#Mutable (we can change the values)

# Unordered, cannot contain duplicate values

bio = {

    "name" : 'AI',

    "age" : 2000,

    "discovered" : 'Google'

}

bio['age'] = 10000  # way to access the value

c = bio.update({"place" : 'ABC'})  # to update the dict

d = bio.items() # display all items

e = bio.keys() # return all keys

f = bio.values() # return all values

# Sets (cannot take duplicate values and immutable,unordered)

s = {1,2,3,4,5}

t = {4,5,6,7,8}

# s.add(1) # add val to set
# s.pop()  # remove arbitrary element
# s.clear() # empty the set

print(s.intersection(t))  # return common val in both sets

print(s.union(t))  # return all  val in both sets but not repeated vals

print(s.difference(t))  # remove duplicate vals and return remaining vals in set-1

print(s.issubset(t)) # True if all elements of a in b

print(s.issuperset(t)) # True if all elements of b in a

print(s.isdisjoint(t)) # True if no common elements


