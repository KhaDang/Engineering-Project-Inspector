import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# Import UI
from views.path_selector import PathSelector
from views.path_selector import BrowseType
from views.report_table import ReportTable
from views.type_selector import TypeSelector
from views.columns_selector import ColumnsSelector
from views.progress_message import ProgressMessage

# Import Configurations
from workflows.file_inspector_configs import FileInspectorConfig

# Import Services
from services.folder_scanner import FolderScanner, count_file_types
from services.bom_reader import BomReader
from services.comparison_service import ComparisonService
from services.report_formatter import ReportFormatter

# Import Rules/ValidationEngine
from rules.validation_engine import ValidationEngine


# Import datetime
from datetime import datetime

class FilesInspector(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=20)

        # Instance for Workflow configuration
        self.config = FileInspectorConfig()

        # Instance for FolderScanner
        self.folder_scanner = FolderScanner()

        # Instance for BomReader
        self.bom_reader = BomReader()

        # Instance of ComparisonService
        self.comparison = ComparisonService(
            validator_engines = ValidationEngine(
                rules=self.config.RULES
            )
        )

        # Comparison result
        self.comparison_results = []

        # Instance for Report Formatter
        self.r_formatter = ReportFormatter()

        # header and labelframe option container
        option_text = "Compare BOM records to the Project Folder"
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

        # Add comlumn selector widget
        self.column_selector = ColumnsSelector(
            self.option_lf,
            columns= self.config.KEY_COLUMNS
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
            text="Inspect Files",
            width=10,
            command=self.on_compare
        )
        trigger_button.pack(fill='x')
        #------------------------------------
        # Add Result frame label
        self.result_frame = ttk.Labelframe(self, text="", padding=15)
        self.result_frame.pack(fill=X, expand=YES, anchor=N)

        self.type_selector = TypeSelector(
            self.result_frame,
            label='Filter',
            options= self.config.TYPE_OPTIONS,
            on_update_table= self.on_radio_changed

        )

        self.type_selector.pack(fill="x")
        # Confirm type selector is already created
        self.type_selector.select_default()


        # Add Treeview that equals level to Labelframe.
        self.report_table = ReportTable(
            self.result_frame,
            columns= self.config.REPORT_TABLE_COLUMNS
        )
        self.report_table.pack(fill='both', expand=True)

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

        # Update message box rows found
        self.progress_message.info(f"BOM records: {len(bom_dic)}")

        # Scan Folder, update progress bar
        folder_path = self.folder_selector.get()
        folder_dic = self.folder_scanner.scan_folder(
            folder_path,
            self.progress_message.start_progress,
            self.progress_message.update_progress
        )

        # Update message box files found, list all types of drawing records
        stats = count_file_types(self,folder_dic)

        self.r_formatter.report(
            self.progress_message,
            stats,
            self.config.REPORT_STATUS_MESSAGES
        )

        self.comparison_results = self.comparison.compare(
            bom_dic,
            folder_dic
        )

        self.report_table.load_records(self.comparison_results)

    def on_bom_selected(self, bom_path):
        headers = self.bom_reader.read_header(bom_path)
        self.column_selector.set_values(headers)
        self.progress_message.warning("✓ BOM loaded ")

    def on_clear(self):
        self.comparison_results=[]
        self.report_table.clear()
        self.progress_message.clear()


    # Temporarily use, to relocate to Services,
    def export_report(self):
        self.progress_message.warning("Exporting...")
        self.comparison.create_report(self.comparison_results, self.config.REPORT_TABLE_COLUMNS)
        self.progress_message.warning("Export completed!")

    def on_radio_changed(self):

        selected_option = self.type_selector.selected_option.get()

        predicate = self.config.FILTERS[selected_option]

        filtered = [
            r
            for r in self.comparison_results
            if predicate(r)
        ]

        self.report_table.load_records(filtered)
        self.progress_message.info(f"{self.config.TYPE_OPTIONS[selected_option]} : {len(filtered)} files")

        ## Helpful debug
        # print("----------------")
        # print("update_base_record")
        # print("self =", self)
        # print("class =", self.__class__.__name__)
        # print("attributes =", self.__dict__.keys())


