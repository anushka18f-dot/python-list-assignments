#Assignment 1

foods = ["Rice", "Kottu", "Noodles", "Pizza,", "Burger"]
foods_Count = len(foods)
first = foods[0]
last = foods[-1]

print("="*32)
print(f'{"FAVOURITE FOODS":^32}')
print("="*32+ "\n")

print(f'{"First Food: ":<16}{first}')
print(f'{"Last Food: ":<16}{last}')
print(f'{"Total Foods: ":<16}{foods_Count}')
print(f'{"All Foods: ":<16}{foods}')

print("="*32+ "\n")