import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port= 3306,
    database='flight_game',
    user='nalle',
    password='sup3rS!!st1',
    autocommit=True
)

icao_code = input("Enter the ICAO code of an airport: ").upper()
sql = f'SELECT name, municipality FROM airport WHERE ident = %s'

cursor = connection.cursor()
cursor.execute(sql, (icao_code,))
result = cursor.fetchall()

if not result:
    print(f"No airport found with ICAO code {icao_code}")
else:
    for row in result:
        print(f"Airport name: {row[0]}")
        print(f"Location: {row[1]}")