def gallons_to_liters(g):
    return g * 3.785


gallons = float(input("Enter a volume in American gallons (negative value to quit): "))
while gallons > 0:
    print(f"{gallons} American gallons is {gallons_to_liters(gallons):.2f} liters.")
    gallons = float(input("Enter a volume in American gallons (negative value to quit): "))

print("Program finished.")