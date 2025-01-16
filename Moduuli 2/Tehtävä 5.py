print(" ")

gram = 1
bul = (gram)*13.3
nail = (bul)*32
lei = (nail)*20

L = float(input("How many leiviskät?: "))
N = float(input("How many nails?: "))
B = float(input("How many bullets?: "))

L2 = (L)*(lei)
N2 = (N)*(nail)
B2 = (B)*(bul)
weight = (L2)+(N2)+(B2)

kg = int(weight)/1000
g = (weight)%1000


print(" ")
print(f"The equivalent weight in kilograms and grams is: {kg:0.0f}" "kg and " + (f"{g:0.3f}" "g."))


