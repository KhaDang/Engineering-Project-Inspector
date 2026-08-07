
import ttkbootstrap as ttk

class DialogButtonBar(ttk.Frame):
    """
    """
    def __init__(self,master,on_cancel, on_find):
        super().__init__(master)

        find_button = ttk.Button(
            master,
            text="Find & Copy",
            width=15,
            command=on_find
        )
        find_button.pack(side='right',pady=(15,15), padx=(15, 45))

        cancel_button = ttk.Button(
            master,
            text="Cancel",
            width=10,
            command=on_cancel
        )
        cancel_button.pack(side='right', padx=(15, 15))
