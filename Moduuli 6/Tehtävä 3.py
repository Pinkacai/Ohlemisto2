print(" ")
def gallons(amt):
    litres = amt * 4.54609
    if amt < 0:
        print("The amount you entered was negative. Goodbye")
        quit()
    else:
        print(f"{amt:.2f} gallons is:{litres: .2f} litres.")
        print(" ")
    return litres
amt = float(input("How many gallons would you like to convert to litres?: "))
gallons(amt)
print(" ")
while amt > 0:
    amt = float(input("How many gallons would you like to convert to litres?: "))
    gallons(amt)
    print(" ")
else:
    quit()

