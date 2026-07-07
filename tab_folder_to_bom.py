import pathlib
from tkinter import filedialog
from tkinter.filedialog import askdirectory
from ttkbootstrap import utility
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class SettingsTab(ttk.Frame):
    def __init__(self, parent):
        # Initialize the parent tb.Frame class
        super().__init__(parent, padding=20)

        # application variables
        _path = pathlib.Path().absolute().as_posix()
        self.path_var = ttk.StringVar(value=_path)
        self.bom_entry = ttk.StringVar(value='input the path to BOM here')
        self.type_var = ttk.StringVar(value='endswidth')

        # header and labelframe option container
        option_text = "Complete the form to begin your comparison"
        self.option_lf = ttk.Labelframe(self, text=option_text, padding=15)
        self.option_lf.pack(fill=X, expand=YES, anchor=N)

        self.create_path_row()
        self.create_file_row()
        self.create_type_row()
        self.create_results_view()

        self.progressbar = ttk.Progressbar(
            master=self,
            mode=INDETERMINATE,
            bootstyle=(STRIPED, SUCCESS)
        )
        self.progressbar.pack(fill=X, expand=YES)

    def create_path_row(self):
        """Add path row to labelframe"""
        path_row = ttk.Frame(self.option_lf)
        path_row.pack(fill=X, expand=YES)
        path_lbl = ttk.Label(path_row, text="Project Folder", width=15)
        path_lbl.pack(side=LEFT, padx=(15, 0))
        path_ent = ttk.Entry(path_row, textvariable=self.path_var)
        path_ent.pack(side=LEFT, fill=X, expand=YES, padx=5)
        browse_btn = ttk.Button(
            master=path_row,
            text="Browse",
            command=self.on_browse,
            width=8
        )
        browse_btn.pack(side=LEFT, padx=5)

    def create_file_row(self):
        """Add term row to labelframe"""
        file_row = ttk.Frame(self.option_lf)
        file_row.pack(fill=X, expand=YES, pady=15)
        file_lbl = ttk.Label(file_row, text="BOM File", width=15)
        file_lbl.pack(side=LEFT, padx=(15, 0))
        file_ent = ttk.Entry(file_row, textvariable=self.bom_entry)
        file_ent.pack(side=LEFT, fill=X, expand=YES, padx=5)
        browse_btn = ttk.Button(
            master=file_row,
            text="Browse",
            command=self.browse_bom_file,
            width=8
        )
        browse_btn.pack(side=LEFT, padx=5)

    def create_type_row(self):
        """Add type row to labelframe"""
        type_row = ttk.Frame(self.option_lf)
        type_row.pack(fill=X, expand=YES)
        type_lbl = ttk.Label(type_row, text="Type", width=8)
        type_lbl.pack(side=LEFT, padx=(15, 0))

        contains_opt = ttk.Radiobutton(
            master=type_row,
            text="Contains",
            variable=self.type_var,
            value="contains"
        )
        contains_opt.pack(side=LEFT)

        startswith_opt = ttk.Radiobutton(
            master=type_row,
            text="StartsWith",
            variable=self.type_var,
            value="startswith"
        )
        startswith_opt.pack(side=LEFT, padx=15)

        endswith_opt = ttk.Radiobutton(
            master=type_row,
            text="EndsWith",
            variable=self.type_var,
            value="endswith"
        )
        endswith_opt.pack(side=LEFT)
        endswith_opt.invoke()

    def create_results_view(self):
        """Add result treeview to labelframe"""
        self.resultview = ttk.Treeview(
            master=self,
            bootstyle=INFO,
            columns=[0, 1, 2, 3, 4],
            show=HEADINGS
        )
        self.resultview.pack(fill=BOTH, expand=YES, pady=10)

        # setup columns and use `scale_size` to adjust for resolution
        self.resultview.heading(0, text='Name', anchor=W)
        self.resultview.heading(1, text='Modified', anchor=W)
        self.resultview.heading(2, text='Type', anchor=E)
        self.resultview.heading(3, text='Size', anchor=E)
        self.resultview.heading(4, text='Path', anchor=W)
        self.resultview.column(
            column=0,
            anchor=W,
            width=utility.scale_size(self, 125),
            stretch=False
        )
        self.resultview.column(
            column=1,
            anchor=W,
            width=utility.scale_size(self, 140),
            stretch=False
        )
        self.resultview.column(
            column=2,
            anchor=E,
            width=utility.scale_size(self, 50),
            stretch=False
        )
        self.resultview.column(
            column=3,
            anchor=E,
            width=utility.scale_size(self, 50),
            stretch=False
        )
        self.resultview.column(
            column=4,
            anchor=W,
            width=utility.scale_size(self, 300)
        )

    def on_browse(self):
        """Callback for directory browse"""
        path = askdirectory(title="Browse directory")
        if path:
            self.path_var.set(path)

    def browse_bom_file(self):

        filename = filedialog.askopenfilename(
            title="Select BOM File",
            filetypes=[
                ("Excel Workbook", "*.xlsx"),
                ("Excel Workbook 97-2003", "*.xls"),
                ("All Files", "*.*")
            ]
        )

        if filename:
            self.bom_entry.set(filename)
