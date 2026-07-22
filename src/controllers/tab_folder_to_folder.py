import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from views.path_selector import PathSelector
from views.path_selector import BrowseType
from views.report_table import ReportTable
from views.type_seletor import TypeSelector

# Import Services
from services.folder_scanner import FolderScanner, count_file_types
from services.comparison_service import ComparisonService
from models.comparsion_result import ComparisonStatus


# Import datetime
from datetime import datetime

class FolderToFolder(ttk.Frame):
    def __init__(self, parent):

        super().__init__(parent, padding=20)

        # Instance for FolderScanner
        self.folder_scanner = FolderScanner()

        # Instance of ComparisonService
        self.comparison = ComparisonService()

        # Comparison result
        self.comparison_results = []

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
        self.type_selector = TypeSelector(
            self.option_lf,
            label='Type',
            on_update_table=None
        )
        self.type_selector.pack(fill="x")

        # Trigger button!
        trigger_button = ttk.Button(
            self,
            text="Inspect Files",
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
            "PDF",
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
            progress_callback=None
            # Callback function (argument were passed from class Folder Scanner)

        )
        # matches = len(self.comparison.filter_results(
        #     self.comparison_results,
        #     {ComparisonStatus.LEFT_ONLY, ComparisonStatus.RIGHT_ONLY}
        #     )
        # )
        t2 = datetime.now()

        # Update progress bar
        # Filter the results _ exclude the LEFT_ONLY
        filtered_comparison_results = self.comparison.filter_results(self.comparison_results, {ComparisonStatus.RIGHT_ONLY} )
        self.type_selector.bom_opt.invoke()

        # update report table
        self.report_table.load_records(filtered_comparison_results)

        self.export_report()


    def export_report(self):
        self.comparison.create_report(self.comparison_results)
