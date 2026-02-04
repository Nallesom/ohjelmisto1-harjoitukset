import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='nalle',
         password='sup3rS!!st1',
         autocommit=True
         )

icao_code = input("Enter the ICAO code of an airport: ").upper()
sql = f'SELECT name, municipality FROM airport WHERE ident = "{icao_code}"'
kursori = yhteys.cursor()
kursori.execute(sql)
tulos = kursori.fetchall()

if kursori.rowcount == 1:
    for rivi in tulos:
        print(f"Airport name: {rivi[0]}")
        print(f"Location: {rivi[1]}")
else:
    print(f"No airport found with ICAO code {icao_code}")