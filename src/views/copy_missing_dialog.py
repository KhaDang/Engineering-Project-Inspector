import os
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# Import UI
from views.path_selector import PathSelector, BrowseType
from views.dialog_button_bar import DialogButtonBar
from views.box_selector import BoxSelector
from views.type_selector import TypeSelector
from views.progress_message import ProgressMessage

# Import configurations
from workflows.dialog_copy_missing_configs import DialogCopyMissingConfig

# Import

 # Import Copy request
from models.copy_request import CopyRequest


class CopyMissingDialog(ttk.Frame): # View
    def __init__(self,
                 master,
                 on_copy_missing_files, # For calling from Controller
                 ):
        super().__init__(padding=20)

        self.setting = DialogCopyMissingConfig()

        self.on_copy_missing_files = on_copy_missing_files

        self.popup = ttk.Toplevel(title="Find missing files", size=(600, 370))

        icon_path = self.get_resource_path("src/assets/search_icon.ico")

        self.popup.iconbitmap(icon_path)


        self.popup.resizable(False, False) # Lock size scaling
        # header and labelframe folder to find

        self.dialog_lf = ttk.Labelframe(self.popup, text="Find missing files then copy to folder...", padding=20)
        self.dialog_lf.pack(fill=X, expand=YES, anchor=N, padx=20, pady=5)

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
        self.box_selector = BoxSelector(
            self.dialog_lf,
            label='Type:',
            options=self.setting.CHECK_OPTIONS,
            on_update_table=None
        )
        self.box_selector.pack(fill='x', pady=10)

        # Add mode selector for copying
        self.type_selector = TypeSelector(
            self.dialog_lf,
            "Copy mode:",
            self.setting.TYPE_OPTIONS,
            )
        self.type_selector.select_right()

        self.type_selector.pack(fill='x')

        # Add progress message
        self.progress_message = ProgressMessage(self.popup, "")
        self.progress_message.dialog_console() # Config console only for popup window
        self.progress_message.pack(fill='x', pady=5, padx=20)

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


    def get_resource_path(self,relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

    def on_find(self):
        key = self.type_selector.selected_option.get()

        request = CopyRequest(
                            source= self.folder_find.get(),
                            destination = self.folder_out.get(),
                            extensions=self.box_selector.get_box_values(),
                            copy_mode= self.setting.FILTER[key]
        )
        self.on_copy_missing_files(request, self.progress_message)

    def on_cancel(self):
        self.popup.destroy()




