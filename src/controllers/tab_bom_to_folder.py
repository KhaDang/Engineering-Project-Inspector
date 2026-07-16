import ttkbootstrap as ttk
from ttkbootstrap.constants import *
# Import Pandas temporarily
import pandas as pd

# Import UI
from views.path_selector import PathSelector
from views.path_selector import BrowseType
from views.report_table import ReportTable
from views.type_seletor import TypeSelector
from views.columns_selector import ColumnsSelector
from views.progress_message import ProgressMessage

# Import Services
from services.folder_scanner import FolderScanner, count_file_types
from services.bom_reader import BomReader
from services.comparison_service import ComparisonService
from models.comparsion_result import ComparisonStatus

# Import datetime
from datetime import datetime

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
        option_text = "Compare the BOM records to the Project Folder"
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
            text="Compare",
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
            "PDF",
            "Status"
        )

        self.report_table = ReportTable(
            self.result_frame,
            columns=columns
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
        combo_values = (self.column_selector.get())
        bom_dic = self.bom_reader.read_bom(bom_path, combo_values)

        # Update message box rows found
        self.progress_message.info(f"BOM records: {len(bom_dic)}")

        # Scan Folder
        folder_path = self.folder_selector.get()
        folder_dic = self.folder_scanner.scan_folder(
            folder_path,
        )

        # Start progress bar
        self.progress_message.start_progress(len(bom_dic|folder_dic))
        print(len(bom_dic|folder_dic))

        # Update message box files found, list all types of drawing records
        stats = count_file_types(self,folder_dic)
        self.progress_message.info(f"Drawing records: {stats.drawing_records}")
        self.progress_message.info(f"SLDPRT : {stats.part_count}")
        self.progress_message.info(f"SLDDRW : {stats.drawing_count}")
        self.progress_message.info(f"SLDASM : {stats.assembly_count}")
        self.progress_message.info(f"Duplicates : {stats.duplicate_count}")

        self.progress_message.warning("Comparing...")
        comparison_results = self.comparison.compare(
            bom_dic,
            folder_dic,
            progress_callback=self.progress_message.update_progress
            # Callback function (argument were passed from class Folder Scanner)

        )
        matches = len(self.comparison.filter_results(
            comparison_results,
            {ComparisonStatus.LEFT_ONLY, ComparisonStatus.RIGHT_ONLY}
            )
        )
        self.progress_message.warning(f"Total matches: {matches}")
        t2 = datetime.now()

        # Update progress bar
        self.progress_message.warning(f"Finished in: {(t2 - t1).total_seconds()} sec")
        # Filter the results _ exclude the LEFT_ONLY
        filtered_comparison_results = self.comparison.filter_results(comparison_results, {ComparisonStatus.LEFT_ONLY} )

        # update report table
        self.report_table.load_records(filtered_comparison_results)


    def on_bom_selected(self, bom_path):
        headers = self.bom_reader.read_header(bom_path)
        self.column_selector.set_values(headers)
        self.progress_message.warning("✓ BOM loaded ")


    # Temporarily use, to relocate to Services,
    def export_report(self):
        # 1. Extract data values from the Treeview widget
        row_data = [self.report_table.tree.item(child)["values"] for child in self.report_table.tree.get_children()]

        # 2. Extract column headers from the Treeview widget
        column_headers = self.report_table.tree["columns"]

        # 3. Create the Pandas DataFrame
        df = pd.DataFrame(row_data, columns=column_headers)

        df.to_excel("exported_treeview.xlsx", index=False)
        self.progress_message.info("Exported successfully!")