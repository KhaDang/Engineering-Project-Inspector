
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class BoxSelector(ttk.Frame):

    def __init__(self,
                 master,
                 label,
                 options,
                 on_update_table):
        super().__init__(master)
        self.options = options
        self.checkbox_vars = {}
        self.create_widgets(label)

    def create_widgets(self, label):
        # Label
        type_lbl = ttk.Label(
            self,
            text=label,
            width=15,
        )
        type_lbl.pack(side=LEFT, padx=(20, 20), pady=5)

        for key, value in self.options.items():
            var = ttk.BooleanVar(value=True)
            self.checkbox_vars[key] = var
            # check button
            check_button = ttk.Checkbutton(
                self,
                text= value,
                variable=var,
                command=self.on_changed_checkbox,

            )

            check_button.pack(side=LEFT, padx= (10, 10))

    def on_changed_checkbox(self):

        selected_keys = [key for key, var in self.checkbox_vars.items() if var.get()]
        print(selected_keys)

    def get_box_values(self):
        selected_keys = [key for key, var in self.checkbox_vars.items() if var.get()]
        return selected_keys
