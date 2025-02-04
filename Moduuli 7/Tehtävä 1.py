print(" ")
months = ("January","February","March","April","May","June",
          "July","August","September","October","November","December")
seasons = ("Winter","Spring","Summer","Fall")

userinp = int(input("Please enter the number of a month, between 1-12: "))

num = userinp-1
while userinp-1 <= 11:
    if userinp-1 == 11 or userinp-1 == 0 or userinp-1 == 1:
        num = seasons[0]
        break
    elif userinp-1 == 2 or userinp-1 == 3 or userinp-1 == 4:
        num = seasons[1]
        break
    elif userinp-1 == 5 or userinp-1 == 6 or userinp-1 == 7:
        num = seasons[2]
        break
    elif userinp-1 == 8 or userinp-1 == 9 or userinp-1 == 10:
        num = seasons[3]
        break

print(f"The month of {months[userinp-1]} is {num}")





