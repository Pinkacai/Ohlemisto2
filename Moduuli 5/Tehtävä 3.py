

print("This program will tell you if a number you input is a prime number")
print(" ")
numlst = []
num = input("Please enter a number: ")
num2 = int(num)
print(" ")

for n in range(1,num2+1):
    numlst.append(n)
if num2 != 2:
    numlst.remove(1)
    numlst.remove(num2)
else:
    numlst.remove(num2)

if num2 == 2:
    print(f"{num} is a prime number!")
    quit()
is_prime = True
for n in numlst:
        if num2%n == 0:
            is_prime = False
            break

if is_prime:
    print(f"{num} is a prime number!")
else:
    print(f"{num} is not a prime number!")













