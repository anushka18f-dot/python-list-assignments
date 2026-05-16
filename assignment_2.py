#Assignment 2

cart = []

cart.append("Rice")
cart.append("Suger")
cart.append("Tea")

cart.insert(1, "Milk")

cart.remove("Suger")

count = len(cart)

print("="*32)
print(f'{"SHOPING CART":^32}')
print("="*32)

print(f'{"Cart Items: ":<15}{cart}')
print(f'{"Total Items: ":<15}{count}')
print("="*32+ "\n")