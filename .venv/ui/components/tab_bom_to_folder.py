import pathlib
from tkinter import filedialog
from tkinter.filedialog import askdirectory
from ttkbootstrap import utility
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from ui.components.path_selector import PathSelector
from ui.components.path_selector import BrowseType
from ui.components.report_table import ReportTable

class BomToFolder(ttk.Frame):
    def __init__(self, parent):

        super().__init__(parent, padding=20)

        # header and labelframe option container
        option_text = "Scan the project folder and compare to bom"
        self.option_lf = ttk.Labelframe(self, text=option_text, padding=15)
        self.option_lf.pack(fill=X, expand=YES, anchor=N)

        # Add file selector widget at the first row
        self.bom_selector = PathSelector(
            self.option_lf,
            label="BOM file",
            browse_type= BrowseType.FILE
        )
        self.bom_selector.pack(fill="x")

        # Add path selector widget at the second row
        self.file_selector = PathSelector(
            self.option_lf,
            label="Project Folder",
            browse_type=BrowseType.FOLDER
        )
        self.file_selector.pack(fill="x")

        # Add output folder widget at the third row
        self.output_selector = PathSelector(
            self.option_lf,
            label="Output Folder",
            browse_type=BrowseType.FOLDER
        )
        self.output_selector.pack(fill="x")

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


