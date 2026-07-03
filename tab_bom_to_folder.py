import ttkbootstrap as tb
from ttkbootstrap.constants import *
import time


class ProfileTab(tb.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=20)

        # --- Form Inputs ---
        self.lbl_bom_directory = tb.Label(self, text="BOM directory:", font=("Helvetica", 11))
        self.lbl_bom_directory.pack(anchor=W, pady=(0, 5))

        self.ent_bom_directory = tb.Entry(self, bootstyle="info")
        self.ent_bom_directory.pack(fill=X, pady=(0, 15))

        self.lbl_working_folder = tb.Label(self, text="Working folder:", font=("Helvetica", 11))
        self.lbl_working_folder.pack(anchor=W, pady=(0, 5))

        self.ent_working_folder = tb.Entry(self, bootstyle="info")
        self.ent_working_folder.pack(fill=X, pady=(0, 15))

        # --- New Actions Layout (Pushed to the bottom) ---
        # Compare Button
        self.btn_compare = tb.Button(
            self,
            text="Compare",
            bootstyle="primary",
            command=self.start_comparison
        )
        self.btn_compare.pack(fill=X, pady=(10, 10))

        # Modern Progress Bar (Floodgauge) below the button
        # Using mode="indeterminate" makes the bar bounce back and forth
        self.progress = tb.Floodgauge(
            self,
            bootstyle="info",
            mode="indeterminate",
            mask="Processing... {}%"
        )
        self.progress.pack(fill=X, pady=(5, 0))

    def start_comparison(self):
        """Simulates a processing state when the button is clicked."""
        # Start the bouncing progress animation
        self.progress.start()

        # Disable button to prevent double clicks during processing
        self.btn_compare.config(state="disabled")

        # Stop animation automatically after 3 seconds (3000 ms)
        self.after(3000, self.stop_comparison)

    def stop_comparison(self):
        """Resets the layout back to its normal state."""
        self.progress.stop()
        self.btn_compare.config(state="normal")
