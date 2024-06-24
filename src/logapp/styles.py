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
    background_color = '#ffffff'
    input_background_color = '#ffffff'
    input_text_color = '#333333'

    # Box Styles
    login_box_style = Pack(direction=COLUMN, padding=20, alignment=CENTER, background_color=background_color)
    admin_box_style = Pack(direction=COLUMN, padding=20, alignment=CENTER, background_color=background_color)
    user_box_style = Pack(direction=COLUMN, padding=20, alignment=CENTER, background_color=background_color)

    # TextInput Styles
    input_style = Pack(padding=10, width=250, font_size=16, background_color=input_background_color, color=input_text_color)

    # Button Styles
    button_style = Pack(padding=10, width=150, alignment=CENTER, font_size=16, background_color=primary_color, color=text_color)
    add_user_button_style = Pack(padding=10, width=150, alignment=CENTER, font_size=16, background_color=success_color, color=text_color)
    logout_button_style = Pack(padding=10, width=150, alignment=CENTER, font_size=16, background_color=danger_color, color=text_color)

    # Label Styles
    label_style = Pack(padding=5, font_size=14, color=text_color)
    title_label_style = Pack(padding=5, font_size=18, font_weight='bold', color=primary_color)

    # Switch Styles
    switch_style = Pack(padding=10, width=150, alignment=CENTER, background_color=background_color)

    # Table Styles
    table_style = Pack(padding=10, font_size=14, background_color=background_color, color=text_color)

    # Message Styles
    message_style = Pack(padding=5, font_size=14, color=danger_color)

    # Logo Styles
    app_logo_style = Pack(padding=10, width=150, alignment=CENTER, background_color=background_color)

class DarkThemeStyles:
    # General Colors
    primary_color = '#1e88e5'
    secondary_color = '#e53935'
    accent_color = '#ffb300'
    text_color = '#ffffff'
    success_color = '#43a047'
    warning_color = '#ffeb3b'
    danger_color = '#e53935'
    background_color = '#121212'
    input_background_color = '#333333'
    input_text_color = '#ffffff'

    # Box Styles
    login_box_style = Pack(direction=COLUMN, padding=20, alignment=CENTER, background_color=background_color)
    admin_box_style = Pack(direction=COLUMN, padding=20, alignment=CENTER, background_color=background_color)
    user_box_style = Pack(direction=COLUMN, padding=20, alignment=CENTER, background_color=background_color)

    # TextInput Styles
    input_style = Pack(padding=10, width=250, font_size=16, background_color=input_background_color, color=input_text_color)

    # Button Styles
    button_style = Pack(padding=10, width=150, alignment=CENTER, font_size=16, background_color=primary_color, color=text_color)
    add_user_button_style = Pack(padding=10, width=150, alignment=CENTER, font_size=16, background_color=success_color, color=text_color)
    logout_button_style = Pack(padding=10, width=150, alignment=CENTER, font_size=16, background_color=danger_color, color=text_color)

    # Label Styles
    label_style = Pack(padding=5, font_size=14, color=text_color)
    title_label_style = Pack(padding=5, font_size=18, font_weight='bold', color=primary_color)

    # Switch Styles
    switch_style = Pack(padding=10, width=150, alignment=CENTER, background_color=background_color)

    # Table Styles
    table_style = Pack(padding=10, font_size=14, background_color=background_color, color=text_color)

    # Message Styles
    message_style = Pack(padding=5, font_size=14, color=danger_color)

    # Logo Styles
    app_logo_style = Pack(padding=10, width=150, alignment=CENTER, background_color=background_color)
