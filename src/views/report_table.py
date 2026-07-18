
import ttkbootstrap as ttk

class ReportTable(ttk.Frame):

    def __init__(self, master, columns):
        super().__init__(master)
        self.tree = ttk.Treeview(self, height=18, columns=columns, show='headings')
        # Add headings for Treeview table
        for col in columns:
            self.tree.heading(col, text=col, anchor ='w')
            self.tree.column(col, width=120, anchor='w')

        # Add vertical scrollbar to the right side of tree
        self.scrollbar = ttk.Scrollbar(
            self,
            orient="vertical",
            command=self.tree.yview
        )
        # Configure the Treeview to use scrollbar
        self.tree.configure(yscrollcommand=self.scrollbar.set)

        # pack
        self.tree.pack(side="left", expand=True, fill="both", pady=5)
        self.scrollbar.pack(side="right", fill="y")

    def insert_row(self, values):
        self.tree.insert(
            "",
            "end",
            values=values
        )

    def clear(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

    def load_records(self, records):
        self.clear()

        for record in records:
            self.insert_row(
                record.to_table_row()
            )