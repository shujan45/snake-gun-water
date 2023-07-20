#  <<<<<<<<<<------------------Snake, water or Gun Game-------------------------->>>>>>>>>>>>>


import random # this is used when we want to let the computer display randomly from the input ypu have provided

def game(comp, b):
    if comp == b:
        return None
    if comp == 's':
        if b=='w':
            return False
        elif b=='g':
            return True
    elif comp == 'w':
        if b=='g':
            return False
        elif b=='s':
            return True
    elif comp == 'g':
        if b=='s':
            return False
        elif b=='w':
            return True


print("Comp Turn: Snake(s) Water(w) or Gun(g)?")
randomno=random.randint(1, 3)
if randomno ==1:
    comp='s'
elif randomno ==2:
    comp='w'
elif randomno==3:
    comp='g'
print(comp)
b= input("Player's Turn: Snake(s) Water(w) or Gun(g)?")

a = game(comp , b)
if a== None:
    print("Game is tie")
elif a==True:
    print("you win")
else:
    print("you lose")