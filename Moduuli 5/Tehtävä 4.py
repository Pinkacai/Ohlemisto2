print(" ")
print("Enter the names of five cities: ")
print(" ")
lst = []

for cities in range(0,5):
    inp = input("Please enter the name of a city: ")
    lst.append(inp)

print(" ")
print("You entered:")
for n in lst:
    print(n)


