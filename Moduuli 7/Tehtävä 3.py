airports = {}
command = int(input("Please choose one."
                "\n1. Enter a new airport."
                "\n5. Fetch an existing airport name."
                "\n9. quit."
                "\nEnter a command: "))
print("--------------------------------------------------")

while command == 1:
    icao = input("Please enter the ICAO code of the airport you wish to enter: ")
    airport = input("Please enter the name of the airport you wish to enter: ")
    airports[icao] = airport
    command = int(input("Please choose one."
                "\n1. Enter a new airport."
                "\n5. Fetch an existing airport name."
                "\n9. quit."
                "\nEnter a command: "))
    print("--------------------------------------------------")
while command == 5:
    icao = input("Please enter the ICAO code of the airport you wish to see: ")
    if icao in airports:
        print(f"{icao} is the airport code for {airport[icao]}")
    command = int(input("Please choose one."
                        "\n1. Enter a new airport."
                        "\n5. Fetch an existing airport name."
                        "\n9. quit."
                        "\nEnter a command: "))
    print("--------------------------------------------------")
while command == 9:
    print(airports)
    quit()





print(airports)