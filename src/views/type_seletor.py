
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class TypeSelector(ttk.Frame):
    """
    Reusable widget consisting of:
        Label
        Radion button

    """
    def __init__(self,master,label,on_update_table):
        super().__init__(master)
        self.selected_option = ttk.StringVar()

        # For parent calls
        self.on_update_table = on_update_table

        self.create_widgets(label)


    def create_widgets(self, label):
        # Label
        type_lbl = ttk.Label(
            self,
            text=label,
            width=15,
        )
        type_lbl.pack(side=LEFT, padx=(10, 50), pady=5)

        # Radion button
        self.bom_opt = ttk.Radiobutton(
            self,
            text="bom",
            variable=self.selected_option,
            value="bom",
            command=self.on_select,

        )
        self.bom_opt.pack(side=LEFT)

        folder_opt = ttk.Radiobutton(
            self,
            text="folder",
            variable=self.selected_option,
            value="folder",
            command=self.on_select,
        )
        folder_opt.pack(side=LEFT, padx=15)

        combined_opt = ttk.Radiobutton(
            self,
            text="combined",
            variable=self.selected_option,
            value="combined",
            command=self.on_select,
        )
        combined_opt.pack(side=LEFT)

    def select_defaulf(self):
        self.selected_option.set("bom")


    def on_select(self):
        print(self.selected_option.get())
        self.on_update_table()
