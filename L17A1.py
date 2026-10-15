import random

playing = True
number = str(random.randint(0, 9))

print("I will print a number from 1 to 9 try o figure out the number! :)")

while playing:
    guess = input("enter your guess \n")
    if guess == number:
        print("you win the game! :):):):)")
        print("play again later")
        break
    else:
        print("oops! wrong guess try again")