# number guess game

import random

number = random.randint(1,10)

guess = int(input("ENTER YOUR GUESS NUMBER : "))

if guess == number:
    print("CORRECT")
elif guess > number:
    print("TO) HIGH")
elif guess < number:
    print("TOO LOW")

print(number)