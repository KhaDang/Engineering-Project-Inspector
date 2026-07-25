
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class ColumnsSelector(ttk.Frame):
    """
    Reusable widget consisting of:
        Label
        Combo box
        Label
        Combo box
    """
    def __init__(self, master, columns, **kwargs):
        super().__init__(master, **kwargs)

        self.columns = columns

        # self.p_selected_value = ttk.StringVar(value="Select an column")

        self.create_widgets()


    def create_widgets(self):

        self.combo_boxes: dict[str, ttk.Combobox] = {}

        for index, value in enumerate(self.columns):
            # Create a label
            type_lbl = ttk.Label(
                self,
                text=value,
                width=15
            )
            type_lbl.pack(side=LEFT, padx=(10, 5))

            box_variable = ttk.StringVar()

            # Create a combo box
            combo_box = ttk.Combobox(
                self,
                textvariable=box_variable,
                state="readonly"
            )
            # Set it to readonly so users cannot type custom values
            combo_box.pack(side=LEFT, padx= (5,50))

            self.combo_boxes[value] = combo_box

    def set_values(self, headers):
        self.reset_values()

        for combo_box in self.combo_boxes.values():
            combo_box['values'] = headers

            # Try to guess Drawing Number column
            for i, h in enumerate(headers):
                if h.lower() in ("drawing", "drawing number", "part number", "number","rev", "revision"):
                    combo_box.current(i)
                    break

    def reset_values(self):
        for combo_box in self.combo_boxes.values():
            combo_box.set('')

    def get(self):
        values = {
            column: combo_box.get()
            for column, combo_box in self.combo_boxes.items()
        }
        return values