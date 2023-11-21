import tkinter as tk
from tkinter import ttk
from login import LoginFrame
from utils.utils import create_login_frame

class App:
    def __init__(self, root):
        self.showCaptcha = False
        self.locked = False
        self.root = root
        self.root.title("World Championship")
        self.root.geometry("800x600")
        self.root.configure(bg="white")
        self.style = ttk.Style()
        self.style.configure("TFrame", background="white")
        self.style.configure("TLabel", background="white", font=('Helvetica', 10))
        create_login_frame(self.root, self.showCaptcha, self.locked)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
