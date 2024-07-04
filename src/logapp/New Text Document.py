import toga
from toga.style import Pack
from toga.style.pack import COLUMN
import os
import json
from mentat import Mentat
from mentat.session_context import SessionContext, SESSION_CONTEXT
from mentat.config import Config


class MentatApp(toga.App):
    def startup(self):
        self.settings_file = "settings.json"
        self.settings = self.load_settings()

        # Create the main window
        self.main_window = toga.MainWindow(title=self.formal_name)

        # Create the main box
        main_box = toga.Box(style=Pack(direction=COLUMN, padding=10))

        self.filepath = None
        self.file_label = toga.Label("No file or directory selected", style=Pack(flex=1))

        choose_file_button = toga.Button("Choose File", on_press=self.choose_file, style=Pack(padding=5))
        choose_dir_button = toga.Button("Choose Directory", on_press=self.choose_directory, style=Pack(padding=5))
        run_button = toga.Button("Run Mentat", on_press=self.run_mentat, style=Pack(padding=5))

        main_box.add(self.file_label)
        main_box.add(choose_file_button)
        main_box.add(choose_dir_button)
        main_box.add(run_button)

        # Create the settings command
        settings_command = toga.Command(
            text='Settings',
            action=self.open_settings,
            group=toga.Group.FILE,
            order=3
        )
        self.commands.add(settings_command)
        # Add the command to the toolbar
        #self.main_window.toolbar.add(settings_command)

        self.main_window.content = main_box
        self.main_window.show()

    def load_settings(self):
        if os.path.exists(self.settings_file):
            with open(self.settings_file, "r") as f:
                return json.load(f)
        return {}

    def save_settings(self, OPENAI_API_KEY, ai_module):
        self.settings["OPENAI_API_KEY"] = OPENAI_API_KEY
        self.settings["ai_module"] = ai_module
        with open(self.settings_file, "w") as f:
            json.dump(self.settings, f)
        self.main_window.info_dialog("Info", "Settings Saved")

    async def choose_file(self, widget):
        try:
            self.filepath = await self.main_window.open_file_dialog("Choose File")
            if self.filepath:
                self.file_label.text = f"Selected: {self.filepath}"
            else:
                self.file_label.text = "No file selected"
        except Exception as e:
            self.main_window.error_dialog("Error", f"An error occurred while choosing a file: {e}")
            self.file_label.text = "Error selecting file"
    
    async def choose_directory(self, widget):
        try:
            self.filepath = await self.main_window.select_folder_dialog("Choose Directory")
            if self.filepath:
                self.file_label.text = f"Selected: {self.filepath}"
            else:
                self.file_label.text = "No directory selected"
        except Exception as e:
            self.main_window.error_dialog("Error", f"An error occurred while choosing a directory: {e}")
            self.file_label.text = "Error selecting directory"

    def run_mentat(self, widget):
        if not self.filepath:
            self.main_window.error_dialog("Error", "No file or directory selected")
            return

        # Create a configuration object
        config = Config(
            #model : str
            #provider : ["openai", "anthropic", "azure"]
            #maximum_context : int

        )

        # Initialize Mentat
        mentat_client = Mentat(config)

        # Create a session context
        session_context = SessionContext(self.filepath)

        # Run Mentat
        try:
            response = mentat_client.run(session_context)
            if response.success:
                # Handle successful response
                with open(self.filepath, "w") as f:
                    f.write(response.code)
                self.main_window.info_dialog("Info", "Mentat has processed the file(s)")
            else:
                # Handle error response
                self.main_window.error_dialog("Error", "Mentat encountered an error")
        except Exception as e:
            # Handle any exceptions
            self.main_window.error_dialog("Error", str(e))

    def open_settings(self, widget):
        settings_box = toga.Box(style=Pack(direction=COLUMN, padding=10))

        api_key_input = toga.TextInput(placeholder="API Key", value=self.settings.get("api_key", ""), style=Pack(flex=1))
        ai_module_input = toga.TextInput(placeholder="AI Module", value=self.settings.get("ai_module", ""), style=Pack(flex=1))

        save_button = toga.Button("Save", on_press=lambda x: self.save_settings(api_key_input.value, ai_module_input.value), style=Pack(padding=5))

        settings_box.add(toga.Label("API Key:", style=Pack(padding=(0, 5))))
        settings_box.add(api_key_input)
        settings_box.add(toga.Label("AI Module:", style=Pack(padding=(0, 5))))
        settings_box.add(ai_module_input)
        settings_box.add(save_button)

        settings_window = toga.Window(title="Settings")
        settings_window.content = settings_box
        settings_window.show()

def main():
    return MentatApp()

if __name__ == '__main__':
    main().main_loop()
