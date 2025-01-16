import json
import tkinter as tk
from tkinter import messagebox

contact_book = {}

# Load contacts from a file
def load_contacts():
    global contact_book
    try:
        with open("contacts.json", "r") as file:
            contact_book = json.load(file)
    except FileNotFoundError:
        contact_book = {}

# Save contacts to a file
def save_contacts():
    with open("contacts.json", "w") as file:
        json.dump(contact_book, file, indent=4)

# Add a new contact
def add_contact():
    name = name_entry.get()
    number = number_entry.get()
    email = email_entry.get()

    if not name or not number or not email:
        messagebox.showwarning("Input Error", "All fields are required!")
        return

    if name in contact_book:
        messagebox.showwarning("Duplicate Entry", "Contact already exists! Use Update instead.")
    else:
        contact_book[name] = {"number": number, "email": email}
        save_contacts()
        messagebox.showinfo("Success", "Contact added successfully!")
        update_contact_list()

# View all contacts
def update_contact_list():
    contact_list.delete(0, tk.END)
    for name, details in contact_book.items():
        contact_list.insert(tk.END, f"{name} - {details['number']}")

# Search for a contact
def search_contact():
    query = search_entry.get().strip().lower()
    contact_list.delete(0, tk.END)
    
    for name, details in contact_book.items():
        if query in name.lower() or query in details["number"]:
            contact_list.insert(tk.END, f"{name} - {details['number']}")

# Update a contact
def update_contact():
    name = name_entry.get()
    if name in contact_book:
        number = number_entry.get() or contact_book[name]["number"]
        email = email_entry.get() or contact_book[name]["email"]
        
        contact_book[name] = {"number": number, "email": email}
        save_contacts()
        messagebox.showinfo("Success", "Contact updated successfully!")
        update_contact_list()
    else:
        messagebox.showwarning("Not Found", "Contact not found!")

# Delete a contact
def delete_contact():
    name = name_entry.get()
    if name in contact_book:
        del contact_book[name]
        save_contacts()
        messagebox.showinfo("Deleted", "Contact deleted successfully!")
        update_contact_list()
    else:
        messagebox.showwarning("Not Found", "Contact not found!")

# GUI Setup
root = tk.Tk()
root.title("Contact Book")

tk.Label(root, text="Name: ").grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

tk.Label(root, text="Number: ").grid(row=1, column=0)
number_entry = tk.Entry(root)
number_entry.grid(row=1, column=1)

tk.Label(root, text="Email: ").grid(row=2, column=0)
email_entry = tk.Entry(root)
email_entry.grid(row=2, column=1)

# Buttons
tk.Button(root, text="Add Contact", command=add_contact).grid(row=3, column=0, columnspan=2)
tk.Button(root, text="Update Contact", command=update_contact).grid(row=4, column=0, columnspan=2)
tk.Button(root, text="Delete Contact", command=delete_contact).grid(row=5, column=0, columnspan=2)

# Search
tk.Label(root, text="Search:").grid(row=6, column=0)
search_entry = tk.Entry(root)
search_entry.grid(row=6, column=1)
tk.Button(root, text="Search", command=search_contact).grid(row=6, column=2)

# Contact List
contact_list = tk.Listbox(root, width=50)
contact_list.grid(row=7, column=0, columnspan=3)

tk.Button(root, text="View Contacts", command=update_contact_list).grid(row=8, column=0, columnspan=3)

load_contacts()
update_contact_list()

root.mainloop()
