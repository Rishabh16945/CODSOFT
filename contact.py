print("Contact Book App")

my_contacts = {}

# Menu

while True:
    print("\n*** MAIN MENU")
    print("1. Add Contact")
    print("2. Delete Contact")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. View All Contact")
    print("6. Exit")

    choice = input("Please Choose an option (1/2/3/4/5/6): ")

    if choice == "1":
        name = input("Enter Contact Name: ")
        phone = input("Enter Phone Number: ")
        my_contacts[name] = phone
        print("\nContact Added Sucessfully !")
        
    elif choice == "2":
        name = input("Enter the Contact tha you want to Delete: ")
        if name in my_contacts.keys():
            del(my_contacts[name])
            print("\nContact Deleted Successfully !")

        else:
            print("\nContact Not Found")

    elif choice == "3":
        name = input("Enter the Contact name that you want to Search")
        if name in my_contacts.keys():
            print("\nContact Found !\n Phone Number: ", my_contacts[name])

        else:
            print("\nContact Not Found")

    elif choice == "4":
        name = input("Enter the Contact Name that you want to Update: ")
        if name in my_contacts.keys():
            new_phone = input("Enter the New Phone Number: ")
            my_contacts[name] = new_phone
            print("\nContact Updated Successfully!")

        else:
            print("Contact Not Found")

    elif choice == "5":
        if not my_contacts:
            print("\nNo Contacts to Display !")

        else:
            print("\n---Displaying All Contacts---")
            for name, phone in my_contacts.items():
                print("Contact Name: ", name, "\nPhone Number: ", phone)

    elif choice == "6":
        print("\nExiting the Application...  GOOD BYE !!")
        break

    else:
        print("Invaild Choice ! Please choose from option (1/2/3/4/5/6)!")
        