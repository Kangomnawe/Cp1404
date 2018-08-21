sales = float(input("Enter sales: $"))

if sales < 1000:
    bonus = sales * 10 / 100
    print(bonus)
elif sales >= 1000:
    bonus = sales * 15 / 100

print(bonus)
