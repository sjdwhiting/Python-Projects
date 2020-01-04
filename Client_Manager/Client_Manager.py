#This program is for handling real estate client lists

def Menu():
    print("Welcome to Real Estate Client Manager V1.0")
    print("Please pay attention, as our menu options have changed.\n")
    print("-------Menu Options-------")
    print("Add     Delete     Modify\n")
    print("Enter 'Menu' at any time to return to the main menu")
    print("Enter 'Exit' at any time to quite the program")

def add():

def delete():

def modify():

client_list = []
current_client = []

current_command = " "
Menu()
while True:
    current_command = input("Enter command:  ").lower()

    if current_command == 'add':
        add()
    elif current_command == 'delete':
        delete()
    elif current_command == 'modify':
        modify()
    elif current_command == 'menu':
        menu()
    elif current_command == "exit":
        break




