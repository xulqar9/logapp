import toga
from toga.style import Pack
from .auth import authenticate, is_admin, setup_admin_ui, setup_user_ui, show_message
from .theme_manager import ThemeManager
from datetime import datetime

class LogApp(toga.App):
    def startup(self):
        self.theme_manager = ThemeManager()
        
        self.main_window = toga.MainWindow(title=self.formal_name)

        # Create groups
        preferences_group = toga.Group('Preferences', parent=toga.Group.FILE, order=1)
        themes_group = toga.Group('Themes', parent=preferences_group, order=2)

        # Create commands for theme switching under the Themes group
        light_theme_command = toga.Command(
            text='Light Theme',
            action=self.set_light_theme,
            group=themes_group,
            order=0
        )

        dark_theme_command = toga.Command(
            text='Dark Theme',
            action=self.set_dark_theme,
            group=themes_group,
            order=1
        )

        self.commands.add(light_theme_command, dark_theme_command)

        self.current_user = None
        self.message_box = toga.Box(style=self.theme_manager.current_theme.message_style)

        self.login_box = self.setup_login_ui()
        self.admin_box = toga.Box()
        self.user_box = toga.Box()

        self.main_window.content = self.login_box
        self.main_window.show()

    def setup_login_ui(self):
        login_box = toga.Box(style=self.theme_manager.current_theme.login_box_style)
        
        app_logo = toga.ImageView(image='resources/logo.png', style=self.theme_manager.current_theme.app_logo_style)
        login_box.add(app_logo)

        username_input = toga.TextInput(placeholder='Username', style=self.theme_manager.current_theme.input_style)
        password_input = toga.PasswordInput(placeholder='Password', style=self.theme_manager.current_theme.input_style)
        login_button = toga.Button('Login', on_press=lambda widget: self.login(username_input.value, password_input.value), style=self.theme_manager.current_theme.button_style)

        login_box.add(username_input)
        login_box.add(password_input)
        login_box.add(login_button)
        login_box.add(self.message_box)

        return login_box

    def login(self, username, password):
        if authenticate(username, password):
            self.current_user = username
            if is_admin(username):
                self.setup_admin_ui()
            else:
                self.setup_user_ui()
        else:
            show_message("Invalid username or password", self)

    def setup_admin_ui(self):
        self.admin_box = toga.Box(style=self.theme_manager.current_theme.admin_box_style)
        setup_admin_ui(self.admin_box, self)
        self.main_window.content = self.admin_box

    def setup_user_ui(self):
        self.user_box = toga.Box(style=self.theme_manager.current_theme.user_box_style)
        setup_user_ui(self.user_box, self)
        self.main_window.content = self.user_box

    def refresh_ui(self):
        self.main_window.content.refresh()

    def set_light_theme(self, widget):
        self.theme_manager.switch_to_light()
        self.apply_theme()

    def set_dark_theme(self, widget):
        self.theme_manager.switch_to_dark()
        self.apply_theme()

    def apply_theme(self):
        self.message_box.style = self.theme_manager.current_theme.message_style
        if self.current_user is None:
            self.main_window.content = self.setup_login_ui()
        elif is_admin(self.current_user):
            self.setup_admin_ui()
        else:
            self.setup_user_ui()

def main():
    return LogApp()
