# Lists and Tuples (to hold multiples values under single variable)

#Lists (Mutable i.e we can change the values of lists)

a = [1,2.3,True,'AI',None,5.9,2.3]

a.append('ML') # which adds values at last
a.extend(['dsa','algorithms']) # extend the list
a.insert(1,False) # insert val at given index 
a.remove(None) # remove the val
a.pop(3) # remove the last ele in list and if we mention the index it will remove ele at particular index


b = a.index(False) # find index of mentioned val

c =  a.count(2.3) # count no of vals

f = [34,89,12,7,56]

e = f.reverse() # reverse the list items

g = f.sort() # sort the values in an order

h = f.clear() # remove all values in list

# Tuples (immutable i.e we can't change the values in tuple)

t = (1)

print(t,type(t)) # returns int

t = (1,)

print(t,type(t)) # returns tuple

tup = (1,2,3,True,'Seenu',3,None,3)

print(tup.count(3))

print(tup.index(3))

