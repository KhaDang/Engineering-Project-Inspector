# import ttkbootstrap as ttk
# from ttkbootstrap.constants import *
#
# from views.path_selector import PathSelector
# from views.path_selector import BrowseType
# from views.report_table import ReportTable
# from views.type_seletor import TypeSelector
#
#
# class FolderToFolder(ttk.Frame):
#     def __init__(self, parent):
#
#         super().__init__(parent, padding=20)
#
#         # header and labelframe option container
#         option_text = "Scan 2 Project Folders and compare their file names"
#         self.option_lf = ttk.Labelframe(self, text=option_text, padding=15)
#         self.option_lf.pack(fill=X, expand=YES, anchor=N)
#
#         # Add path selector widget at the first row for directory 1
#         self.path1_selector = PathSelector(
#             self.option_lf,
#             label="W. Directory 1",
#             browse_type=BrowseType.FOLDER
#         )
#         self.path1_selector.pack(fill="x")
#
#         # Add output folder widget at the third row
#         self.path2_selector = PathSelector(
#             self.option_lf,
#             label="W.Directory 2",
#             browse_type=BrowseType.FOLDER
#         )
#         self.path2_selector.pack(fill="x")
#
#         # Add type selector widget
#         self.type_selector = TypeSelector(
#             self.option_lf,
#             label='Type',
#         )
#         self.type_selector.pack(fill="x")
#
#         # Add Result frame label
#         result_frame_text = ""
#         self.result_frame = ttk.Labelframe(self, text=result_frame_text, padding=15)
#         self.result_frame.pack(fill=X, expand=YES, anchor=N)
#
#         # Add Treeview that equals level to Labelframe.
#         columns = (
#             "Drawing Number",
#             "SLDPRT",
#             "SLDDRW",
#             "SLDASM",
#             "Status"
#         )
#
#         self.report_table = ReportTable(
#             self.result_frame,
#             columns=columns
#         )
#         self.report_table.pack(fill="both", expand=True)
#
#         # Add progress bar
#         self.progressbar = ttk.Progressbar(
#             master=self,
#             mode=INDETERMINATE,
#             bootstyle=(STRIPED, SUCCESS)
#         )
#         self.progressbar.pack(fill=X, expand=YES)
