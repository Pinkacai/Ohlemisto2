

print("This program will tell you if a number you input is a prime number")
print(" ")
numlst = []
num = input("Please enter a number: ")
num2 = int(num)
num3 = float(num)
print(" ")

for n in range(1,num2+1):
    numlst.append(n)

numlst.remove(1)
numlst.remove(num2)

for n in numlst:
    if num2%n == 0:
        print(f"{num} is not a prime number.")
        break
    else:
        print(f"{num} is a prime number!")
        break









