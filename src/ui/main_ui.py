import ttkbootstrap as tb
from ttkbootstrap.constants import *

# Import your custom tabs from separate files
from ui.tabs.tab_bom_to_folder import BomToFolder
from ui.tabs.tab_folder_to_bom import FolderToBOM
from ui.tabs.tab_folder_to_folder import FolderToFolder
from ui.tabs.tab_compare_two_files import FileToFile



# Initialize main application
app = tb.Window(themename="superhero")
app.title("Engineering File Manager")
app.geometry("1000x800")

# Create the Notebook widget
notebook = tb.Notebook(app, bootstyle="primary")
notebook.pack(padx=20, pady=20, fill=BOTH, expand=True)

# Instantiate the tab objects (passing the notebook as the parent container)
bom_to_folder_tab = BomToFolder(notebook)
folder_to_bom_tab = FolderToBOM(notebook)
folder_to_folder_tab = FolderToFolder(notebook)
file_to_file_tab = FileToFile(notebook)

# Link the modular tab objects to the notebook tabs
notebook.add(bom_to_folder_tab, text="BOM -> Project Folder")
notebook.add(folder_to_bom_tab, text="Project Folder -> BOM")
notebook.add(folder_to_folder_tab, text="Folder -> Folder")
notebook.add(file_to_file_tab, text="Compare 2 files")

app.mainloop()
