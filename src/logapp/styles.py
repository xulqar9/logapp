from toga.style import Pack
from toga.style.pack import COLUMN, CENTER, LEFT

class LightThemeStyles:
    # General Colors
    primary_color = '#4a90e2'
    secondary_color = '#d0021b'
    accent_color = '#f5a623'
    text_color = '#333333'
    success_color = '#7ed321'
    warning_color = '#f8e71c'
    danger_color = '#d0021b'
    background_color = '#a0a0a0'
    input_background_color = '#868686'
    input_text_color = '#333333'

    # Box Styles
    login_box_style = Pack(direction=COLUMN, padding=0, alignment=CENTER, background_color=background_color)
    admin_box_style = Pack(direction=COLUMN, padding=0, alignment=CENTER, background_color=background_color)
    user_box_style = Pack(direction=COLUMN, padding=0, alignment=CENTER, background_color=background_color)

    # TextInput Styles
    input_style = Pack(padding=10, width=250, font_size=16, background_color=input_background_color, color=input_text_color)

    # Button Styles
    button_style = Pack(padding=10, width=200, alignment=CENTER, font_size=16, background_color=primary_color, color='#ffffff')
    add_user_button_style = Pack(padding=10, width=200, alignment=CENTER, font_size=16, background_color=success_color, color='#ffffff')
    logout_button_style = Pack(padding=10, width=200, alignment=CENTER, font_size=16, background_color=danger_color, color='#ffffff')

    # Label Styles
    label_style = Pack(padding=5, font_size=14, color=text_color)
    title_label_style = Pack(padding=5, font_size=20, font_weight='bold', color=primary_color)

    # Switch Styles
    switch_style = Pack(padding=10, width=150, alignment=CENTER, background_color=background_color)

    # Table Styles
    table_style = Pack(padding=10, font_size=14, background_color=background_color, color=text_color)

    # Message Styles
    message_style = Pack(padding=5, font_size=14, color=danger_color)

    # Logo Styles
    app_logo_style = Pack(padding=20, width=150, alignment=CENTER, background_color=background_color)

class DarkThemeStyles:
    # General Colors
    primary_color = '#1E1E1E'           # A very dark gray for primary elements
    secondary_color = '#2D2D2D'         # A slightly lighter gray for secondary elements
    accent_color = '#007ACC'            # A bright blue for accentuating important elements
    text_color = '#D4D4D4'              # A light gray for text to ensure readability
    success_color = '#28A745'           # A green color to indicate success
    warning_color = '#FFC107'           # A yellow color to indicate warnings
    danger_color = '#DC3545'            # A red color to indicate errors or danger
    background_color = '#121212'        # A very dark gray/black for the background
    input_background_color = '#333333'  # A dark gray for input fields
    input_text_color = '#FFFFFF'        # White for text within input fields


    # Box Styles
    login_box_style = Pack(direction=COLUMN, padding=0, alignment=CENTER, background_color="#414141")
    admin_box_style = Pack(direction=COLUMN, padding=0, alignment=CENTER, background_color="#414141")
    user_box_style = Pack(direction=COLUMN, padding=0, alignment=CENTER, background_color="#414141")

    # TextInput Styles
    input_style = Pack(padding=10, width=250, font_size=16, background_color=input_background_color, color="#ffffff")

    # Button Styles
    button_style = Pack(padding=10, width=200, alignment=CENTER, font_size=16, background_color=primary_color)
    add_user_button_style = Pack(padding=10, width=200, alignment=CENTER, font_size=16, background_color=success_color)
    logout_button_style = Pack(padding=10, width=200, alignment=CENTER, font_size=16, background_color=danger_color)

    # Label Styles
    label_style = Pack(padding=5, font_size=14, color=text_color)
    title_label_style = Pack(padding=5, font_size=20, font_weight='bold', color=primary_color)

    # Switch Styles
    switch_style = Pack(padding=10, width=150, alignment=CENTER, background_color=background_color)

    # Table Styles
    table_style = Pack(padding=10, font_size=14, background_color=background_color, color=text_color)

    # Message Styles
    message_style = Pack(padding=5, font_size=14, color=danger_color)

    # Logo Styles
    app_logo_style = Pack(padding=20, width=150, alignment=CENTER, background_color="#414141")
