def div(w, p):
    if(p==0):
        return print("This is not possible")
    else:
        f = w/p
        return print(f)

w = input('Enter any value: ')
p= input('Entrer the second value: ')
div(int(w), int(p))