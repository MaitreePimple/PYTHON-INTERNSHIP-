import json
contat_book = {}

def load_contacts():
    try:
        with open("contacts.json","r") as file:
            global contact_book
            contact_book = json,load(file)
    except FileNotFoundError:
        contact_book = {}

def save_contacts():
    with open("contacts.json","w") as file:
        json.dump(contact_book,file,indent = 4)

def add_contact():
    name = input("Enter name:")
    number = input("Enter number:")
    email = input("Enter Email:")

    if name in contact_book:
        print("Contact already exist. use update for modyifying")
    else:
        contact_book[name]= {"Number": number , "email": email }
        print("Successfully saved")
        save_contacts

def view_contacts():
    if contact_book:
        print("\nContact List:")
        for name , details in contact_book.items():
            print(f"Name: {name} , Number : {details['numbers']}")
    else:
        print("No contact found.")

def search_contact():
    query = input("Enter name or phone number to search:")
    found = False
    for name, details in contact_book.items():
        if query.lower()in name.lower() or query in details['phone']:
            print(f"\nName:{name}")
            print(f"Number: {details['numbers']}")
            print(f"Email : {details ['email']}")
    if not found:
        print("No Contact found")

def update_contact() :
    name = input("Enter name :")
    if name in contact_book: 
     number = input(f"Enter new phone number({contact_book[name] ['number']}): ") or contact_book[name]['number']
     email = input(f"Enter the email({contact_book[name]['email']}): ") or contact_book[name]['email']   
     contact_book[name] = {"number":number , "email": email}
     print("Updated Successfully")
     save_contacts()
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter name : ")
    if name in contact_book:
        confirm = input(f"Delete the contact {name}? (yes/no): ").lower()
        if confirm == "yes":
            del contact_book[name]
            print("Deleted")
            save_contacts()
        else:
            print("Unsuccessful")
    else:
        print("Contact not found.")

def menu() :
    load_contacts()
    while True:
        print("\n Contact Book Menu:")
        print("Add contact")
        print("view contacts")
        print("Search contact")
        print("Update COntact")
        print("Delete Contact")
        print("EXIT")

        choice = input("Enter your choice: ")

        if choice == "Add contact":
            add_contact()
        elif choice == "view contacts" :
            view_contacts()
        elif choice == "Search contact" :
            search_contact()
        elif choice == "Update COntact ":
            update_contact()
        elif choice == "Delete Contact ":
            delete_contact()
        elif choice == "EXIT":
            print("EXIT")
            break
        else:
            print("Invalid ..")
if __name__  == "__main__" :
    menu()

