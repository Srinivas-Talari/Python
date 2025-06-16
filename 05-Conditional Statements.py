#Conditional Statements (if,else,elif)

'''

1. if 'if' condition is true  it will stop exceution and wont check else block

2. it will enter into else block only if block condition is false'

3. if there is n number of possibile conditions then we use elif statements only exceutes if 'if' block is false

4. there can be any number of elif blocks

5.the indentation is important

'''

a = 10

if(a == 20):
    print("Yes")  

elif(a > 15):
    print('yes yes')
else:
    print('No')


# Ternary Operator

a = 100

print('Yes' if a == 100 else 'No')