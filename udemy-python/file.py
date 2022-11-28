file = open("text.txt", "r")
x = file.read()
print(x)

#writting
#file = open("text.txt", "w")
#file.write("pink\n")
#file.close()
file = open("text.txt", "w")
x= ['red', 'greern', 'purpose']
for item in x:
    file.write(item + "\n" )

file.close()

#Appending
file = open("text.txt", "a")
file.write("pnk")
file.close()