print(" ")

fish_size = float(input("What is the length of the Zander you caught, in centimeters?: "))
size_dif = 42-fish_size

print(" ")

if fish_size <= 42:
    print("You should release the fish back to the lake, it is " + str(size_dif) + "cm too small.")
else:
    print("That's a great catch!")
