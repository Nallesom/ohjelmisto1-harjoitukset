lukustr = input("Enter a number (or press Enter to quit): ")
smallest_number = float(lukustr)
largest_number = float(lukustr)

while lukustr != "":
    lukustr = input("Enter a number (or press Enter to quit): ")
    if lukustr == "":
        break
    luku = int(lukustr)
    if luku < smallest_number:
        smallest_number = luku
    if luku > largest_number:
        largest_number = luku

print(f"Smallest number: {smallest_number:.1f}\nLargest number: {largest_number:.1f}")

