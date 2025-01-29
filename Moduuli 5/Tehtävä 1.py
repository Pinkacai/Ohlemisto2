import random

rolls = []
roll = int(input("How many dice would you like to throw?: " ))
outcome = 0
for n in range(0, roll):
    dice = random.randint(1,6)
    rolls.append(dice)

for n in rolls:
    outcome = outcome + n

print(f"The total sum of your {roll} dice thrown is {outcome}")





















