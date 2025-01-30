import random


main_num = 0

def rolls():
    ran = random.randint(1, 6)
    return ran

while main_num != 6:
    main_num = rolls()
    print(f"You threw a {main_num}!")
else:
    print("You did it! You threw a 6!")






