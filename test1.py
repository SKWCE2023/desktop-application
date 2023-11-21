import tkinter as tk
from tkinter import ttk, messagebox
from barcode import Code128
from barcode.writer import ImageWriter
from reportlab.pdfgen import canvas
from datetime import datetime

class BarcodeGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Barcode Generator")
        self.root.geometry("600x400")

        # Variables
        self.order_id_var = tk.StringVar()
        self.date_var = tk.StringVar(value=datetime.today().strftime('%Y%m%d'))
        self.unique_code_var = tk.StringVar()
        self.generated_barcode = None

        # Create UI components
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.root, text="Order ID:").grid(row=0, column=0, padx=10, pady=10)
        ttk.Entry(self.root, textvariable=self.order_id_var).grid(row=0, column=1, padx=10, pady=10)

        ttk.Label(self.root, text="Date (YYYYMMDD):").grid(row=1, column=0, padx=10, pady=10)
        ttk.Entry(self.root, textvariable=self.date_var).grid(row=1, column=1, padx=10, pady=10)

        ttk.Label(self.root, text="Unique Code (6 characters):").grid(row=2, column=0, padx=10, pady=10)
        ttk.Entry(self.root, textvariable=self.unique_code_var).grid(row=2, column=1, padx=10, pady=10)

        ttk.Button(self.root, text="Generate Barcode", command=self.generate_barcode).grid(row=3, column=0, columnspan=2, pady=10)

        ttk.Button(self.root, text="Save Barcode as PDF", command=self.save_pdf).grid(row=4, column=0, columnspan=2, pady=10)

    def generate_barcode(self):
        try:
            # Get values from entry fields
            order_id = self.order_id_var.get()
            date = self.date_var.get()
            unique_code = self.unique_code_var.get()

            # Combine elements to create barcode content
            barcode_content = f"{order_id}{date}{unique_code}"

            # Generate barcode using Code128
            self.generated_barcode = Code128(barcode_content, writer=ImageWriter())
            tk.messagebox.showinfo("Barcode Generated", "Barcode generated successfully.")

        except Exception as e:
            tk.messagebox.showerror("Error", f"Error generating barcode: {str(e)}")

    def save_pdf(self):
        try:
            if self.generated_barcode is not None:
                # Save barcode to PDF
                pdf_filename = f"barcode_{self.order_id_var.get()}_{self.date_var.get()}_{self.unique_code_var.get()}.pdf"
                c = canvas.Canvas(pdf_filename)

                # Draw barcode on PDF
                barcode_path = self.generated_barcode.save(f'tmp_barcode')
                c.drawInlineImage(barcode_path, x=50, y=50, width=500, height=80)

                # Save PDF
                c.save()

                # Clean up temporary barcode file
                import os
                os.remove('tmp_barcode.png')

                tk.messagebox.showinfo("Barcode Saved", f"Barcode saved to {pdf_filename}")
            else:
                tk.messagebox.showwarning("Warning", "Please generate the barcode first.")

        except Exception as e:
            tk.messagebox.showerror("Error", f"Error saving barcode as PDF: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = BarcodeGeneratorApp(root)
    root.mainloop()
