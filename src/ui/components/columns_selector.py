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
    def __init__(self, master, p_label, s_label, **kwargs):
        super().__init__(master, **kwargs)

        self.p_selected_value = ttk.StringVar(value="Select an column")
        self.s_selected_value = ttk.StringVar(value=" Select an column")

        self.create_widgets(p_label, s_label)


    def create_widgets(self, p_label, s_label):
        # 1st Label
        p_type_lbl = ttk.Label(
            self,
            text=p_label,
            width=15
        )
        p_type_lbl.grid(row=0,column=0,padx=(10, 5),pady=5,sticky="w")
        # Combo box
        self.p_combo_box =  ttk.Combobox(
            self,
            textvariable=self.p_selected_value,
            state="readonly"
        )
        # Set it to readonly so users cannot type custom values
        self.p_combo_box.grid(row=0,column=1,padx=(5, 5),pady=5,sticky="w")

        # 2nd label
        s_type_lbl = ttk.Label(
            self,
            text=s_label,
            width=15
        )
        s_type_lbl.grid(row=0, column=2, padx=(25, 5), pady=5, sticky="w")
        # Combo box
        self.s_combo_box = ttk.Combobox(
            self,
            textvariable=self.s_selected_value,
            state="readonly"
        )
        self.s_combo_box.grid(row=0, column=3, padx=(5, 5), pady=5, sticky="w")

    def set_values(self, headers):
        self.reset_values()
        self.p_combo_box["values"] = headers
        self.s_combo_box["values"] = headers

        # Try to guess Drawing Number column
        for i, h in enumerate(headers):
            if h.lower() in ("drawing", "drawing number", "part number", "number"):
                self.p_combo_box.current(i)
                break

        # Try to guess Revision column
        for i, h in enumerate(headers):
            if h.lower() in ("rev", "revision"):
                self.s_combo_box.current(i)
                break

    def reset_values(self):
        self.p_combo_box.set('')
        self.s_combo_box.set('')

    def get_drawing_column(self):
        return self.drawing_var.get()

    def get_revision_column(self):
        return self.revision_var.get()