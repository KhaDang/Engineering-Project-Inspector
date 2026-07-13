import ttkbootstrap as ttk
from ttkbootstrap.widgets.scrolled import ScrolledText
from ttkbootstrap.constants import *
# Module use for calling date time
from datetime import datetime, date


class ProgressMessage(ttk.Frame):
    """
    Reusable widget consisting of:
        Label
        Scrolledtext
    """

    def __init__(self, master, label, **kwargs):
        super().__init__(master, **kwargs)
        self.label = label
        self.create_widgets()

    def create_widgets(self):
        # Add progress bar
        self.progressbar = ttk.Progressbar(
            master=self,
            mode=INDETERMINATE,
            bootstyle=(STRIPED, SUCCESS)
        )
        self.progressbar.pack(fill=X, expand=YES)

        option_text = " "
        self.option_lf = ttk.Labelframe(self, text=option_text, padding=15)
        self.option_lf.pack(fill=X, expand=NO, anchor=N)



        title = ttk.Label(
            self.option_lf,
            text=self.label,
            width=15
        )
        title.pack(fill="x")
        # Scrolled Text
        self.console = ScrolledText(
            self.option_lf,
            padding= 5,
            autohide=True,
        )
        self.console.pack(fill="both", expand=NO)
        self.console.text.insert("end", "Sytem initialized...\n")
        self.console.text.config(height=6)


    def clear(self):
        ...

    def info(self, message):

        self.console.text.insert("end", message + "\n")
        self.console.text.see("end")

    def warning(self, message):
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.console.text.insert("end", f"{timestamp}: {message} \n")
        self.console.text.see("end")

    def error(self, message):
        ...

    def start(self):
        ...

    def stop(self):
        ...

    def set_progress(self, value, maximum):
        ...