import os
import tkinter as tk
from tkinter import filedialog
from enum import Enum
import ttkbootstrap as ttk
#

class BrowseType(Enum):
    FOLDER = 1
    FILE = 2

class PathSelector(ttk.Frame):
    """
    Reusable widget consisting of:
        Label
        Entry
        Browse Button
    Can be used for:
        • Folder selection
        • Excel file selection
        • Output folder
        • PDF
        • STEP
    """
    def __init__(
            self,
            master,
            label="Path",
            browse_type=BrowseType.FOLDER,
            filetypes=None,
            button_text="Browse",
            on_path_changed=None,
            **kwargs
    ):
        super().__init__(master, **kwargs)
        self.browse_type = browse_type
        self.filetypes = filetypes
        self.path = tk.StringVar()
        self.on_path_changed = on_path_changed
        self.create_widgets(
            label,
            button_text
        )

    def create_widgets(self, label, button_text):
        self.columnconfigure(1, weight=1)
        ttk.Label(
            self,
            text=label,
            width=15
        ).grid(
            row=0,
            column=0,
            padx=(10, 5),
            pady=5,
            sticky="w"
        )
        ttk.Entry(
            self,
            textvariable=self.path
        ).grid(
            row=0,
            column=1,
            sticky="ew",
            padx=5,
            pady=5
        )
        ttk.Button(
            self,
            text=button_text,
            width=10,
            command=self.browse
        ).grid(
            row=0,
            column=2,
            padx=(5,10),
            pady=5
        )

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
                if self.on_path_changed:
                    self.on_path_changed(filename)



    # ------------------------------------------------
    # Public Methods
    # ------------------------------------------------

    def get(self):
        return self.path.get()
    def set(self, value):
        self.path.set(value)
    def clear(self):
        self.path.set("")


