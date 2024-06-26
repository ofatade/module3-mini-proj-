# Contact Management System

import re

contacts = {}

def display_menu():
    print('''
Welcome to the Contact Management System!

Menu:
1. Add a new contact
2. Edit an existing contact
3. Delete a contact
4. Search for a contact
5. Display all contacts
6. Export contacts to a text file
7. Import contacts from a text file
8. Quit
''')
    
#display_menu()

def validate_email(email):# checking the format of the email with regex pattern
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(pattern, email) is not None

def validate_phone(phone):# checking the format of the phone number with regex pattern
        pattern = r'^\+?\d{1,15}$'
        return re.match(pattern, phone) is not None

def add_contacts():# Function to add new contacts

    name = input("Enter name: ")

    phone = input("Enter phone number without space or dashes: ")

    email = input("Enter email address: ")

    address = input("Enter address: ")

    notes = input("Enter notes: ")

    if not validate_phone(phone):
            print('='*75)
            print("Invalid phone number format.")
            return

    if not validate_email(email):
            print('='*75)
            print("Invalid email address format.")
            return

    contacts[phone] = {
            "name": name,
            "phone": phone,
            "email": email,
            "address": address,
            "notes": notes
        }
    print('='*75)
    print("Contact added successfully!")

#add_contacts()
    

def edit_contact():# Function to update the details of contacts

        identifier = input("Enter the phone number of the contact to edit without space or dash: ")

        if identifier not in contacts:
            print('='*75)
            print("Contact not found.")
            return

        name = input("Enter new name (leave blank to keep current name): ")
        phone = input("Enter new phone number without space or dash (leave blank to keep current number): ")
        email = input("Enter new email address (leave blank to keep current email): ")
        address = input("Enter new address (leave blank to keep current address): ")
        notes = input("Enter new notes (leave blank to keep current notes): ")

        if phone and not validate_phone(phone):
            print('='*75)
            print("Invalid phone number format.")
            return

        if email and not validate_email(email):
            print('='*75)
            print("Invalid email address format.")
            return

        if name:
            contacts[identifier]['name'] = name
        if phone:
            contacts[identifier]['phone'] = phone
        if email:
            contacts[identifier]['email'] = email
        if address:
            contacts[identifier]['address'] = address
        if notes:
            contacts[identifier]['notes'] = notes

        if phone:
            contacts[phone] = contacts.pop(identifier)

        print('='*75)
        print("Contact updated successfully!")

#edit_contact()


def delete_contact(): # Function to delete any contact in the dictionary with their phone number 

        identifier = input("Enter the phone number of the contact to delete without space or dashe: ")

        if identifier in contacts:
            del contacts[identifier]
            print('='*75) # Separation line
            print("Contact deleted successfully!")
        else:
            print('='*75)
            print("Contact not found.")

#delete_contact()


def search_contact(): # Function to search for any contact in the dictionary with phone number or email

        identifier = input("Enter the phone number without space or dashes or email of the contact to search: ")

        if identifier in contacts:
            contact = contacts[identifier]
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
            print(f"Notes: {contact['notes']}")
        else:
            for contact in contacts.values():
                if contact['email'] == identifier:
                    print(f"Name: {contact['name']}")
                    print(f"Phone: {contact['phone']}")
                    print(f"Email: {contact['email']}")
                    print(f"Address: {contact['address']}")
                    print(f"Notes: {contact['notes']}")
                    return
            print('='*75)    
            print("Contact not found.")

#search_contact()


def display_all_contacts(): # Function to show details of all contacts in our dictionary
        if not contacts:
            print('='*75)
            print("No contacts available.")
            return

        for phone, contact in contacts.items():
            print('='*75)
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

#display_all_contacts()


def export_contacts(): #Function to create and export our contacts into a text file

        filename = input("Enter the filename to export contacts to: ")

        try:
            with open(filename, 'w') as file:
                for phone, contact in contacts.items():
                     line = f"{contact['name']},{contact['phone']},{contact['email']},{contact['address']},{contact['notes']}\n"
                     file.write(line)
            print('='*75)         
            print("Contacts exported successfully!")
        except Exception as e:
            print(f"An error occurred while exporting contacts: {e}")

#export_contacts()


def import_contacts(): #  Function to import other contacts from a text file
        filename = input("Enter the filename to import contacts from: ")

        try:
            with open(filename, 'r') as file:
                for line in file:
                    name, phone, email, address, notes = line.strip().split(',')
                    contacts[phone] = {
                        "name": name,
                        "phone": phone,
                        "email": email,
                        "address": address,
                        "notes": notes
                    }
            print('='*75)
            print("Contacts imported successfully!")
        except Exception as e:
            print(f"An error occurred while importing contacts: {e}")

#import_contacts()


def quit(): # Function to exit the app
        print("Exiting Contact Management System. Goodbye!")
        exit()
#quit()



def main_app():

        while True:
            
            display_menu()

            choice = input("Enter your choice: ")

            if choice == '1':
                add_contacts()

            elif choice == '2':
                edit_contact()

            elif choice == '3':
                delete_contact()

            elif choice == '4':
                search_contact()

            elif choice == '5':
                display_all_contacts()

            elif choice == '6':
                export_contacts()

            elif choice == '7':
                import_contacts()

            elif choice == '8':
                quit()

            else:
                print("Invalid choice. Please try again.")

main_app()