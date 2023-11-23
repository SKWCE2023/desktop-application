import tkinter as tk
from tkinter import ttk

class AssistantFrame(ttk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        ttk.Label(self, text="Please select the action you need to perform:").pack(padx=10, pady=10)
        ttk.Button(self, text="Create Order", command=self.create_order_frame).pack(pady=10)
        ttk.Button(self, text="Add New Client", command=self.add_new_client).pack(pady=10)

    def create_order_frame(self):
        pass
    
    def add_new_client(self):
        pass
