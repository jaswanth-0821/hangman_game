import random
import json


def fill(x, xx, z):
    z = z.split()
    xx = list(xx)
    x = list(x)
    if(len(xx) >= len(x)):
        for i in range(len(x)):
            if(xx[i] == x[i]):
                z[i] = x[i]
    else:
        for i in range(len(xx)):
            if(xx[i] == x[i]):
                z[i] = x[i]
    z = " ".join(z)
    return z


f = open("dictionary.json")
data = json.load(f)

x, y = random.choice(list(data.items()))
z = list(x)
for i in range(len(x)):
    if((i != 0) and (i != (len(x) - 1))):
        z[i] = " _ "

z = "".join(z)
print(x, z)
for i in range(3):
    print(f'you have {3-i} chances only')
    print("")
    xx = input("enter your guess: ",)
    if xx == x:
        print("congrats your guess is right")
        print("")
        break
    else:
        if(i == 2):

            print("sorry your guess is wrong")
            print("")
            print("you last all your chances. The majic word is ")

            print(f'{x}')
            print(f'{x} means : {y}')
        else:
            z = fill(x, xx, z)
            print(z)
            print("sorry your guess is wrong")
            print("")

print(f'if you want to try again please press "PLAY AGAIN"')
f.close()
