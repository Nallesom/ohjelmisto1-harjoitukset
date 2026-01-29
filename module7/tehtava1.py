def get_season(num):
    print(f"You entered: {num}")
    if num < 1 or num > 12:
        print("Please enter a number between 1 and 12.")
        return
    seasons = "winter", "winter", "spring", "spring", "spring", "summer", "summer", "summer", "autumn", "autumn", "autumn", "winter"
    print(f"The season is {seasons[num-1]}.")

monthnum = int(input("Enter the number of a month (1-12): "))
get_season(monthnum)