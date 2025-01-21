print(" ")
print("This program will give you a written description of your cabin class on your upcoming cruise! ")

LUX = "Your room is an upper deck cabin with a balcony"
A = "Your cabin is above the car deck, equipped with a window "
B = "Your cabin is a windowless cabin above the car deck "
C = "Your cabin is a windowless cabin below the car deck "

cabin_class = input("What is the cabin class of your room?: ").upper()
print(" ")
if cabin_class == str("LUX"):
    print(LUX)
    print(" ")
    print("Enjoy your stay in the " + str(cabin_class) + " class cabin")
elif cabin_class == str("A"):
    print(A)
    print(" ")
    print("Enjoy your stay in the " + str(cabin_class) + " class cabin")
elif cabin_class == str("B"):
    print(B)
    print(" ")
    print("Enjoy your stay in the " + str(cabin_class) + " class cabin")
elif cabin_class == str("C"):
    print(C)
    print(" ")
    print("Enjoy your stay in the " + str(cabin_class) + " class cabin")
else:
    print("Invalid cabin class.")





