import mysql.connector
from geopy import distance

def get_airport_coordinates(icao_code):
    connection = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='nalle',
        password='sup3rS!!st1',
        autocommit=True
    )
    cursor = connection.cursor()
    sql = f'SELECT latitude_deg, longitude_deg FROM airport WHERE ident = "{icao_code}";'
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount == 0:
        return 0
    for i in result:
        return i

def run_airport_distance():
    first_icao = input("Enter the ICAO code of the first airport: ").upper()
    second_icao = input("Enter the ICAO code of the second airport: ").upper()

    first_coords = get_airport_coordinates(first_icao)
    second_coords = get_airport_coordinates(second_icao)

    if first_coords == 0:
        print(f"Airport with ICAO code {first_icao} not found in the database.")
        return
    elif second_coords == 0:
        print(f"Airport with ICAO code {second_icao} not found in the database.")
        return

    airport_distance = distance.geodesic(first_coords, second_coords)
    print(f"Distance between {first_icao} and {second_icao}: {airport_distance.km:.2f} kilometers")

run_airport_distance()