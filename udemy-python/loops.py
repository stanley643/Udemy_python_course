# for loop

x = [1,2,3,4,5,6,7,8,9,10]
y = ['Red', 'Blue', 'Green']
for item in x:
    print(item)

for a in y:
    print(a)

#loops and user input
#or i in x:
 #   x[i] = input('Enter your name: ')
print(x)

#while loop
i = 0
while i<60:
    print(i)
    i +=1

#loops in strings
for i in "Stanley":
    print(i)

#Break
for item in x:
    print(item)
    if item == 5:
     break

#continue
for item in x:
    if item == 5:
        continue
    print(item)

#Range () fn
for x in range(5, 100, 3):
    print(x)

#else in for loop
for x in range(10):
    print(x)
else:
    print('Now the seats are full')

#Nested loops
x = ['big', 'small', 'bold', 'heavy']
y = ['iron', 'silver', 'diamond', 'gold']

for i in x:
    for j in y:
        print(i,j)