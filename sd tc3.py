CONTACT_FILE = "contacts.txt"

# Load contacts from file (returns list of dicts)
def load_contacts():
    contacts = []
    try:
        with open(CONTACT_FILE, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    contacts.append({"name": parts[0], "phone": parts[1], "email": parts[2]})
    except FileNotFoundError:
        pass  # File doesn't exist yet
    return contacts

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACT_FILE, "w") as file:
        for contact in contacts:
            line = f"{contact['name']},{contact['phone']},{contact['email']}\n"
            file.write(line)

# Add a new contact
def add_contact(contacts):
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email Address: ")
    contacts.append({"name": name, "phone": phone, "email": email})
    print("Contact added successfully!")

# View all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        for i, contact in enumerate(contacts):
            print(f"{i + 1}. {contact['name']} - {contact['phone']} - {contact['email']}")

# Edit a contact
def edit_contact(contacts):
    view_contacts(contacts)
    choice = int(input("Enter the number of the contact to edit: ")) - 1
    if 0 <= choice < len(contacts):
        contacts[choice]["name"] = input("Enter New Name: ")
        contacts[choice]["phone"] = input("Enter New Phone Number: ")
        contacts[choice]["email"] = input("Enter New Email Address: ")
        print("Contact updated successfully!")
    else:
        print("Invalid selection.")

# Delete a contact
def delete_contact(contacts):
    view_contacts(contacts)
    choice = int(input("Enter the number of the contact to delete: ")) - 1
    if 0 <= choice < len(contacts):
        del contacts[choice]
        print("Contact deleted successfully!")
    else:
        print("Invalid selection.")

# Main program loop
contacts = load_contacts()

while True:
    print("\nContact Manager")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. Exit")

    option = input("Choose an option (1-5): ")

    if option == '1':
        add_contact(contacts)
    elif option == '2':
        view_contacts(contacts)
    elif option == '3':
        edit_contact(contacts)
    elif option == '4':
        delete_contact(contacts)
    elif option == '5':
        save_contacts(contacts)
        print("Contacts saved. Exiting...")
        break
    else:
        print("Invalid option. Try again.")
