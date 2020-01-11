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
        if len(client_list) != 0:
            for client in client_list:
                print(client.firstname)
        elif len(client_list) == 0:
            print("\nThere are no clients in the database.\n")
    elif current_command == 'delete':
        clientfound = False
        answer = input("Enter the first and last name of the client you wish to delete: ").lower().split()
        for client in client_list:
            if (client.firstname.lower() == answer[0]) and (client.lastname.lower() == answer[1]):
                print(" \n" + client.firstname + " " + client.lastname)
                answer = input("\n Is this the client you wish to delete? (y/n)  ").lower()
                if answer == "y":
                    clientfound = True
                    client_list.remove(client)
                    print("\n" + client.firstname + " " + client.lastname + " was successfully removed. \n")
        if not clientfound:
            print("\nClient not found. \n")

    elif current_command == 'modify':
        clientfound = False
        answer = input("Enter the first and last name of the client you wish to modify: ").lower().split()
        for client in client_list:
            if (client.firstname.lower() == answer[0]) and (client.lastname.lower() == answer[1]):
                print(" \n" + client.firstname + " " + client.lastname)
                answer = input("\n Is this the client you wish to modify (y/n)  ").lower()
                if answer == "y":
                    clientfound = True
                    answer = input("What would you like to edit? \n Your choices are: First Name, Last Name, Address, Phone Number, Email").lower()


                    if answer == "first name":
                        change = input("Enter new first name: ")
                        client.firstname = change
                    elif answer == "last name":
                        change = input("Enter new last name: ")
                        client.lastname = change
                    elif answer == "address":
                        change = input("Enter new address: ")
                        client.address = change
                    elif answer == "phone number":
                        change = input("Enter new phone number: " )
                        client.phone = change
                    elif answer == "email":
                        change = input("Enter new email: ")
                        client.email = change


        if clientfound == False:
            print("\nClient not found. \n")


    elif current_command == 'menu':
        menu()
    elif current_command == "exit":
        print("\nThanks! Come again!")
        break 




