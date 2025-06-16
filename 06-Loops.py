# Loops

# while (runs loop until condition is false)

num = int(input("Enter number"))

while(num!=0):

    num = int(input("Enter number"))

print("You entered correct number")


# for 

for i in [1,2,3]:

    print(i)

# for else

for i in [4,5,6]:

    print(i)
else:
    print('Done')

# range 

for i in range(0,20,2):

    print(i)

# Break (break the loop and come out it)

for i in range(0,10,3):

    if(i / 3 ):

        print(i)
        break

# Continue (will continue the loop until ends)

for i in range(0,10,3):

    if(i / 3 ):

        print(i)
        continue

# Pass (it is like  do nothing)


for i in range(0,10,3):

    if(i / 3 ):

        pass

