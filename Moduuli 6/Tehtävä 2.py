import random
main_num = 0

def rolls(sides):
    ran = random.randint(1, sides)
    return ran
sides = int(input("How many sides would you like your dice to have?: "))
while main_num != int(sides):
    main_num = rolls(sides)
    print(f"You threw a {main_num}!")
else:
    print(f"You did it! You threw the biggest number in your dice with {sides} sides!")