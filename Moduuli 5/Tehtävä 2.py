num = []
numbers = input("Please enter a number or enter an empty string to quit: ")
while numbers != "":
    numbers2 = int(numbers)
    num.append(numbers2)
    numbers = input("Please enter a number or enter an empty string to quit: ")


num.sort(reverse=True)
for index in range(0,5):
    print(num[index])
