import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# Import UI
from views.path_selector import PathSelector, BrowseType

class PopupWindow(ttk.Frame):

    find_list: []

    def __init__(self, master):
        super().__init__(padding=20)
        self.find_list: []
        popup = ttk.Toplevel(title="Find missing files", size=(600, 300))

        # header and labelframe folder to find
        folder_to_find = "Select Folder to find the missing."
        self.to_find_lf = ttk.Labelframe(popup, text=folder_to_find, padding=15)
        self.to_find_lf.pack(fill=X, expand=YES, anchor=N, padx=20)

        # Add path selector widget
        self.folder_find = PathSelector(
            self.to_find_lf,
            label="Find in folder:",
            browse_type=BrowseType.FOLDER
        )
        self.folder_find.pack(fill="x")

        # header and labelframe folder to output
        folder_to_output = "Select Folder to place the output."
        self.to_copy_lf = ttk.Labelframe(popup, text=folder_to_output, padding=15)
        self.to_copy_lf.pack(fill=X, expand=YES, anchor=N, padx=20)

        # Add path selector widget
        self.folder_out = PathSelector(
            self.to_copy_lf,
            label="Output folder:",
            browse_type=BrowseType.FOLDER
        )
        self.folder_out.pack(fill="x")
        popup.transient(master)
        # popup.attributes('-topmost', True)  # Keeps window above others
        popup.place_window_center()

        # Trigger button!
        trigger_button = ttk.Button(
            popup,
            text="Find...",
            width=10,
            command=self.on_find_missing
        )
        trigger_button.pack(fill='x')

        # --- MODAL LOGIC START ---
        popup.grab_set()  # Redirects all user interaction to this window only
        # --- MODAL LOGIC END ---

        # Optional: Pauses main code execution until this window is destroyed
        popup.wait_window()

    def on_find_missing(self):
        ...