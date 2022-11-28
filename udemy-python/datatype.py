#numbers
x = 4
print(type(x))
#int
#float
#double

#operations
#arithmetric operators(+ - / * ** ())
y= 3 + 5 * 6
print(y)

#dynamic typing and restriction in data types
 
 #casting
z = 2
print(z)
z=float(2)
print(z)

#STRINGS
c = 'water'
print(type(c))

#Methods and Strings (dir('string'))
print(c.upper())
c.replace('', '')
#indexing and slicing
print(c[3])

a= 'hello world'
print(a[1:4])

#string formating, ie string concatination
x= 22
y= 'Stanley'
z= "My name is {1} and my age is {0}".format(x , y)
print(z)
#or
z = f"My name is {y} and my age is {x}"
print(z)

x= ['Linda' , 'Music' , '21']
z= f"My name is {x[0]} and I like {x[1]} and am {x[2]} years of age"
print(z)

list1 = ['JavaTpoint', 1, 2.50, {'Name: ' 'peter'}]
print(type(list1))

tuple1 = ('javaTpoint', 5, 7.8, [1,2,3])
print(type(tuple1))
print(tuple1)

#user input
username = input("Enter username: ")
print("Username is: " + username)

# Bitwise eg. &, <<, >>, ~, 