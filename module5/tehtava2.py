values = []
value = input("Enter a number: ")

while value != "":
    values.append(float(value))
    value = input("Enter a number: ")

values.sort(reverse=True)
print("The greatest numbers in descending order:")

buh = 0
for value in values:
    if buh > 4:
        break
    print(value)
    buh += 1