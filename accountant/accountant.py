import tkinter as tk
from tkinter import ttk

class AccountantFrame(ttk.Frame):
    def __init__(self, master=None, user_info = None):
        super().__init__(master)
        ttk.Label(self, text="Accountant Frame").pack(padx=10, pady=10)