import math

def calculate_unit_price(diameter, price):
    diameterinmeter = diameter / 100
    radius = diameterinmeter / 2
    area = math.pi * radius ** 2
    return price / area

first_size = float(input("Enter the diameter of the first pizza (cm): "))
first_price = float(input("Enter the price of the first pizza (euros): "))
second_size = float(input("Enter the diameter of the second pizza (cm): "))
second_price = float(input("Enter the price of the second pizza (euros): "))

first_pizza = calculate_unit_price(first_size, first_price)
second_pizza = calculate_unit_price(second_size, second_price)

print(f"Unit price of the first pizza: {first_pizza:.2f} euros/m²")
print(f"Unit price of the second pizza: {second_pizza:.2f} euros/m²")

if first_pizza < second_pizza:
    print("The first pizza provides better value for money.")
else:
    print("The second pizza provides better value for money.")