print(" ")
print("This program will tell you if the year you input is a leap year")
year = int(input("Please enter a year: "))
print(" ")
d_4 = year%4
d_100 = year%100 == 0
d_400 = year%400 == 0
if d_4 == 0 and d_100 == d_400 :
    print(str(year) + " is a leap year! ")
else:
    print(str(year) + " is not a leap year")