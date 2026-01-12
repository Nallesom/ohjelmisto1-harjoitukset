talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))
print(f"The weight in modern units: ")

# One talent is 20 pounds and one pound is 32 lots and a lot is 13,3grams
total_grams = 0.0
# First calculate talents weight
total_grams += talents * 20 * 32 * 13.3
# Then pounds
total_grams += pounds * 32 * 13.3
# Finally lots
total_grams += lots * 13.3

kilograms = int(total_grams / 1000.0)
remaining_grams = total_grams - kilograms * 1000

print(f"{kilograms} kilograms and {remaining_grams:.2f} grams.")