# Strings (A set of chars is called a string)

name = 'Artificial Intelligence'

print(name[0]) # indicies to access the each char from the string

print(len(name))  # to find length of the string

print(name[-4]) # negative values  indicates indices from end to first

print(name[0:6]) # slicing to get the desired chars from string from one position to another position

print(name[:7]) # no starting values means by default it takes from start char

print(name[3:]) #  no ending values means by default it takes until last char

print(name.upper()) # to change string to uppercase letters

print(name.lower()) # to change string to lowercase letters

b = 'srinivas talari'

print(b.strip()) # to remove the empty spaces in string

print(b.replace('srinivas','seenu')) #replaces old val to new val

print(b.split('-')) # splits the string

c = ['seenu','learns','python']

print(''.join(c)) # joins the strings

print(b.find('r')) # to find char indice

print(b.index('r')) # to find char indice

# find() returns -1 if not found, index() raises an error.

print(b.startswith('a')) # checks str starts with user entered char

print(b.endswith('b')) # checks str ends with user entered char

c = 'seenu'

d = "100"

print(c.isalpha()) # checks it is str or not

print(d.isdigit()) # checks it is num or not

print(c.capitalize()) # first char every str converts into uppercase

a = 'seenu'

b = 25

print('Name:{} age:{}'.format(a,b)) # use as a placeholders

print(f"Name :{a} age:{b}") # simply use f-strings for above things


