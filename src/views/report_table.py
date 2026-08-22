
import ttkbootstrap as ttk

# file type popup window
from views.file_type_popup import FileTypePopup

# Import Interfaces
from observer import Observer

class ReportTable(ttk.Frame, Observer):

    def __init__(self, master, columns, state):
        super().__init__(master)
        self.master = master
        self.result_map = {}

        self.tree = ttk.Treeview(self, height=18, columns=columns, show='headings')
        self.file_type_popup = FileTypePopup(self.tree) #Floating window when user interacts with treeview

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

        state.add_observer(self)  # Add Report table into observers


    def insert_row(self, values, record):
        item_id = self.tree.insert(
            "",
            "end",
            values=values
        )
        self.result_map[item_id] = record

    def clear(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

    def load_records(self, records):
        self.clear()

        for record in records:
            self.insert_row(
                record.to_table_row(),
                record
            )


    def load_records_rev(self, records):
        self.clear()

        for record in records:
            self.insert_row(
                record.to_table_row_rev(),
                record
            )
    def load_records_fol(self, records):
        self.clear()

        for record in records:
            self.insert_row(
                record.to_table_row_fol(),
                record
            )

    def on_row_click(self, event):

        item_id = self.tree.identify_row(
            event.y
        )
        if not item_id:
            return

        result = self.result_map.get(item_id)


        if not result:
            return

        self.file_type_popup.show_tip(event.x_root, event.y_root, record=result)

    def on_motion(self,event):
        self.file_type_popup.on_motion(event)

    def on_release(self, event):
        self.file_type_popup.on_release(event)

    def update(self, state):
        if state.current_tab == ".!notebook.!folderinspector":
            self.tree.bind("<Button-1>", self.on_row_click)
            # Bind mouse movement to track cursor
            self.tree.bind("<B1-Motion>", self.on_motion)
            self.tree.bind("<ButtonRelease-1>", self.on_release)
        else:
            self.tree.unbind("<Button-1>")
            self.tree.unbind("<B1-Motion>")
            self.tree.unbind("<ButtonRelease-1>")