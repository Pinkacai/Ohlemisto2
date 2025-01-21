print(" ")
gender = input("Please input your biological gender: ").lower()
hgv = input("Please input your hemoglobin value(g/l): ")
print(" ")


if gender == str("male") and (float(hgv) >=134) and float(hgv) <= 167:
    print("Your hemoglobin levels are normal!")
elif gender == str("male") and (float(hgv) <= 134):
    print("Your hemoglobin values are low! ")
elif gender == str("male") and (float(hgv) >= 167):
    print("Your hemoglobin values are high!")

elif gender == str("female") and (float(hgv) >=117) and float(hgv) <= 155:
    print("Your hemoglobin levels are normal!")
elif gender == str("female") and (float(hgv) <= 117):
    print("Your hemoglobin values are low! ")
elif gender == str("female") and (float(hgv) >= 155):
    print("Your hemoglobin values are high!")
else:
    print("Your input was invalid. ")

