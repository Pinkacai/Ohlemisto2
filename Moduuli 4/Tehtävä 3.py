print(" ")
print("Please enter numbers as you please. To quit, enter an empty string. ")
print(" ")

big = None
small = None

while True:
    nums = input("Enter a number: ")
    if nums == "":
        print(f"The biggest number you entered was {big} and the smallest was {small}.")
        break
    else:
        num = float(nums)
        if big is None or num > big:
            big = num
        if small is None or num < small:
            small = num



