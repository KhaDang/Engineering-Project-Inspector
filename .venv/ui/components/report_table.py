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
        self.tree.pack(fill="both", expand=True)
        for col in self.columns:
            self.tree.heading(col, text=col)
