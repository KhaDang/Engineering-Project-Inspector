
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class TypeSelector(ttk.Frame):
    """
    Reusable widget consisting of:
        Label
        Radion button

    """
    def __init__(
            self,
            master,
            label,
            options,
            on_update_table=None
        ):
        super().__init__(master)
        self.selected_option = ttk.StringVar()

        self.options = options

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

        for key, value in self.options.items():
            # Radio button
            radio_button = ttk.Radiobutton(
                self,
                text= value,
                variable=self.selected_option,
                value= key,
                command=self.on_select,

            )
            radio_button.pack(side=LEFT, padx= (10, 10))


    def select_default(self):
        self.selected_option.set("default")
    def select_right(self):
        self.selected_option.set('right')


    def on_select(self):
        if self.on_update_table:
            self.on_update_table()
        return