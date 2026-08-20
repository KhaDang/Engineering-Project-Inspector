import ttkbootstrap as ttk

class FileTypePopup(ttk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.tip_window = None

        # self.popup = ttk.Toplevel(size=(150, 100))
        # print('Popup window is created!!!')
        # self.popup.overrideredirect(True)
        # self.popup.withdraw()
        #
        #
        # record_label = ttk.Label(
        #     self.popup,
        #     text="Drawing record",
        #     width=15
        # )
        # record_label.pack(fill='x')
        #
        # columns = ['Type', 'Left', 'Right']
        #
        # self.tree = ttk.Treeview(self.popup, height=18, columns=columns, show='headings')
        # # Add headings for Treeview table
        # for col in columns:
        #     self.tree.heading(col, text=col, anchor ='w')
        #     self.tree.column(col, width=120, anchor='w')
        # # pack
        # self.tree.pack(side="left", expand=True, fill="both", pady=5)

        # self.popup.transient(master)
        # # popup.attributes('-topmost', True)  # Keeps window above others
        # self.popup.place_window_center()

    def show_tip(self, x, y, text):
        if self.tip_window:
            return
        self.tip_window = tw = ttk.Toplevel(size=(150, 100))
        tw.overrideredirect(True)  # Remove window borders
        tw.geometry(f"+{x + 15}+{y + 15}")  # Offset from cursor
        label = ttk.Label(tw, text=text, relief="solid", borderwidth=1, font=("Arial", 10))
        label.pack()

    def update_tip(self, x, y):
        if self.tip_window:
            self.tip_window.geometry(f"+{x + 15}+{y + 15}")

    def hide_tip(self):
        if self.tip_window:
            self.tip_window.destroy()
            self.tip_window = None

    def on_click(self, event):
        # Show text pinned or following on click
        self.show_tip(event.x_root, event.y_root, "Floating Description!")

    def on_motion(self, event):
        # Update position while dragging
        self.update_tip(event.x_root, event.y_root)

    def on_release(self, event):
        # Hide description when click is released (optional)
        self.hide_tip()