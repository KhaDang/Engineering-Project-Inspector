import ttkbootstrap as ttk
from ttkbootstrap.constants import *
# Import UI
from views.path_selector import PathSelector
from views.path_selector import BrowseType
from views.report_table import ReportTable
from views.type_selector import TypeSelector

# Import Configuration
from workflows.folder_inspector_config import FolderInspectorConfig

# Import Services
from services.folder_scanner import FolderScanner, count_file_types
from services.comparison_service import ComparisonService

# Import issues
from models.comparison_issue import MissingInLeft, MissingInRight, FileMatching

# Import Validator
from rules.validation_engine import ValidationEngine

# Import datetime
from datetime import datetime

class FolderInspector(ttk.Frame):
    def __init__(self, parent):

        super().__init__(parent, padding=20)

        # Instance for Configurations
        self.config = FolderInspectorConfig()

        # Instance for FolderScanner
        self.folder_scanner = FolderScanner()

        # Instance of ComparisonService
        self.comparison = ComparisonService(
            validator_engines= ValidationEngine(
                rules= self.config.RULES
            )
        )

        # header and labelframe option container
        option_text = "Scan 2 Project Folders and compare their file names"
        self.option_lf = ttk.Labelframe(self, text=option_text, padding=15)
        self.option_lf.pack(fill=X, expand=YES, anchor=N)

        # Add path selector widget at the first row for directory 1
        self.left_folder_selector = PathSelector(
            self.option_lf,
            label="W. Directory 1",
            browse_type=BrowseType.FOLDER
        )
        self.left_folder_selector.pack(fill="x")

        # Add output folder widget at the third row
        self.right_folder_selector = PathSelector(
            self.option_lf,
            label="W.Directory 2",
            browse_type=BrowseType.FOLDER
        )
        self.right_folder_selector.pack(fill="x")

        # Add type selector widget
        # self.type_selector = TypeSelector(
        #     self.option_lf,
        #     label='Type',
        #     on_update_table=None
        # )
        # self.type_selector.pack(fill="x")

        # Trigger button!
        trigger_button = ttk.Button(
            self,
            text="Inspect Folders",
            width=10,
            command=self.on_compare
        )
        trigger_button.pack(fill='x')

        # Add Result frame label
        result_frame_text = ""
        self.result_frame = ttk.Labelframe(self, text=result_frame_text, padding=15)
        self.result_frame.pack(fill=X, expand=YES, anchor=N)

        self.type_selector = TypeSelector(
            self.result_frame,
            label='Filter',
            options=self.config.TYPE_OPTIONS,
            on_update_table=self.on_radio_changed

        )
        self.type_selector.pack(fill="x")
        # Confirm type selector is already created
        self.type_selector.select_default()


        # Add Treeview that equals level to Labelframe.
        self.report_table = ReportTable(
            self.result_frame,
            columns=self.config.REPORT_TABLE_COLUMNS
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
        t1 = datetime.now()
        # Scan left folder
        left_path = self.left_folder_selector.get()
        left_dic = self.folder_scanner.scan_folder(left_path)


        # Scan Folder
        right_path = self.right_folder_selector.get()
        right_dic = self.folder_scanner.scan_folder(
            right_path,
        )

        self.comparison_results = self.comparison.compare(
            left_dic,
            right_dic,
        )

        t2 = datetime.now()

        self.report_table.load_records_fol(self.comparison_results)


    def export_report(self):
        self.comparison.create_report(self.comparison_results, self.config.REPORT_TABLE_COLUMNS)

    def on_radio_changed(self):
        FILTERS = {
            "dir1": lambda r:
            r.has_issue(MissingInLeft),

            "dir2": lambda r:
            r.has_issue(MissingInRight),

            "match": lambda r:
            r.has_issue(FileMatching),

            "default": lambda r:
            True,
        }

        selected_option = self.type_selector.selected_option.get()

        predicate = FILTERS[selected_option]

        filtered = [
            r
            for r in self.comparison_results
            if predicate(r)
        ]

        self.report_table.load_records_fol(filtered)
