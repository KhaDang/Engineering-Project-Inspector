import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# Import UI
from views.path_selector import PathSelector, BrowseType
from views.dialog_button_bar import DialogButtonBar
from views.box_selector import BoxSelector

from dataclasses import dataclass, field
from pathlib import Path

@dataclass
class CopyRequest:

    search_folder: Path

    destination_folder: Path

    # file_types: list[str]
    #
    # overwrite: bool

class CopyMissingDialog(ttk.Frame): # View
    def __init__(self,
                 master,
                 on_copy_missing_files, # For calling from App
                 ):
        super().__init__(padding=20)

        self.on_copy_missing_files = on_copy_missing_files

        self.popup = ttk.Toplevel(title="Find missing files", size=(600, 300))
        self.popup.resizable(False, False) # Lock size scaling
        # header and labelframe folder to find
        folder_to_find = "Copy missing files."
        self.dialog_lf = ttk.Labelframe(self.popup, text=folder_to_find, padding=20)
        self.dialog_lf.pack(fill=X, expand=YES, anchor=N, padx=20, pady=20)

        # Add path selector widget
        self.folder_find = PathSelector(
            self.dialog_lf,
            label="Find in folder:",
            browse_type=BrowseType.FOLDER
        )
        self.folder_find.pack(fill="x")

        # Add path selector widget
        self.folder_out = PathSelector(
            self.dialog_lf,
            label="Output folder:",
            browse_type=BrowseType.FOLDER
        )
        self.folder_out.pack(fill="x")

        # Add BoxSelector
        CHECK_OPTIONS = {
            ".sldprt": ".sldprt",
            ".sldasm": ".sldasm",
            ".slddrw": ".slddrw",
            ".pdf": ".pdf",

        }
        self.box_selector = BoxSelector(
            self.dialog_lf,
            label='Type',
            options=CHECK_OPTIONS,
            on_update_table=None
        )
        self.box_selector.pack(fill='x')

        # Add Buttons
        self.button_bar = DialogButtonBar(self.popup,
                                          on_cancel= self.on_cancel,
                                          on_find= self.on_find
                                          )
        self.button_bar.pack(fill='x')

        self.popup.transient(master)
        # popup.attributes('-topmost', True)  # Keeps window above others
        self.popup.place_window_center()

        # --- MODAL LOGIC START ---
        self.popup.grab_set()  # Redirects all user interaction to this window only
        # --- MODAL LOGIC END ---

        # Optional: Pauses main code execution until this window is destroyed
        self.popup.wait_window()

    def on_find(self):
        request = CopyRequest(
                            search_folder= self.folder_find.get(),
                            destination_folder = self.folder_out.get()
        )

        self.on_copy_missing_files(request)
    def on_cancel(self):
        self.popup.destroy()




