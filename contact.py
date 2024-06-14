class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}, Address: {self.address}"

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        return [(contact.name, contact.phone) for contact in self.contacts]

    def search_contact(self, query):
        results = []
        for contact in self.contacts:
            if query.lower() in contact.name.lower() or query in contact.phone:
                results.append(contact)
        return results

    def update_contact(self, old_name, new_contact):
        for idx, contact in enumerate(self.contacts):
            if contact.name.lower() == old_name.lower():
                self.contacts[idx] = new_contact
                return True
        return False

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                return True
        return False

def main():
    book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact = Contact(name, phone, email, address)
            book.add_contact(contact)
            print("Contact added.")

        elif choice == '2':
            contacts = book.view_contacts()
            if contacts:
                for name, phone in contacts:
                    print(f"Name: {name}, Phone: {phone}")
            else:
                print("No contacts found.")

        elif choice == '3':
            query = input("Enter name or phone number to search: ")
            results = book.search_contact(query)
            if results:
                for contact in results:
                    print(contact)
            else:
                print("No contacts found.")

        elif choice == '4':
            old_name = input("Enter the name of the contact to update: ")
            name = input("Enter new name: ")
            phone = input("Enter new phone number: ")
            email = input("Enter new email: ")
            address = input("Enter new address: ")
            new_contact = Contact(name, phone, email, address)
            if book.update_contact(old_name, new_contact):
                print("Contact updated.")
            else:
                print("Contact not found.")

        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            if book.delete_contact(name):
                print("Contact deleted.")
            else:
                print("Contact not found.")

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()