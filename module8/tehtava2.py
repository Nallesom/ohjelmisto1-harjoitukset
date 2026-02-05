import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='nalle',
    password='sup3rS!!st1',
    autocommit=True
)

def get_airports_by_country(country_code):
    cursor = connection.cursor()
    sql = f'SELECT DISTINCT type, COUNT(type) FROM airport WHERE iso_country = %s GROUP BY type ORDER BY type DESC;'
    cursor.execute(sql, (country_code,))
    result = cursor.fetchall()
    return result

def run_country_program():
    country_code = input("Enter the country code (e.g., FI for Finland): ").upper()
    result = get_airports_by_country(country_code)

    if len(result) == 0:
        print(f"No airports found for country code '{country_code}'.")
        return

    print(f"\n\nAirports in {country_code}:")
    for airport in result:
        if airport[0] == "closed":
            continue
        print(f"{airport[1]} {airport[0]} airports")

run_country_program()