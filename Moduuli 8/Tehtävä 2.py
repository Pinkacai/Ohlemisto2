import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='eliell2',
         password='gr0ups',
         autocommit=True
         )

def airport_info(country_code):
    sql = f"SELECT type,count(*) FROM airport WHERE iso_country ='{country_code}' group by type desc"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount >0 :
        print(" ")
        print(f"The airports in the country you entered are: ")
        for row in result:
            print(row)

    else:
        print("The country code you entered could not be found.")
    return

airport_iso_code = input("Please enter the country code of the country: ").upper()
airport_info(airport_iso_code)