from .styles import LightThemeStyles, DarkThemeStyles

class ThemeManager:
    def __init__(self):
        self.light_theme = LightThemeStyles()
        self.dark_theme = DarkThemeStyles()
        self.get_current_theme()
        self.current_theme = self.chossen_current_theme

    def switch_to_light(self):
        self.current_theme = self.light_theme
        self.save_theme_preference()

    def switch_to_dark(self):
        self.current_theme = self.dark_theme
        self.save_theme_preference()

    def save_theme_preference(self):
        with open('theme_preference.txt', 'w') as file:
            file.write('dark' if self.current_theme == self.dark_theme else 'light')
            print(2)

    def get_current_theme(self):
        try:
            with open('theme_preference.txt', 'r') as file:
                theme_preference = file.read().strip()
                if theme_preference == 'dark':
                    self.chossen_current_theme = self.dark_theme
                else:
                    self.chossen_current_theme = self.light_theme
        except FileNotFoundError:
            self.save_theme_preference()
        return self.chossen_current_theme