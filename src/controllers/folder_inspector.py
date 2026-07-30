import ttkbootstrap as ttk
from ttkbootstrap.constants import *
# Import UI
from views.path_selector import PathSelector
from views.path_selector import BrowseType
from views.report_table import ReportTable
from views.type_selector import TypeSelector
from views.progress_message import ProgressMessage

# Import Configuration
from workflows.folder_inspector_config import FolderInspectorConfig

# Import Services
from services.folder_scanner import FolderScanner, count_file_types
from services.comparison_service import ComparisonService
from services.report_formatter import ReportFormatter

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

        # Instance for Report Formatter
        self.r_formatter = ReportFormatter()

        # header and labelframe option container
        option_text = "Scan 2 Project Folders"
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
        self.progress_message = ProgressMessage(self, "Status")
        self.progress_message.pack(fill="x")

    def on_compare(self):
        t1 = datetime.now()
        # Scan left folder
        left_path = self.left_folder_selector.get()
        left_dic = self.folder_scanner.scan_folder(left_path)


        # Scan right folder
        right_path = self.right_folder_selector.get()
        right_dic = self.folder_scanner.scan_folder(
            right_path,
            self.progress_message.start_progress,
            self.progress_message.update_progress
        )
        # Update message box files found, list all types of drawing records
        left_stats = count_file_types(self, left_dic)
        right_stats = count_file_types(self, right_dic)

        self.progress_message.info('Indexing files in Directory 1...')
        self.r_formatter.report(
            self.progress_message,
            left_stats,
            self.config.REPORT_STATUS_MESSAGES
        )
        self.progress_message.info('Indexing files in Directory 2...')
        self.r_formatter.report(
            self.progress_message,
            right_stats,
            self.config.REPORT_STATUS_MESSAGES
        )

        self.comparison_results = self.comparison.compare(
            left_dic,
            right_dic,
        )

        t2 = datetime.now()

        self.report_table.load_records_fol(self.comparison_results)

    def on_clear(self):
        self.comparison_results = []
        self.report_table.clear()
        self.progress_message.clear()



    def export_report(self):
        self.progress_message.warning("Exporting...")
        self.r_formatter.create_report(3,self.comparison_results, self.config.REPORT_TABLE_COLUMNS)
        self.progress_message.warning("Export completed!")

    def on_radio_changed(self):

        selected_option = self.type_selector.selected_option.get()

        predicate = self.config.FILTERS[selected_option]

        filtered = [
            r
            for r in self.comparison_results
            if predicate(r)
        ]

        self.report_table.load_records_fol(filtered)

        self.progress_message.info(f"{self.config.TYPE_OPTIONS[selected_option]} : {len(filtered)} files")

