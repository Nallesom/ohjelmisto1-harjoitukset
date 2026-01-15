kuhan_pituus = float(input("Enter the length of the zander in centimeters: "))
if kuhan_pituus < 42:
    print("The zander does not meet the size limit.")
    print("Please release the fish back into the lake.")
    puuttuvat_sentit = 42.0 - kuhan_pituus
    print(f"The fish was {puuttuvat_sentit:.1f} centimeters below the size limit.")
else:
    print("The zander meets the size limit.")