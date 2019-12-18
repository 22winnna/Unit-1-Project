#!/usr/bin/env python3

def display_menu():
    print("COMMAND MENU")
    print("show - Show all items")
    print("grab - Grab an item")
    print("edit - Edit an item")
    print("drop - Drop an item")
    print("exit - Exit program")
    print()    

def list(Inventory):
    if len(Inventory) == 0:
        print("There are no items in the list.\n")
        return
    else:
        i = 1
        for item in Inventory:
            row = item
            print(str(i) + ". " + row[0])
            i += 1
        print()

def grab(Inventory):
    if len(Inventory) > 3:
        print("You can't carry anymore items. Drop something")
    else:
        name = input("Name: ")
        item = []   
        item.append(name)
        Inventory.append(item)
        print(item[0] + " was added.\n")
    
    
def drop(Inventory):
    number = int(input("Number: "))
    if number < 1 or number > len(Inventory):
        print("Invalid item number.\n")
    else:
        item = Inventory.pop(number-1)
        print(item[0] + " was dropped.\n")

def edit(Inventory):
    number = int(input("Number: "))
    new = []
    new.append(input("Updated name: "))
    print("Item number", (number), "was updated")
    Inventory[number -1] = new



        
def main():
    Inventory = [["wooden staff"],
                  ["wizard hat"],
                  ["cloth shoes"]]
    
    display_menu()
    while True:        
        command = input("Command: ")
        if command == "show":
            list(Inventory)
        elif command == "grab":
            grab(Inventory)
        elif command == "drop":
            drop(Inventory)
        elif command == "edit":
            edit(Inventory)
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")

if __name__ == "__main__":
    main()