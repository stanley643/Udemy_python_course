#if - else condition
x = 3
y = 7
if(x == y):
    print('They are equal')

else:
    print('They are not equal')

#elif condition
x=4
y=5
z= 2
if(x == y):
    print('x and y are equal')
elif(x>y):
    print('x is greater than y')
elif(x<y):
    print('x is less than y')
else:
    print('working')

#strings
x ="fade"
y = input('Enter a word: ')
if(x == y):
    print("x and y are equal")
else:
    print("x is not equal to y")

#Multiple conditions
x = 5
y = 5
z = 5
if(x==y and x!=z):
    print('x is equal to y')

#nested conditions
if(x == y):
    if(x != z):
        print('x equal to y')
    else:
        print('it breaks here')