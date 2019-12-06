#!/usr/bin/env python3

def display_menu():
    print("COMMAND MENU")
    print("list - Display all contacts")
    print("view - View a contact")
    print("add -  Add a contact")
    print("del -  Delete a contact")
    print("exit - Exit program")
    print()    

def list(contact_list):
    if len(contact_list) == 0:
        
        print("There are no contacts in the list.\n")
        return
    else:
        i = 1
        for contact in contact_list:
            row = contact
            print(str(i) + ". " + row[0])
            i += 1
        print()

def add(contact_list):
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")
    contact = []
    contact.append(name)
    contact.append(email)
    contact.append(phone)
    contact_list.append(contact)
    print(contact[0] + " was added.\n")

def delete(contact_list):
    number = int(input("Number: "))
    if number < 1 or number > len(contact_list):
        print("Invalid contact number.\n")

    else:
        contact = contact_list.pop(number-1)
        print(contact[0] + " was deleted.\n")  

def view(contact_list):
    print("Contact List:", contact_list)
    view_number = int(input("Number: "))

    # Test that input is a valid number
    if view_number < 1 or view_number > len(contact_list):
        print("Invalid contact number. Try again.\n")
    else:
        view_number -= 1
        print("Name:", contact_list[view_number][0])
        print("Email:", contact_list[view_number][1])
        print("Phone:", contact_list[view_number][2])
          
def main():
    contact_list = [["Guido van Rossum", "guidmaster@daboss.net", "805 241 2414"], 
                    ["Eric Idle", "eric@ericidle.com", "+44 20 7946 0958"]]
    display_menu()
    while True:        
        command = input("Command:")
        if command == "list":
            list(contact_list)
        elif command == "add":
            add(contact_list)
        elif command == "del":
            delete(contact_list)
        elif command == "view":
            view(contact_list)
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")

if __name__ == "__main__":
    main()