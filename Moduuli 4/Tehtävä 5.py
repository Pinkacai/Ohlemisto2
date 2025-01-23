
uname = input("Please enter your username: ")
pword = input("Please input your password: ")
right1 = "python"
right2 = "rules"
tries = 1
while tries < 5:
        if uname == right1 and pword == right2:
                print("")
                print("Welcome")
                break
        if uname != right1 or pword != right2:
                tries = tries + 1
                print("")
                print(f"That's incorrect. You have {6-tries} tries left." )
                uname = input("Please enter your username: ")
                pword = input("Please input your password: ")
        if tries == 5:
            print(" ")
            print("Access denied")









