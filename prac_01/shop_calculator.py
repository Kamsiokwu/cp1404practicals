num_items = int(input("Number of items bought: "))
while num_items < 0:
    print("Invalid items!")
    num_items = int(input("Number of items: "))

total_price = 0
for i in range(num_items):
    price = float(input(f"Price of item {i + 1}: "))

# Check for discount
if total_price > 100:
    total_price *= 0.90
print(f"Total price for {num_items} items is ${total_price}")