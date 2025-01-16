import math
Radius_str = float(input("What is the radius of the circle?: "))
R = float(Radius_str)
Pi = float(math.pi)
Area = float(Pi*(R**2))
print (f"The area is: {Area: .3f}" )
