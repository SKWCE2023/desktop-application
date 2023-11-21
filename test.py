import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from reportlab.pdfgen import canvas
from fuzzywuzzy import fuzz
import csv

class MaterialOrderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Material Order Form")
        self.root.geometry("800x600")

        # Sample data (you need to replace this with your actual data)
        self.clients = ["Client A", "Client B", "Client C"]
        self.services = ["Service A", "Service B", "Service C"]
        self.materials = {"Material A": 10, "Material B": 20, "Material C": 30}

        # Variables
        self.selected_client_var = tk.StringVar()
        self.selected_service_var = tk.StringVar()
        self.quantity_var = tk.IntVar()
        self.barcode_var = tk.StringVar()
        self.order_price_var = tk.StringVar()

        # Create UI components
        self.create_widgets()

    def create_widgets(self):
        # Client Section
        ttk.Label(self.root, text="Client:").grid(row=0, column=0, padx=10, pady=10)
        self.client_combobox = ttk.Combobox(self.root, textvariable=self.selected_client_var, values=self.clients)
        self.client_combobox.grid(row=0, column=1, padx=10, pady=10)
        self.client_combobox.bind("<KeyRelease>", self.filter_clients)

        # Service Section
        ttk.Label(self.root, text="Service:").grid(row=1, column=0, padx=10, pady=10)
        self.service_combobox = ttk.Combobox(self.root, textvariable=self.selected_service_var, values=self.services)
        self.service_combobox.grid(row=1, column=1, padx=10, pady=10)
        self.service_combobox.bind("<KeyRelease>", self.filter_services)

        # Quantity Section
        ttk.Label(self.root, text="Quantity:").grid(row=2, column=0, padx=10, pady=10)
        self.quantity_entry = ttk.Entry(self.root, textvariable=self.quantity_var)
        self.quantity_entry.grid(row=2, column=1, padx=10, pady=10)

        # Barcode Section
        ttk.Label(self.root, text="Barcode:").grid(row=3, column=0, padx=10, pady=10)
        self.barcode_entry = ttk.Entry(self.root, textvariable=self.barcode_var)
        self.barcode_entry.grid(row=3, column=1, padx=10, pady=10)

        # Order Price Section
        ttk.Label(self.root, text="Order Price:").grid(row=4, column=0, padx=10, pady=10)
        ttk.Entry(self.root, textvariable=self.order_price_var, state='readonly').grid(row=4, column=1, padx=10, pady=10)

        # Buttons
        ttk.Button(self.root, text="Generate Barcode", command=self.generate_barcode).grid(row=5, column=0, pady=10)
        ttk.Button(self.root, text="Generate Order", command=self.generate_order).grid(row=5, column=1, pady=10)

    def filter_clients(self, event):
        filter_text = self.selected_client_var.get()
        filtered_clients = [client for client in self.clients if fuzz.partial_ratio(filter_text, client) >= 50]
        self.client_combobox['values'] = filtered_clients

    def filter_services(self, event):
        filter_text = self.selected_service_var.get()
        filtered_services = [service for service in self.services if fuzz.partial_ratio(filter_text, service) >= 50]
        self.service_combobox['values'] = filtered_services

    def generate_barcode(self):
        barcode_text = self.barcode_var.get()
        if barcode_text:
            # Save barcode to PDF
            pdf_filename = "barcode.pdf"
            c = canvas.Canvas(pdf_filename)
            c.drawString(100, 100, barcode_text)
            c.save()
            messagebox.showinfo("Barcode Generated", f"Barcode saved to {pdf_filename}")

    def generate_order(self):
        # Generate order form and save to text file
        order_text = f"Client: {self.selected_client_var.get()}\n"
        order_text += f"Service: {self.selected_service_var.get()}\n"
        order_text += f"Quantity: {self.quantity_var.get()}\n"
        order_text += f"Barcode: {self.barcode_var.get()}\n"
        order_text += f"Order Price: {self.order_price_var.get()}\n"

        text_filename = "order.txt"
        with open(text_filename, 'w') as file:
            file.write(order_text)

        messagebox.showinfo("Order Form Generated", f"Order form saved to {text_filename}")

if __name__ == "__main__":
    root = tk.Tk()
    app = MaterialOrderApp(root)
    root.mainloop()
