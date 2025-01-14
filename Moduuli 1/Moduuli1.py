#User = input("What's your name?: ")
#print("Nice to meet you,  " + User + "!")
import math

#Fahrenheit_str = input("Enter temperature in fahrenheit: ")
#Fahrenheit = float(Fahrenheit_str)
#Celcius = (Fahrenheit - 32)*5/9
#print (f"The degrees in celcius are: {Celcius:.2f}")

#<20s : a string printed into a field of 20 characters wide, justified to the left
#8d : an integer into a field of 8 characters wide
#WHAT???????^

Radius_str = float(input("What is the radius of the circle?: "))
R = float(Radius_str)
Pi = float(math.pi)
Area = float(Pi*(R**2))
print ("The area is: " + str(Area))
