
import random
import string
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
def generate_password():    
    try:
        length = int(password_length_entry.get())
        if  length < 5:
            raise ValueError("Password should above 5 characters.")
        characters =""
        if include_uppercase.get():
            characters+= string.ascii_uppercase
        if include_lowercase.get():
            characters+=string.ascii_lowercase
        if include_symbols.get():
            characters+=string.punctuation
        if include_numbers.get():
            characters+=string.digits
        
        if not characters:
            raise ValueError("Please give an correct password.")
        
        password = "".join(random.choice(characters) for _ in range(length))
        generated_password.set(password)
    except ValueError as e:
        messagebox.showerror("Error",str(e))
root = tk.Tk()
root.title ("PASSWORD GENRATOR")
root.geometry("400x500")
root .resizable(False,False)

style = ttk.Style()
style.configure("TLabel",font=("Ariel",12))
style.configure("TButton",font=("Ariel",12))

tittle_label = ttk.Label(root, text="Passwrod Generator",font=("Ariel",14,"bold"))
tittle_label.pack(pady=10)

input_frame = ttk.Frame(root)
input_frame.pack(pady=10, padx=20)

password_length_label = ttk.Label(input_frame,text="Password Length:")
password_length_label.grid(row=0, column=0, pady=5, sticky="w")
password_length_entry = ttk.Entry(input_frame, width=20)
password_length_entry.grid(row=0, column=1, pady=5, padx=5)

include_uppercase = tk.BooleanVar(value=True)
include_lowercase = tk.BooleanVar(value=True)
include_symbols = tk.BooleanVar(value=False)
include_numbers = tk.BooleanVar(value=True)

uppercase_check = ttk.Checkbutton(input_frame, text="Include Uppercase", variable=include_uppercase)
uppercase_check.grid(row=1, column=0, pady=5, sticky="w")

lowercase_check = ttk.Checkbutton(input_frame, text="Include Lowercase",variable=include_lowercase)
lowercase_check.grid(row=2,column=0,pady=5,sticky="w")

symbols_check = ttk.Checkbutton(input_frame, text="Include Symbols", variable="include_symbols")
symbols_check.grid(row=3,column=0,pady=5, sticky="w")

numbers_check = ttk.Checkbutton(input_frame, text="Include Symbols", variable="include_symbols")
numbers_check.grid(row=4,column=0,pady=5, sticky="w")

generated_password = tk.StringVar()
password_display_label = ttk.Label(root, text = "Genrated Password:")
password_display_label.pack(pady=5)
password_diaply_entry = ttk.Entry(root, textvariable=generated_password, font=("Ariel", 12), state="readonly", justify="center")
password_diaply_entry.pack(pady=5,padx=10,fill="x")

generate_button = ttk.Button(root, text="Generate Password", command = generate_password)
generate_button.pack(pady=10)

root.mainloop()
