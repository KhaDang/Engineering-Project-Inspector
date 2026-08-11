import tkinter

import ttkbootstrap as ttk
from ttkbootstrap.widgets.scrolled import ScrolledText
from ttkbootstrap.constants import *
# Module use for calling date time
from datetime import datetime


class ProgressMessage(ttk.Frame):
    """
    Reusable widget consisting of:
        Label
        Scrolledtext
    """

    def __init__(self, master, label, **kwargs):
        super().__init__(master, **kwargs)

        self.master = master

        self.label = label

        self.create_widgets()

    def create_widgets(self):
        # Add progress bar
        self.progressbar = ttk.Progressbar(
            master=self,
            mode=DETERMINATE,
            bootstyle=(STRIPED, SUCCESS)
        )
        self.progressbar.pack(fill=X, expand=YES)

        # option_text = " "
        # self.option_lf = ttk.Labelframe(self, text=option_text, padding=15)
        # self.option_lf.pack(fill=X, expand=NO, anchor=N)

        title = ttk.Label(
            self,
            text=self.label,
            width=15
        )
        title.pack(fill="x")
        # Scrolled Text
        self.console = ScrolledText(
            self,
            padding= 5,
            autohide=True,
        )
        self.console.pack(fill="both", expand=NO)
        self.console.text.insert("end", "Sytem initialized...\n")
        self.console.text.config(height=6)


    def clear(self):
        self.console.text.delete("1.0", tkinter.END)
        self.console.text.insert("end", "Sytem initialized...\n")


    def info(self, message):

        self.console.text.insert("end", message + "\n")
        self.console.text.see("end")

    def warning(self, message):
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.console.text.insert("end", f"{timestamp}: {message} \n")
        self.console.text.see("end")

    def confirmed_message(self, message):
        self.console.text.delete("1.0", tkinter.END)
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.console.text.insert("end", f"{timestamp}: {message}")
        self.console.text.see("end")

    def error(self, message):
        ...


    # Methods for progress bar

    def start_progress(self, maximum):

        self.progressbar["maximum"] = maximum
        self.progressbar["value"] = 10

    def update_progress(self, value, text):

        self.progressbar["value"] = value
        self.console.text.delete("insert linestart", "insert lineend")
        self.console.text.insert("insert", text)

        self.progressbar.update_idletasks()

    def finish_progress(self):

        self.progressbar["value"] = self.progressbar["maximum"]

    def dialog_console(self):
        self.console.text.delete("1.0", tkinter.END)
        self.console.text.config(height=1)