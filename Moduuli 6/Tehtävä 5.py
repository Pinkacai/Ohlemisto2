


def dif(nums):
    even = []
    for n in nums:
        if n % 2 == 0:
            even.append(n)
    return even

odd=[]
num = input(" Please enter numbers as you please. To quit, enter an empty string: ")
while num != "":
    num2= int(num)
    odd.append(num2)
    num = input(" Please enter numbers as you please. To quit, enter an empty string: ")
else:
    print(f"The original list was {odd}.")
    num3 = dif(odd)
    print(f"The list with odd numbers removed is {num3}.")



