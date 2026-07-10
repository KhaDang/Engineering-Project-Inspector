import pathlib
from tkinter import filedialog
from tkinter.filedialog import askdirectory
from ttkbootstrap import utility
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
# Import UI
from ui.components.path_selector import PathSelector
from ui.components.path_selector import BrowseType
from ui.components.report_table import ReportTable
from ui.components.type_seletor import TypeSelector
from ui.components.columns_selector import ColumnsSelector


# Import Services
from services.folder_scanner import FolderScanner
from services.bom_scanner import BomReader


class BomToFolder(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=20)
        # Instance for FolderScanner
        self.scanner = FolderScanner()
        self.bom_reader = BomReader()


        # header and labelframe option container
        option_text = "Read the BOM file then compare to the name of existing files that stored in Project Folder"
        self.option_lf = ttk.Labelframe(self, text=option_text, padding=15)
        self.option_lf.pack(fill=X, expand=YES, anchor=N)

        # Add Bom selector widget
        self.bom_selector = PathSelector(
            self.option_lf,
            label="BOM file",
            browse_type= BrowseType.FILE,
            on_path_changed=self.on_bom_selected
        )
        self.bom_selector.pack(fill="x")
        #-----------------------------------------
        self.container = ttk.Frame(self.option_lf, padding=5)

        # Add column selector widget
        self.primary_selector = ColumnsSelector(
            self.container,
            label="BOM key"
        )
        self.primary_selector.grid(row=0, column=0, padx=(0, 5), pady=1, sticky="w")

        # Add second column selector widget
        self.secondary_selector = ColumnsSelector(
            self.container,
            label="Secondary key"
        )
        self.primary_selector.grid(row=0, column=1, padx=(10, 5), pady=1, sticky="w")

        self.container.pack(fill=BOTH, expand=YES)
        #--------------------------------------------
        # Add path selector widget
        self.folder_selector = PathSelector(
            self.option_lf,
            label="Project Folder",
            browse_type=BrowseType.FOLDER
        )
        self.folder_selector.pack(fill="x")

        # Add type selector widget
        self.type_selector = TypeSelector(
            self.option_lf,
            label='Type',

        )
        self.type_selector.pack(fill="x")

        # Trigger button!! Test only
        trigger_button = ttk.Button(
            self,
            text="Test!!",
            width=10,
            command=self.on_compare
        )
        trigger_button.pack(fill='x')
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


    def on_compare(self):
        folder = self.folder_selector.get()
        records = self.scanner.scan_folder(folder)
        self.report_table.load_records(records)

        # for record in record.values():
        #     self.report_table.insert_row(
        #         record.to_table_row()
        #     )


    def on_bom_selected(self, bom_path):
        headers = self.bom_reader.read_header(bom_path)
        self.primary_selector.set(headers)
        self.secondary_selector.set(headers)
        print(headers)
