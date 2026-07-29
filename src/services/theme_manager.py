from ttkbootstrap import Style

class ThemeManager:

    def __init__(self, style: Style):
        self.style = style

    def apply_theme(self, theme_name: str):

        if theme_name == self.style.theme.name:
            return

        self.style.theme_use(theme_name)