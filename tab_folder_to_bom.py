import ttkbootstrap as tb
from ttkbootstrap.constants import *


class SettingsTab(tb.Frame):
    def __init__(self, parent):
        # Initialize the parent tb.Frame class
        super().__init__(parent, padding=20)

        # Build UI Components
        self.lbl_api = tb.Label(self, text="API Secret Key:", font=("Helvetica", 11))
        self.lbl_api.pack(anchor=W, pady=(0, 5))

        self.ent_api = tb.Entry(self, bootstyle="success", show="*")
        self.ent_api.pack(fill=X, pady=(0, 15))
