#This program is for handling a client list



class client:
    def __init__(self, firstname, lastname, address, phone, email):
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.phone = phone
        self.email = email

def menu():
    print("\n\nWelcome to Real Estate Client Manager V1.0")
    print("Please pay attention, as our menu options have changed.\n")
    print("-----------Menu Options---------")
    print("List    Add     Delete     Modify\n")
    print("Enter 'Menu' at any time to return to the main menu")
    print("Enter 'Exit' at any time to quit the program\n")


#def delete():

#def modify():

client_list = []
current_client = []

current_command = " "
menu()

while True:
    current_command = input("Enter command:  ").lower()

    if current_command == 'add':
        answer = "n"
        while answer != "y":
            firstname = input("First Name: ")
            lastname = input("Last Name: ")
            address = input("Address: ")
            phone = input("Phone Number: ")
            email = input("Email: ")
            print("Is this information correct?\n")
            print(firstname + " " + lastname + "\n" + address + "\n" + phone + "\n" + email + "\n")
            answer = input("y/n  ").lower()
        new_client = client(firstname, lastname, address, phone, email)
        client_list.append(new_client)
    elif current_command == "list":
        for client in client_list:
            print(client.firstname)
    elif current_command == 'delete':
        answer = input("Enter the first and last name of the client you wish to delete: ").split()
        for client in client_list:
            if (client.firstname == answer[0]) and (client.lastname == answer[1]):
                print(client.firstname + " " + client.lastname)
                answer = input("Is this the client you wish to delete? (y/n)").lower()
                if answer == "y":
                    client_list.remove(client)
                el

    elif current_command == 'modify':
        modify()
    elif current_command == 'menu':
        menu()
    elif current_command == "exit":
        print("\nThanks! Come again!")
        break 




