import tkinter as tk
from tkinter import ttk

class AssistantFrame(ttk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        ttk.Label(self, text="Assistant Frame").pack(padx=10, pady=10)
