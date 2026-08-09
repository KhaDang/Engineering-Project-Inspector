import tkinter as tk
from workflows.menubar_configs import MenubarConfig

# Import interfaces
from observer import Observer

class MenuBar(Observer):
    def __init__(self,
                 master,
                 state,
                 blind_events,
                ):

        self.sub_menu = {}

        config = MenubarConfig(blind_events)

        self.menubar = tk.Menu(master)

        self.add_menu("File", config.FILE_MENU)
        self.add_menu("Edit", config.EDIT_MENU)
        self.add_menu("Theme", config.THEME_MENU)

        state.add_observer(self)  # Add Menubar into observers

        master.config(menu=self.menubar)


    def add_menu(self, menu_label, menu_commands):
        submenu = tk.Menu(self.menubar, tearoff=False)
        for item in menu_commands:

            if item.separator:
                submenu.add_separator()
                continue
            submenu.add_command(label=item.label, command=item.command)

            if item.is_enable:
                submenu.entryconfig(item.label, state='normal')
            else:
                submenu.entryconfig(item.label, state='disable')

        self.menubar.add_cascade(label=menu_label ,menu=submenu)

        # Add submenu to a dictionary
        self.sub_menu[menu_label] =  submenu


    def set_enabled(
            self,
            label,
            menu_name,

                ):
        self.sub_menu[label].entryconfig(menu_name, state='normal')

    def set_disabled(
            self,
            label,
            menu_name,

                ):
        self.sub_menu[label].entryconfig(menu_name, state='disable')

    def update(self, state):
            if state.comparison_results:
                self.set_enabled(label='File', menu_name='Export Report')
                self.set_enabled(label='File', menu_name='Find missing files...')
                self.set_enabled(label='Edit', menu_name='Clear')

            else:
                self.set_disabled(label='File', menu_name='Export Report')
                self.set_disabled(label='File', menu_name='Find missing files...')
                self.set_disabled(label='Edit', menu_name='Clear')

        # self.set_enabled(sub_menu='File', menu_name='Find missing')
