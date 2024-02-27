import json

def read_configuration():
    try:
        with open("config.json", "r") as file:
            data = json.load(file)
            if not data:
                print("config.json is empty")
            else:
                print("config.json data: ")
                print(json.dumps(data, indent=4))
    except FileNotFoundError:
        print("config.json doesnt exists")

def write_configuration():
    server_name = input("input the server_name: ")
    server_ip = input("input the server_ip: ")
    server_password = input("input the server_password: ")

    data = { "server_name": server_name or "", "server_ip": server_ip or "", "server_password": server_password or "" }

    with open("config.json", "w") as file:
        json.dump(data, file, indent=4)

    print("data saved successfully into config.json:")
    print(json.dumps(data, indent=4))

def main():

    READ_OPTION = "1"
    WRITE_OPTION = "2"
    EXIT_OPTION = "3"

    while True:
        print("1 - Read config")
        print("2 - Write config")
        print("3 - Exit")
        choosedOption = input("Choose one option: ")
    
        if choosedOption == READ_OPTION:
            read_configuration()
        elif choosedOption == WRITE_OPTION:
            write_configuration()
        elif choosedOption == EXIT_OPTION:
            print("Exiting the program.")
            break
        else:
            print("Invalid choose, please try again")

if __name__ == "__main__":
    main()