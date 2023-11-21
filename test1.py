import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class ImageFrame:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Frame")

        # Load an image using Pillow (replace 'path/to/your/image.png' with the actual path)
        image_path = 'assets/images/Logo.png'
        image_pil = Image.open(image_path)
        self.image = ImageTk.PhotoImage(image_pil)

        # Create a label to display the image
        self.image_label = ttk.Label(root, image=self.image)
        self.image_label.grid(row=0, column=0, padx=10, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageFrame(root)
    root.mainloop()