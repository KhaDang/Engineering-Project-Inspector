# import os
# import tkinter as tk
# from tkinter import filedialog
import ttkbootstrap as ttk

class ReportTable(ttk.Frame):

    def __init__(self, master, columns):
        super().__init__(master)
        self.columns = columns
        self.create_widgets()

    def create_widgets(self):
        self.tree = ttk.Treeview(
            self,
            columns = self.columns,
            show='headings',
        )
        # Add headings for Treeview table
        for col in self.columns:
            self.tree.heading(col, text=col)
            self.tree. column(col, width=120)

        # sample data - to delete
        self.tree.insert(
            "",
            "end",
            values=("130-050001", "Yes", "No")
        )

        # Add vertical scrollbar to the right side of tree
        self.scrollbar = ttk.Scrollbar(
            self,
            orient="vertical",
            command=self.tree.yview
        )
        # Configure the Treeview to use scrollbar
        self.tree.configure(yscrollcommand=self.scrollbar.set)

        # pack
        self.tree.pack(side="left", expand=True, fill="both")
        self.scrollbar.pack(side="right", fill="y")


