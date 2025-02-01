import math
print("")

def pizza_price(diameter,price):
    rad = int(diameter/2)
    area = int(rad**2) * math.pi
    sqm = area /10000
    price_sqm = price / sqm
    return price_sqm
def comparison(price_1,price_2):
    if price_1 < price_2:
        return price_1
    else:
        return price_2

cm = int(input("Please enter the diameter of your first pizza: "))
euros = int(input("Please enter the price of your first pizza: "))
cm2 = int(input("Please enter the diameter of your second pizza: "))
euros2 = int(input("Please enter the price of your second pizza: "))
tot_price1 = pizza_price(cm, euros)
tot_price2 = pizza_price(cm2,euros2)
comp1 = comparison(tot_price1,tot_price2)

if comp1 == tot_price1:
    print(f"The cheaper option is the first pizza you entered, which costs {tot_price1:.2f}€ per square meter.")
else:
    print(f"The cheaper option is the second pizza you entered, which costs {tot_price2:.2f}€ per square meter.")
