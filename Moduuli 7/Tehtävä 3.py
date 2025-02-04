airports = {}
command = int(input("Please choose one."
                "\n1. Enter a new airport."
                "\n5. Fetch an existing airport name."
                "\n9. quit."
                "\nEnter a command: "))
print("--------------------------------------------------")
while int(command in range(1,9)):
    if command == 1:
        icao = input("Please enter the ICAO code of the airport you wish to enter: ")
        airport = input("Please enter the name of the airport you wish to enter: ")
        airports[icao] = airport
        print("--------------------------------------------------")
        command = int(input("Please choose one."
                "\n1. Enter a new airport."
                "\n5. Fetch an existing airport name."
                "\n9. quit."
                "\nEnter a command: "))
    if command == 5 :
        icao = input("Please enter the ICAO code of the airport you wish to see: ")
        if icao in airports:
            print("")
            print(f"{icao} is the airport code for {airports[icao]}")
            print("--------------------------------------------------")
            command = int(input("Please choose one."
                        "\n1. Enter a new airport."
                        "\n5. Fetch an existing airport name."
                        "\n9. quit."
                        "\nEnter a command: "))
        if icao not in airports:
            print(" ")
            print("ICAO code not found. please try again.")
            print("--------------------------------------------------")
            command = int(input("Please choose one."
                        "\n1. Enter a new airport."
                        "\n5. Fetch an existing airport name."
                        "\n9. quit."
                        "\nEnter a command: "))
        if command == 9:
            quit()

