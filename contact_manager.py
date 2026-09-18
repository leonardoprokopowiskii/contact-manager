def add_contact(contacts, contact_name, contact_phone, contact_email):
    contact = {
        "name": contact_name,
        "phone": contact_phone,
        "email": contact_email,
        "favorite": False,
    }
    contacts.append(contact)
    print(f"\nContact '{contact_name}' added successfully!")

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
    elif choice == "6":
        break

print("Finish program!")
