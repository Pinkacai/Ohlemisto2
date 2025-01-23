import random


rndm = random.randint(1,10)
guess = (int(input("Guess a integer between 1-10: ")))
while True:
    if guess < rndm:
        print("The number you guessed was too low!")
        print("")
        guess = (int(input("Guess a integer between 1-10: ")))
    if guess > rndm:
        print("The number you guessed was too high!")
        print("")
        guess = (int(input("Guess a integer between 1-10: ")))
    if guess == rndm :
        print("That's the number! ")
        break

