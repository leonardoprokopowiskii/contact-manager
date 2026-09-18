def add_contact(contacts, contact_name, contact_phone, contact_email):
    contact = {
        "name": contact_name,
        "phone": contact_phone,
        "email": contact_email,
        "favorite": False,
    }
    contacts.append(contact)
    print(f"\nContact '{contact_name}' added successfully!")


def view_contacts(contacts):
    print("\n--- List of contacts ---")
    for index, contact in enumerate(contacts, start=1):
        status = "★" if contact["favorite"] else " "
        print(f"{index}. [{status}] {contact["name"]} - {contact["phone"]} - {contact["email"]}")

    
def view_edit_options():
    print("\n--- Options to edit ---")
    print("1. Edit the contact name")
    print("2. Edit the contact phone")
    print("3. Edit the contact email")
    print("4. Back to menu")


def edit_contact(contacts, contact_index):
    adjusted_contact_index = int(contact_index) - 1

    if adjusted_contact_index >= 0 and adjusted_contact_index < len(contacts):
        view_edit_options()
        choice_to_edit = input("\nEnter your choice: ")
        if choice_to_edit == "1":
            contacts[adjusted_contact_index]["name"] = input("Enter the new name of contact: ")
        elif choice_to_edit == "2":
            contacts[adjusted_contact_index]["phone"] = input("Enter the new phone of contact: ")
        elif choice_to_edit == "3":
            contacts[adjusted_contact_index]["email"] = input("Enter the new email of contact: ")
        elif choice_to_edit == "4":
            print("\nReturning to menu...")
            return
        else:
            print("\nInvalid choice! Returning to menu...")
            return
        print("\nThe contact has been successfully edited!")
    else:
        print("\nThe index entered is invalid!")


def toggle_favorite(contacts, contact_index):
    adjusted_contact_index = int(contact_index) - 1
    if adjusted_contact_index >= 0 and adjusted_contact_index < len(contacts):
        if contacts[adjusted_contact_index]["favorite"]:
            contacts[adjusted_contact_index]["favorite"] = False
            print("The contact was unmarked favorite successfully!")
        else:
            contacts[adjusted_contact_index]["favorite"] = True
            print("The contact was marked favorite successfully!")
    else:
        print("\nThe index entered is invalid!")


def view_favorite_contacts(contacts):
    favorite_count = 0
    print("\n--- Favorite contacts list ---")
    for index, contact in enumerate(contacts, start=1):
        if contact["favorite"]:
            favorite_count += 1
            print(f"{index}. [★] {contact["name"]} - {contact["phone"]} - {contact["email"]}")
    if favorite_count == 0:
        print("No favorite contacts found!")


contacts = []

while True:
    print("\n----- Contacts manager -----")
    print("1. Add a contact")
    print("2. View contacts")
    print("3. Edit a contact")
    print("4. Mark or unmark contact as favorite")
    print("5. View contacts marked as favorite")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        contact_name = input("Enter the name of contact: ")
        contact_phone = input("Enter the phone of contact: ")
        contact_email = input("Enter the email of contact: ")
        add_contact(contacts, contact_name, contact_phone, contact_email)
    elif choice == "2":
        view_contacts(contacts)
    elif choice == "3":
        view_contacts(contacts)
        contact_index = input("\nEnter the index of the contact you want to edit: ")
        edit_contact(contacts, contact_index)
    elif choice == "4":
        view_contacts(contacts)
        contact_index = input("\nEnter the index of the contact you want to mark/unmark as a favorite: ")
        toggle_favorite(contacts, contact_index)
    elif choice == "5":
        view_favorite_contacts(contacts)
    elif choice == "6":
        break

print("Finish program!")
