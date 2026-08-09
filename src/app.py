import sys
import os

import ttkbootstrap as tb
from ttkbootstrap.constants import *

# Import your custom controllers from separate files
from controllers.file_inspector import FilesInspector
from controllers.revision_inspector import RevisionsInspector
from controllers.folder_inspector import FolderInspector
from services.theme_manager import ThemeManager

# Import Tools
from controllers.tools.copy_missing_controller import CopyMissingController

# Import Menu bar
from views.menu_bar import MenuBar

# Import app_setting
from workflows.app_settings import Settings


class EngineeringFileManagerApp:

    def __init__(self, state):

        self.state = state

        self.settings = Settings.load()

        self.create_window()
        # Have to be initialized after window - Window itself has theme
        self.theme_manager = ThemeManager(tb.Style(self.settings.theme))

        self.create_menu()

        self.create_notebook()


    def create_window(self):
        self.app = tb.Window(themename=self.settings.theme)

        self.app.title("Engineering File Manager")

        icon_path = self.get_resource_path("src/assets/engineering.ico")
        self.app.iconbitmap(icon_path)

        self.app.geometry(f"{self.settings.window_width}x{self.settings.window_height}")

    def create_notebook(self):
        self.notebook = tb.Notebook(self.app, bootstyle="primary")
        self.notebook.pack(padx=20, pady=20, fill=BOTH, expand=True)

        # Instantiate the tab objects (passing the notebook as the parent container)
        self.files_inspector = FilesInspector(self.notebook, self.state)
        self.revision_inspector = RevisionsInspector(self.notebook, self.state)
        self.folder_inspector = FolderInspector(self.notebook, self.state)

        # Link the modular tab objects to the notebook controllers
        self.notebook.add(self.files_inspector, text="Files Inspector")
        self.notebook.add(self.revision_inspector, text="Revision Inspector")
        self.notebook.add(self.folder_inspector, text="Folder Inspector")
        # self.notebook.add(self.file_to_file_tab, text="Compare 2 files")

        self.notebook.bind(
            "<<NotebookTabChanged>>",
            self.on_tab_changed
        )
    def run(self):


        self.app.mainloop()

    def create_menu(self):
        bind_menubar_events = {
            'on_export': self.on_export,
            'load_setting' : self.load_settings,
            'on_clear': self.on_clear,
            'on_exit': self.on_exit,
            'on_popup': self.open_popup,
            'on_theme_changed': self.on_theme_changed,

        }
        MenuBar(self.app, self.state, bind_menubar_events)
        

    def on_exit(self):
        sys.exit()

    def bind_events(self):
        ...
    def load_settings(self):
        ...
    def on_export(self):

        current_tab_object = self.notebook.nametowidget(self.notebook.select())

        current_tab_object.export_report()

    def on_clear(self):
        current_tab_object = self.notebook.nametowidget(self.notebook.select())

        current_tab_object.on_clear()

    def on_theme_changed(self, theme_name):
        # Switch the entire window theme dynamically

        self.theme_manager.apply_theme(theme_name)

        # Save theme_name for next run
        self.settings.theme = theme_name
        self.settings.save()


    def open_popup(self):

        current_tab_object = self.notebook.nametowidget(self.notebook.select())

        # if current_tab_object.get_result():
        copy_missing_controller = CopyMissingController(
            parent=self.app,
            comparison_result=current_tab_object.get_result()
        )
        copy_missing_controller.show()
        # else:
        #     print("Nothing to copy")


    def get_resource_path(self,relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

    def on_tab_changed(self, event):
        current_tab_object = self.notebook.nametowidget(self.notebook.select())
        self.state.comparison_results = current_tab_object.get_result()
        self.state.comparison_completed = True if self.state.comparison_results else False


        selected_widget = str(
                            event.widget.nametowidget(
                                event.widget.select()
                            )
        )

        for tab in self.notebook.tabs():

            if tab == selected_widget:
                self.state.set_current_tab(tab)
                break


        ## Helpful debug
        # print("----------------")
        # print("update_base_record")
        # print("self =", self)
        # print("class =", self.__class__.__name__)
        # print("attributes =", self.__dict__.keys())
