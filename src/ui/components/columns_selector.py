import os
import tkinter as tk
from doctest import master
from tkinter import filedialog
from enum import Enum
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class ColumnsSelector(ttk.Frame):
    """
    Reusable widget consisting of:
        Label
        Combo box
        Label
        Combo box
    """
    def __init__(self, master, label, **kwargs):
        super().__init__(master, **kwargs)
        self.options = ["Option 1", "Option 2", "Option 3"]
        self.selected_value = ttk.StringVar(value="Select an option")

        self.primary_column=[]
        self.secondary_col=[]

        self.create_widgets(label)

    def create_widgets(self, label):
        # Label
        type_lbl = ttk.Label(
            self,
            text=label,
            width=15
        )
        type_lbl.grid(row=0,column=0,padx=(5, 5),pady=5,sticky="w")
        # Combo box
        combo_box =  ttk.Combobox(
            self,
            textvariable=self.selected_value,
            values=self.options,
        )
        # Set it to readonly so users cannot type custom values
        combo_box.state(['readonly'])
        combo_box.grid(row=0,column=1,padx=(5, 5),pady=5,sticky="w")

    def set_values(self, headers):
        self.options = headers
    def get(self):
        return self.selected_value
    def set(self, value):
        self.selected_value = value
