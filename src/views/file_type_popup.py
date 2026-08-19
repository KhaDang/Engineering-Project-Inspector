import ttkbootstrap as ttk

class FileTypePopup(ttk.Frame):

    def __init__(self, master):
        super().__init__(master)

        self.popup = ttk.Toplevel(master, size=(150, 100))
        self.popup.overrideredirect(True)
        self.popup.withdraw()


        record_label = ttk.Label(
            self.popup,
            text="Drawing record",
            width=15
        )
        record_label.pack(fill='x')

        columns = ['Type', 'Left', 'Right']

        self.tree = ttk.Treeview(self.popup, height=18, columns=columns, show='headings')
        # Add headings for Treeview table
        for col in columns:
            self.tree.heading(col, text=col, anchor ='w')
            self.tree.column(col, width=120, anchor='w')
        # pack
        self.tree.pack(side="left", expand=True, fill="both", pady=5)
