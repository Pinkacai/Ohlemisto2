#import math

#min()
#max()
print(" ")
print("Please enter numbers as you please. To quit, enter an empty string. ")
print(" ")




big = small = 0
while True:
    nums = input("Enter a number: ")
    if nums == "":
        print(f"The biggest number you entered was {big} and the smallest was {small}.")
        break
    else:
        if big == 0:
            big = nums
        if small == 0:
            small = nums
        if nums < small:
            small = nums
        if nums > big:
            big = nums



