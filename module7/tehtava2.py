name = input()
names = set()
while name != "":
    if names.__contains__(name):
        print("Existing name")
    else:
        print("New name")
        names.add(name)
    name = input()

for temp in names:
    print(temp)