import ttkbootstrap as tb
from ttkbootstrap.constants import *

# Import your custom tabs from separate files
from ui.components.tab_bom_to_folder import BomToFolder
from ui.components.tab_folder_to_bom import FolderToBOM

# Initialize main application
app = tb.Window(themename="superhero")
app.title("Engineering File Manager")
app.geometry("800x600")

# Create the Notebook widget
notebook = tb.Notebook(app, bootstyle="primary")
notebook.pack(padx=20, pady=20, fill=BOTH, expand=True)

# Instantiate the tab objects (passing the notebook as the parent container)
profile_tab = BomToFolder(notebook)
settings_tab = FolderToBOM(notebook)

# Link the modular tab objects to the notebook tabs
notebook.add(profile_tab, text="BOM -> Project Folder")
notebook.add(settings_tab, text="Project Folder -> BOM")

app.mainloop()
