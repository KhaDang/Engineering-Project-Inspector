import ttkbootstrap as tb
from ttkbootstrap.constants import *

# Import your custom controllers from separate files
from controllers.file_inspector import FilesInspector
from controllers.revision_inspector import RevisionsInspector
# from controllers.tab_folder_to_folder import FolderToFolder
# from controllers.tab_compare_two_files import FileToFile


# Import Menu bar
from views.menu_bar import MenuBar
from views.menu_bar import MenuBarEventHandler

class EngineeringFileManagerApp:

    def __init__(self):

        self.create_window()

        self.create_menu()

        self.create_notebook()

        self.create_statusbar()

        self.bind_events()

        # self.load_settings()


    def create_window(self):
        self.app = tb.Window(themename="superhero")
        self.app.title("Engineering File Manager")
        self.app.geometry("1100x860")

    def create_notebook(self):
        self.notebook = tb.Notebook(self.app, bootstyle="primary")
        self.notebook.pack(padx=20, pady=20, fill=BOTH, expand=True)

        # Instantiate the tab objects (passing the notebook as the parent container)
        self.bom_to_folder_tab = FilesInspector(self.notebook)
        self.folder_to_bom_tab = RevisionsInspector(self.notebook)
        # self.folder_to_folder_tab = FolderToFolder(self.notebook)
        # self.file_to_file_tab = FileToFile(self.notebook)

        # Link the modular tab objects to the notebook controllers
        self.notebook.add(self.bom_to_folder_tab, text="Files Inspector")
        self.notebook.add(self.folder_to_bom_tab, text="Revision Inspector")
        # self.notebook.add(self.folder_to_folder_tab, text="Folder -> Folder")
        # self.notebook.add(self.file_to_file_tab, text="Compare 2 files")

    def run(self):
        self.app.mainloop()

    def create_menu(self):
        bind_menubar_events = MenuBarEventHandler(
            self.on_export,
            self.load_settings,
            self.on_clear

        )
        MenuBar(self.app, bind_menubar_events)
    def create_statusbar(self):
        ...
    def bind_events(self):
        ...
    def load_settings(self):
        ...
    def on_export(self):
        self.bom_to_folder_tab.export_report()

    def on_clear(self):
        self.bom_to_folder_tab.on_clear()

