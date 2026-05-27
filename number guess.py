# number guess game

import random

target = random.randint(1,100)

while True:
    Userchoice = input("Guess Your Choice Number or Quit(Q) : ")
    if(Userchoice == "Q"):
        break

    Userchoice = int(Userchoice)
    if(Userchoice == target):
        print("Success : Correct Guess😎!!")
        break
    elif(Userchoice < target):
        print("Your Number Was Too Small👎🏻. Take a Bigger Guess...")
    else:
        print("Your Number Was Too High😨. Take a Smaller Guess...")



print("-----👾GAME OVER👾-----")

