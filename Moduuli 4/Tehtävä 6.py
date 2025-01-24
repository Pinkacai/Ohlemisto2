import random
n = 0
N = float(input("How many points would you like to use to approximate the value of Pi?: "))
Times = 0

while Times <= N:
    X = random.uniform(-1,1)
    Y = random.uniform(-1, 1)
    if ((X ** 2) + (Y ** 2)) <1:
        n = n + 1
    Times = Times + 1
pi =(4*n)/N
print(pi)








