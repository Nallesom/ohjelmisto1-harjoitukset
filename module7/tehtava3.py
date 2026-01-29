def printmenu():
    print("\nAirport Data Management\n"
        + "1. Enter a new airport\n"
        + "2. Fetch airport information\n"
        + "3. Quit")

def add_airport():
    icao_code = input("Enter the ICAO code: ")
    airport_name = input("Enter the airport name: ")
    airports[icao_code] = airport_name
    print(f"Airport {airports[icao_code]} with ICAO code {icao_code} has been added.")

def fetch_airport():
    icao_code = input("Enter the ICAO code: ")
    if icao_code in airports:
        print(f"The airport with ICAO code {icao_code} is {airports[icao_code]}.")
    else:
        print(f"No airport found with ICAO code {icao_code}.")

airports = {}
printmenu()
action = input("Please choose an option (1-3): ")
while action != "3":
    if action == "1":
        add_airport()
    elif action == "2":
        fetch_airport()
    printmenu()
    action = input("Please choose an option (1-3): ")

print("Thank you for using the Airport Data Management system. Goodbye!")