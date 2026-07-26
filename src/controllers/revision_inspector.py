import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from rules.validation_engine import ValidationEngine
# Import UI
from views.path_selector import PathSelector
from views.path_selector import BrowseType
from views.report_table import ReportTable
from views.type_selector import TypeSelector
from views.columns_selector import ColumnsSelector
from views.progress_message import ProgressMessage

# Import Configurations
from workflows.rev_inspector_config import RevInspectorConfig

# Import Services
from services.folder_scanner import FolderScanner, count_file_types
from services.bom_reader import BomReader
from services.comparison_service import ComparisonService

#Import Rules for comparison
from rules.missing_record_rule import MissingRecordRule
from rules.revision_rule import RevisionRule


# Import Datetime
from datetime import datetime



class RevisionsInspector(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=20)

        # Instance for Configurations
        self.config = RevInspectorConfig()

        # Instance for FolderScanner
        self.folder_scanner = FolderScanner()

        # Instance for BomReader
        self.bom_reader = BomReader()

        # Instance of ComparisonService
        self.comparison = ComparisonService(
            validator_engines= ValidationEngine(
                rules= self.config.RULES
            )
        )

        # header and labelframe option container
        option_text = "Scan the Project Folder then compare to BOM"
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

        # Add column selector widget
        self.column_selector = ColumnsSelector(
            self.option_lf,
            columns=self.config.KEY_COLUMNS
        )
        self.column_selector.pack(fill="x")

        # Add path selector widget
        self.folder_selector = PathSelector(
            self.option_lf,
            label="Project Folder",
            browse_type=BrowseType.FOLDER
        )
        self.folder_selector.pack(fill="x")

        # Trigger button!
        trigger_button = ttk.Button(
            self,
            text="Inspect Revisions",
            width=10,
            command=self.on_compare
        )
        trigger_button.pack(fill='x')
        #------------------------------------
        # Add Result frame label
        self.result_frame = ttk.Labelframe(self, text="", padding=15)
        self.result_frame.pack(fill=X, expand=YES, anchor=N)

        self.report_table = ReportTable(
            self.result_frame,
            columns=self.config.REPORT_TABLE_COLUMNS
        )
        self.report_table.pack(fill="both", expand=True)

        # ------------------------------------
        # Add progress and message status
        self.progress_message = ProgressMessage(self, "Status")
        self.progress_message.pack(fill="x")

    def on_compare(self):

        t1 = datetime.now()
        # Read BOM
        bom_path = self.bom_selector.get()
        selected_columns = self.column_selector.get()
        bom_dic = self.bom_reader.read_bom(bom_path, selected_columns)

        # Scan Folder
        folder_path = self.folder_selector.get()
        folder_dic = self.folder_scanner.parse_filename(
            folder_path,
        )

        self.comparison_results = self.comparison.compare(
            bom_dic,
            folder_dic
        )
        self.report_table.load_records_rev(self.comparison_results)

    def on_bom_selected(self, bom_path):
        headers = self.bom_reader.read_header(bom_path)
        self.column_selector.set_values(headers)
        self.progress_message.warning("✓ BOM loaded ")

    def on_clear(self):
        self.report_table.clear()

    # Temporarily use, to relocate to Services,
    def export_report(self):
        self.progress_message.warning("Exporting...")
        self.comparison.create_report(self.comparison_results, self.config.REPORT_TABLE_COLUMNS)
        self.progress_message.warning("Export completed!")

    def update_report_table(self):
        selected_option = self.type_selector.selected_option.get()
        if len(self.comparison_results) > 0:
            if selected_option == "bom":
                b_result = self.comparison.filter_results(self.comparison_results,{ComparisonStatus.RIGHT_ONLY})
                self.report_table.load_records(b_result)
            elif selected_option == "folder":
                f_result = self.comparison.filter_results(self.comparison_results,{ComparisonStatus.LEFT_ONLY})
                self.report_table.load_records(f_result)
            else:
                self.report_table.load_records(self.comparison_results)
        else:
            self.progress_message.warning("Comparison has not executed yet!")
        ## Helpful debug
        # print("----------------")
        # print("update_base_record")
        # print("self =", self)
        # print("class =", self.__class__.__name__)
        # print("attributes =", self.__dict__.keys())
