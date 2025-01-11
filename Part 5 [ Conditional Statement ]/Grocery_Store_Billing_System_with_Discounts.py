num_items = int(input("Enter the number of item purchased="))
total_price = 0

for i in range(num_items):
    price = float(input("Enter the price of the item="))
    total_price = total_price + price
    i = i + 1
if total_price >= 100:
    discount = 0.1 * total_price
elif 50 <= total_price < 100:
    discount = 0.5 * total_price
else:
    discount = 0

total_bill = total_price - discount
print("Subtotal ", total_bill)
