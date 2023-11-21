import tkinter as tk
from tkinter import ttk, messagebox, PhotoImage
import requests
from db import create_customer

class AddClientFrame:
    def __init__(self, root):
        self.root = root
        img = PhotoImage(file='assets/images/Logo.png')
        self.root.iconphoto(False, img)
        self.root.title("Add New Client")
        self.root.geometry("800x600")
        self.root.configure(bg="white")
        ttk.Label(self.root, text="Please fill the following data").pack(padx=10, pady=10)
        self.frame = ttk.Frame(self.root, padding=(20, 20))
        self.frame.pack(padx=10, pady=10)
        labels = ['First Name', 'Last Name', 'Login', 'Password', 'Date of Birth', 'Passport Series', 'Passport Number', 'Phone Number', 'Email', 'Company Name']
        self.entries = {}
        for i, label_text in enumerate(labels):
            key = label_text.lower().replace(' ', '_')
            label = ttk.Label(self.frame, text=label_text)
            label.grid(row=i, column=0, padx=10, pady=10, sticky=tk.W)
            entry = ttk.Entry(self.frame)
            entry.grid(row=i, column=1, padx=10, pady=10)
            if key == 'date_of_birth':
                entry.insert(0, 'DD/MM/YYYY')
                entry.configure(foreground="gray")
                entry.bind("<FocusIn>", self.on_entry_focus_in)
                entry.bind("<FocusOut>", self.on_entry_focus_out)
            self.entries[key] = entry
        add_button = ttk.Button(self.frame, text="Add Client", command=self.add_client)
        add_button.grid(row=len(labels), column=0, columnspan=2, pady=10)
        self.result_label = ttk.Label(self.frame, text="")
        self.result_label.grid(row=len(labels) + 1, column=0, columnspan=2, pady=10)

    def add_client(self):
        try:
            data = {key: entry.get() for key, entry in self.entries.items()}
            response = create_customer(data)
            if response.get("error_message"):
                messagebox.showerror("Operation Failed", "Failed to add customer. Please try again")
            else:
                messagebox.showinfo("Success", "Customer added successfully")
                self.root.destroy()
        except requests.exceptions.RequestException as e:
            print(f"Error in the request: {e}")

    def on_entry_focus_in(self, event):
        entry = self.entries['date_of_birth']
        if entry.get() == 'DD/MM/YYYY':
            entry.delete(0, tk.END)
            entry.configure(show="")
            entry.configure(foreground="black")

    def on_entry_focus_out(self, event):
        entry = self.entries['date_of_birth']
        if entry.get() == '':
            entry.insert(0, 'DD/MM/YYYY')
            entry.configure(show="")
            entry.configure(foreground="gray")