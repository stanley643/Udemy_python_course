m = input("Enter the number of minutes: ")
s = input("Enter the number of seconds: ")
h = int(m)/60 + int(s)/3600
print(h)

#converts by functions
def temp(c):
    f=(9/5) * c +32
    return print(f)

c = input("Writre the tempersature in cel: ")
c = int(c)
temp(c)