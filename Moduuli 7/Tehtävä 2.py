names = set()
namesinp = input("Please enter a name, or enter an empty string to quit: ").capitalize()
while namesinp != "":
    if namesinp in names:
        print("Existing name")
    else:
        print("New name")
    names.add(namesinp)
    namesinp = input("Please enter a name, or enter an empty string to quit: ").capitalize()

print(" ")
for n in names:
    print(n)



