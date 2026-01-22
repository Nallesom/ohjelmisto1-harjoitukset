cities = []

for index in range(1,6):
    city = input("Enter the name of a city: ")
    cities.insert(index, city)

print("\n\nThe cities you entered:")

for value in cities:
    print(value)