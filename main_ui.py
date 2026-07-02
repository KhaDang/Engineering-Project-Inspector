import ttkbootstrap as tb
from ttkbootstrap.constants import *

# Import your custom tabs from separate files
from tab_Profile import ProfileTab
from tab_setting import SettingsTab

# Initialize main application
app = tb.Window(themename="superhero")
app.title("Modular Notebook UI")
app.geometry("500x400")

# Create the Notebook widget
notebook = tb.Notebook(app, bootstyle="primary")
notebook.pack(padx=20, pady=20, fill=BOTH, expand=True)

# Instantiate the tab objects (passing the notebook as the parent container)
profile_tab = ProfileTab(notebook)
settings_tab = SettingsTab(notebook)

# Link the modular tab objects to the notebook tabs
notebook.add(profile_tab, text="User Profile")
notebook.add(settings_tab, text="Settings")

app.mainloop()
