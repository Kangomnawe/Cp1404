items = int(input("Enter number of items: "))
total_price = 0
for i in range(items):
    price = float(input("Enter the price of items: "))
    total_price += price

if total_price >= 100:
    discount_price = total_price * 10 / 100
    final_price = total_price - discount_price

print("Total price of {} items is: ${:.2f}".format(items, final_price))


