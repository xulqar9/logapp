from .styles import LightThemeStyles, DarkThemeStyles

class ThemeManager:
    def __init__(self):
        self.light_theme = LightThemeStyles
        self.dark_theme = DarkThemeStyles
        self.current_theme = self.light_theme

    def switch_to_light(self):
        self.current_theme = self.light_theme

    def switch_to_dark(self):
        self.current_theme = self.dark_theme
