
lst = []

def sum(nums):
        outcome = 0
        for n in nums:
            outcome = outcome + n
        return outcome

inp = input("Enter a number or enter an empty string to quit: ")
while inp != "":
    inp2 = int(inp)
    lst.append(inp2)
    inp = input("Enter a number or enter an empty string to quit: ")

print(" ")
num2 = sum(lst)
print(f"The sum of the numbers you entered is {num2}")






