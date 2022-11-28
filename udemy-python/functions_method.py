x= input("Enter a number: ")
y = input("Enter the second number: ")
z = x + y
print(z)

#concept of functions
def add(x, y):
    z = x + y
    return print(z)

a = 3
b = 4
add(a, b)

#functions and user input
c= input("Enter the first number: ")
d = input("Enter the second number: ")
c = int(c)
d = int(d)
add(c, d)

#Modifying functions
def div(w, p):
    if(p==0):
        return print("This is not possible")
    else:
        f = w/p
        return print(f)

w = input('Enter any value: ')
p= input('Entrer the second value: ')
div(int(w), int(p))