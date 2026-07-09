import os
import tkinter as tk
from tkinter import filedialog
from enum import Enum
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class TypeSelector(ttk.Frame):
    """
    Reusable widget consisting of:
        Label
        Radion button
        Browse Button

    """
    def __init__(
            self,
            master,
            label="Type",
            button_text="Go",
            **kwargs
    ):
        super().__init__(master, **kwargs)
        self.type_var = ttk.StringVar(value='.sldprt')
        self.create_widgets(
            label,
            button_text
        )

    def create_widgets(self, label, button_text):
        # Label
        type_lbl = ttk.Label(
            self,
            text=label,
            width=15
        )
        type_lbl.pack(side=LEFT)
        # Radion button
        sldprt_opt = ttk.Radiobutton(
            self,
            text=".sldprt",
            variable=self.type_var,
            value=".sldprt"
        )
        sldprt_opt.pack(side=LEFT)

        sldasm_opt = ttk.Radiobutton(
            self,
            text=".sldasm",
            variable=self.type_var,
            value=".sldasm"
        )
        sldasm_opt.pack(side=LEFT, padx=15)

        slddrw_opt = ttk.Radiobutton(
            self,
            text=".slddrw",
            variable=self.type_var,
            value=".slddrw"
        )
        slddrw_opt.pack(side=LEFT)
        slddrw_opt.invoke()

        browse_btn = ttk.Button(
            self,
            text=button_text,
            command=self.browse,
            width=20
        )
        browse_btn.pack(side=RIGHT, padx=5)

    def browse(self):
        if self.browse_type == BrowseType.FOLDER:
            folder = filedialog.askdirectory(
                title="Select Folder"
            )
            if folder:
                self.path.set(folder)
        elif self.browse_type == BrowseType.FILE:
            filename = filedialog.askopenfilename(
                title="Select File",
                filetypes=[
                ("Excel Workbook", "*.xlsx"),
                ("Excel Workbook 97-2003", "*.xls"),
                ("All Files", "*.*")
                ]
            )
            if filename:
                self.path.set(filename)

    # ------------------------------------------------
    # Public Methods
    # ------------------------------------------------

