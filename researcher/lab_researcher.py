import tkinter as tk
from tkinter import ttk

class ResearcherFrame(ttk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        ttk.Label(self, text="Researcher Frame").pack(padx=10, pady=10)