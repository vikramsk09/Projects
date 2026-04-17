contacts = {}

while True:
    print("\n------Contact Management------")
    print("1. Add Contact")
    print("2. Update Contact")
    print("3. Remove Contact")
    print("4. Search Contact")
    print("5. Display all Contacts")
    print("6. Exit")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        name = input("Enter your name: ").title()
        number = input("Enter your number: ")
        contacts[name] = number
        print(f"\nContact '{name}' has been added successfully!!\n")

    elif choice == 2:
        name = input("Enter your name: ").title()
        if name in contacts:
            number = input("Enter your number: ")
            contacts[name] = number
            print(f"\nContact '{name}' has been updated successfully!!\n")
        else:
            print(f"\nContact '{name}' not found!\n")

    elif choice == 3:
        name = input("Enter your name: ").title()
        if name in contacts:
            contacts.pop(f"{name}")
            print(f"\nContact '{name}' has been removed successfully!!\n")
        else:
            print(f"\nContact '{name}' not found!\n")

    elif choice == 4:
        name = input("Enter contact name to search: ").title()
        if name in contacts:
            print(f"\n{name} : {contacts[name]}\n")
        else:
            print(f"\nContact '{name}' not found!\n")

    elif choice == 5:
        if contacts:
            print("\nAll Contacts:")
            for key, value in contacts.items():
                print(f"{key} : {value}")
        else:
            print("\nNo contacts available.\n")

    elif choice == 6:
        print("\nGood bye!!\n")
        break

    else:
        print("\nInvalid choice. Please choose a valid number.\n")

