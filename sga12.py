stock = {
    "rice": 10,
    "sugar": 20,
    "milk": 15,
    "bread": 10
}

bill = []
n = int(input("Enter number of items: "))

for i in range(n):
    item = input("Enter item name: ").lower()
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price per unit: "))

    if item in stock:
        if quantity <= stock[item]:
            bill.append((item, quantity, price))
            stock[item] = stock[item] - quantity
            print("Item added to bill.")

        else:
            print("Insufficient stock.")
    else:
        print("Item not available.")
total = 0

for item, quantity, price in bill:
    total = total + quantity * price

bill.append(("Total", 1, total))

print("\nFinal Bill:")
print(bill)
print("\nUpdated Stock:")
print(stock)
