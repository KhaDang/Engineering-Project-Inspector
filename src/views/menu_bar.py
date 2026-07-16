import sys
import tkinter as tk

class MenuBar:
    def __init__(self, master, on_export):
        self.on_export = on_export

        # Create main top level Menubar
        self.master = master
        self.menubar = tk.Menu(master)

            # 2. Create individual sub-menus (e.g., File Menu)
        self.file_menu = tk.Menu(self.menubar, tearoff=0)
                # 3. Add items and actions to the sub-menu
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Export", command=self.export)
        self.file_menu.add_separator()  # Visual line separator
        self.file_menu.add_command(label="Exit", command=self.exit_app)

            # 4. Cascade (anchor) the sub-menu to the main Menubar
        self.menubar.add_cascade(label="File", menu=self.file_menu)

            # 5. Add another placeholder sub-menu
        self.help_menu = tk.Menu(self.menubar, tearoff=0)
        self.help_menu.add_command(label="About")
        self.menubar.add_cascade(label="Help", menu=self.help_menu)

        # 6. Assign the configured menubar to the window
        master.config(menu=self.menubar)

    def export(self):
        self.on_export()
        print(" Export pressed, calling from MenuBar....")

    def new_file():
        print("New File Created")

    def exit_app():
        sys.exit(0)

