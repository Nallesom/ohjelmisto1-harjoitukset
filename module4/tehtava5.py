attempts = 0
while attempts < 5:
    attempts += 1
    username = input("Enter username: ")
    password = input("Enter password: ")
    if (username == "python") & (password == "rules"):
        print("Welcome")
        break
    elif attempts >= 5:
        print("Access denied")
    else:
        print("Incorrect username or password. Please try again.")