
import ttkbootstrap as ttk

# file type popup window
from views.file_type_popup import FileTypePopup


class ReportTable(ttk.Frame):

    def __init__(self, master, columns):
        super().__init__(master)

        self.result_map = {}

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

        self.tree.bind(
            "<ButtonRelease-1>",
            self.on_row_click
        )

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


    def load_records_rev(self, records):
        self.clear()

        for record in records:
            self.insert_row(
                record.to_table_row_rev()
            )
    def load_records_fol(self, records):
        self.clear()

        for record in records:
            self.insert_row(
                record.to_table_row_fol()
            )

        self.result_map = records

    def on_row_click(self, event):

        item_id = self.tree.identify_row(
            event.y
        )

        if not item_id:
            return

        result = self.result_map.get(item_id)

        if not result:
            return

        FileTypePopup(self.master, )
        # Pop up window


        # self.show_file_types(
        #     result,
        #     event.x_root,
        #     event.y_root
        # )