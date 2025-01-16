print(" ")
print("Hello! This program will give the sum, multiplication and average of any three whole numbers you give me. ")
print("      ")
num1 = float(input("Please input the first number: "))
num2 = float(input("Please input the second number: "))
num3 = float(input("Please input the third and final number: "))

sum = (num1) + (num2) + (num3)
mult = (num1)*(num2)*(num3)
avrg = (sum)/3

print(f"The sum of your numbers is: {sum:2.0f}")
print(f"The multiplication of your numbers is: {mult:2.0f}")
print(f"The average of your numbers is: {avrg:2.0f}")

