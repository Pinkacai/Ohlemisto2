print(" ")
print("This program will tell you if the year you input is a gap year")
print(" ")
year = int(input("Please enter a year: "))
d_4 = year%4
d_100 = year%100
d_400 = year%400
if d_4 == 0 or d_100 == 0 and d_400 == 0:
    print(str(year) + " is a gap year! ")
else:
    print(str(year) + " is not a gap year")