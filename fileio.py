
a = open('practice.txt','r')

text = a.read()

print(text)

a.close()

'''

'r' = read the file
'w' = 'write the file
'a' = 'append the data(at last)
'r+' = 'update the data first'
'rb' = display output in binary format,
'rt' = display output in normal text format
'read() = read, read(int) = which display that many num of chars as output'
'white() = write'
'readlines() = display all the lines in list format'
'''

# instead of writing f.close file repeatedly for that sake we can use keyword called 'with' so that we dont use f.close()

with open("module1.txt",'r') as f:

    print(f.read()) 