wholevalue = int(input("Enter an integer: "))

foundnums = 0
if (wholevalue < 2):
    foundnums += 1

for value in range(2, wholevalue):
    if (wholevalue % value == 0):
        foundnums += 1

if (foundnums > 0):
    print(f"{wholevalue} is not a prime number.")
else:
    print(f"{wholevalue} is a prime number.")
