def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    contacts[name] = phone
    print("Contact added successfully!")
def search_contact(contacts):
    name = input("Enter name to search: ")
    if name in contacts:
        print("Name :", name)
        print("Phone:", contacts[name])
    else:
        print("Contact not found.")
def update_contact(contacts):
    name = input("Enter name to update: ")
    if name in contacts:
        phone = input("Enter new phone number: ")
        contacts[name] = phone
        print("Contact updated successfully!")
    else:
        print("Contact not found.")
def delete_contact(contacts):
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")
def display_contacts(contacts):
    if not contacts:
        print("Phonebook is empty.")
        return
    print("\n--- Contact Directory ---")
    for name, phone in contacts.items():
        print("Name :", name)
        print("Phone:", phone)
def main():
    contacts = {}
    while True:
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Display All Contacts")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            search_contact(contacts)
        elif choice == "3":
            update_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            display_contacts(contacts)
        elif choice == "6":
            print("Exiting Phonebook...")
            break
        else:
            print("Invalid choice!")
main()