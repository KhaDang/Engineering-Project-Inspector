import pathlib
from tkinter import filedialog
from tkinter.filedialog import askdirectory
from ttkbootstrap import utility
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from ui.components.path_selector import PathSelector
from ui.components.path_selector import BrowseType
from ui.components.report_table import ReportTable
from ui.components.type_seletor import TypeSelector


class FileToFile(ttk.Frame):
    def __init__(self, parent):

        super().__init__(parent, padding=20)

        # header and labelframe option container
        option_text = "Compare Partlist stored in 2 separated files"
        self.option_lf = ttk.Labelframe(self, text=option_text, padding=15)
        self.option_lf.pack(fill=X, expand=YES, anchor=N)

        # Add file selector widget at the first row
        self.file1_selector = PathSelector(
            self.option_lf,
            label="BOM 1",
            browse_type= BrowseType.FILE
        )
        self.file1_selector.pack(fill="x")

        # Add path selector widget at the second row
        self.file2_selector = PathSelector(
            self.option_lf,
            label="BOM 2",
            browse_type=BrowseType.FILE
        )
        self.file2_selector.pack(fill="x")

        # Add type selector widget
        self.type_selector = TypeSelector(
            self.option_lf,
            label='Type',

        )
        self.type_selector.pack(fill="x")

        # Add Result frame label
        result_frame_text = ""
        self.result_frame = ttk.Labelframe(self, text=result_frame_text, padding=15)
        self.result_frame.pack(fill=X, expand=YES, anchor=N)

        # Add Treeview that equals level to Labelframe.
        columns = (
            "Drawing Number",
            "SLDPRT",
            "SLDDRW",
            "SLDASM",
            "Status"
        )

        self.report_table = ReportTable(
            self.result_frame,
            columns=columns
        )
        self.report_table.pack(fill="both", expand=True)

        # Add progress bar
        self.progressbar = ttk.Progressbar(
            master=self,
            mode=INDETERMINATE,
            bootstyle=(STRIPED, SUCCESS)
        )
        self.progressbar.pack(fill=X, expand=YES)
