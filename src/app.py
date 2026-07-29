import ttkbootstrap as tb
from ttkbootstrap.constants import *

# Import your custom controllers from separate files
from controllers.file_inspector import FilesInspector
from controllers.revision_inspector import RevisionsInspector
from controllers.folder_inspector import FolderInspector
# from controllers.tab_compare_two_files import FileToFile
from services.theme_manager import ThemeManager

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

        self.theme_manager = ThemeManager()

    def create_window(self):
        self.app = tb.Window(themename="cosmo")
        self.app.title("Engineering File Manager")
        self.app.geometry("1100x860")

    def create_notebook(self):
        self.notebook = tb.Notebook(self.app, bootstyle="primary")
        self.notebook.pack(padx=20, pady=20, fill=BOTH, expand=True)

        # Instantiate the tab objects (passing the notebook as the parent container)
        self.files_inspector = FilesInspector(self.notebook)
        self.revision_inspector = RevisionsInspector(self.notebook)
        self.folder_inspector = FolderInspector(self.notebook)
        # self.file_to_file_tab = FileToFile(self.notebook)

        # Link the modular tab objects to the notebook controllers
        self.notebook.add(self.files_inspector, text="Files Inspector")
        self.notebook.add(self.revision_inspector, text="Revision Inspector")
        self.notebook.add(self.folder_inspector, text="Folder -> Folder")
        # self.notebook.add(self.file_to_file_tab, text="Compare 2 files")

    def run(self):
        self.app.mainloop()

    def create_menu(self):
        bind_menubar_events = MenuBarEventHandler(
            self.on_export,
            self.load_settings,
            self.on_clear

        )
        MenuBar(self.app, bind_menubar_events, update_theme=self.on_theme_changed)
    def create_statusbar(self):
        ...
    def bind_events(self):
        ...
    def load_settings(self):
        ...
    def on_export(self):

        current_tab_object = self.notebook.nametowidget(self.notebook.select())

        current_tab_object.export_report()

    def on_clear(self):
        self.files_inspector.on_clear()

    def on_theme_changed(self, theme_name):
        # Switch the entire window theme dynamically
        self.theme_manager.apply_theme(theme_name)