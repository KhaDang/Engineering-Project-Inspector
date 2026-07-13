import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# Import UI
from ui.components.path_selector import PathSelector
from ui.components.path_selector import BrowseType
from ui.components.report_table import ReportTable
from ui.components.type_seletor import TypeSelector
from ui.components.columns_selector import ColumnsSelector
from ui.components.progress_message import ProgressMessage

# Import Services
from services.folder_scanner import FolderScanner
from services.bom_reader import BomReader
from services.comparison_service import ComparisonService
from models.comparsion_result import ComparisonStatus


class BomToFolder(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=20)

        # Instance for FolderScanner
        self.folder_scanner = FolderScanner()

        # Instance for BomReader
        self.bom_reader = BomReader()

        # Instance of ComparisonService
        self.comparison = ComparisonService()

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

        # Ad comlumn selector widget
        self.column_selector = ColumnsSelector(
            self.option_lf,
            p_label= "BOM key",
            s_label= "Secondary key"
        )
        self.column_selector.pack(fill="x")


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
        #------------------------------------
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

        # ------------------------------------
        # Add progress and message status
        self.message_box = ProgressMessage(self, "Status")
        self.message_box.pack(fill="x")


    def on_compare(self):
        bom_path = self.bom_selector.get()
        folder_path = self.folder_selector.get()

        combo_values = (self.column_selector.get())
        bom_dic = self.bom_reader.read_bom(bom_path,combo_values)
        # Update message box rows found
        self.message_box.info(f"Rows found: {len(bom_dic)}")

        folder_dic = self.folder_scanner.scan_folder(folder_path)
        # Update message box files found
        self.message_box.info("Files found")
        part, drawing, assembly, duplicates = self.folder_scanner.count_file_types(folder_dic)

        self.message_box.info(f"SLDPRT : {part}")
        self.message_box.info(f"SLDDRW : {drawing}")
        self.message_box.info(f"SLDASM : {assembly}")
        self.message_box.info(f"Duplicates : {duplicates}")

        self.message_box.warning("Comparing...")
        comparison_results = self.comparison.compare(bom_dic, folder_dic)
        self.message_box.warning("Done.")
        matches = len(self.comparison.filter_results(
            comparison_results,
            {ComparisonStatus.LEFT_ONLY, ComparisonStatus.RIGHT_ONLY}
            )
        )
        self.message_box.info(f"Matches: {matches}")

        # Filter the results _ exclude the LEFT_ONLY
        filtered_comparison_results = self.comparison.filter_results(comparison_results, {ComparisonStatus.LEFT_ONLY} )

        # update report table
        self.report_table.load_records(filtered_comparison_results)


    def on_bom_selected(self, bom_path):
        headers = self.bom_reader.read_header(bom_path)
        self.column_selector.set_values(headers)
        self.message_box.warning("✓ BOM loaded ")

