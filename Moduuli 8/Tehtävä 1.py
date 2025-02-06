import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='eliell2',
         password='gr0ups',
         autocommit=True
         )

def airport_info(icao):
    sql = f"SELECT name FROM airport WHERE ident='{icao}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount >0 :
        for row in result:
            print(f"The name of the airport is: {row[0]} ")
    else:
        print("The airport code you entered could not be found.")
    return

airport_code = input("Please enter the ICAO code of the airport you wish to see: ")
airport_info(airport_code)



