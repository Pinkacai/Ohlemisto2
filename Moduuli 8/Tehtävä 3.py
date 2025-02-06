import mysql.connector
from geopy import distance

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='eliell2',
         password='gr0ups',
         autocommit=True
         )

def distances(icao1,icao2):
    sql1 = f" select name,latitude_deg,longitude_deg from airport where ident ='{icao1}' "
    sql2 = f" select name,latitude_deg,longitude_deg from airport where ident = '{icao2}' "

    cursor = connection.cursor()

    cursor.execute(sql1)
    result1 = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result1:
            print(" ")
            print(f"The first ICAO code you entered is for the airport: {row[0]}")
            location1 = row[1],row[2]


    cursor.execute(sql2)
    result2 = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result2:
            print(f"The second ICAO code you entered is for the airport: {row[0]}")
            location2 = row[1],row[2]
    print(" ")
    print(f"The distance between the two airports is: {distance.distance(location1,location2).km:.0f}km.")
    return





icao1 = input("Please enter the ICAO code for the first country: ").upper()
icao2 = input("Please enter the ICAO code for the second country: ").upper()
distances(icao1,icao2)