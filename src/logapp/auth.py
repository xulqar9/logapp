import hashlib
import toga
from toga.style import Pack
import calendar
from datetime import datetime, timedelta
from .database import authenticate_user, is_admin_user, add_user_to_db, get_all_users, get_user_check_ins, insert_check_in, update_check_out, get_open_check_in
from .theme_manager import ThemeManager

# Initialize ThemeManager to use the current theme
theme_manager = ThemeManager()

def show_message(message, app):
    app.message_box.clear()
    message_label = toga.Label(message, style=theme_manager.current_theme.message_style)
    app.message_box.add(message_label)
    app.refresh_ui()

def authenticate(username, password):
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    return authenticate_user(username, password_hash)

def is_admin(username):
    return is_admin_user(username)

def calculate_work_hours(check_ins):
    total_seconds = 0
    for check_in in check_ins:
        if check_in['check_out_time'] != 'N/A':
            check_in_time = datetime.strptime(check_in['check_in_time'], '%H:%M - %d/%m/%Y')
            check_out_time = datetime.strptime(check_in['check_out_time'], '%H:%M - %d/%m/%Y')
            total_seconds += (check_out_time - check_in_time).total_seconds()
    total_hours = total_seconds / 3600
    return round(total_hours, 2)

def setup_admin_ui(admin_box, app):
    admin_box.clear()

    username_input = toga.TextInput(placeholder='Username', style=theme_manager.current_theme.input_style)
    password_input = toga.PasswordInput(placeholder='Password', style=theme_manager.current_theme.input_style)
    is_admin_input = toga.Switch('Is Admin', style=theme_manager.current_theme.switch_style)

    add_user_button = toga.Button('Add User', on_press=lambda widget: add_user(username_input.value, password_input.value, is_admin_input.value, app), style=theme_manager.current_theme.add_user_button_style)
    logout_button = toga.Button('Logout', on_press=lambda widget: logout(widget, app), style=theme_manager.current_theme.logout_button_style)

    admin_box.add(username_input)
    admin_box.add(password_input)
    admin_box.add(is_admin_input)
    admin_box.add(add_user_button)
    admin_box.add(logout_button)

    users_check_ins_label = toga.Label('Users Check-ins and Check-outs:', style=theme_manager.current_theme.label_style)
    admin_box.add(users_check_ins_label)

    check_in_table = toga.Table(
        headings=['Username', 'Check-in Time', 'Check-out Time'],
        data=[(user['username'], check_in['check_in_time'], check_in['check_out_time']) for user in get_all_users() for check_in in get_user_check_ins(user['username'])],
        style=theme_manager.current_theme.table_style
    )
    admin_box.add(check_in_table)

    app.refresh_ui()

def setup_user_ui(user_box, app):
    user_box.clear()

    check_in_button = toga.Button('Check In', on_press=lambda widget: check_in(widget, app), style=theme_manager.current_theme.button_style)
    check_out_button = toga.Button('Check Out', on_press=lambda widget: check_out(widget, app), style=theme_manager.current_theme.button_style)
    logout_button = toga.Button('Logout', on_press=lambda widget: logout(widget, app), style=theme_manager.current_theme.logout_button_style)

    user_box.add(check_in_button)
    user_box.add(check_out_button)
    user_box.add(logout_button)

    current_month_name = calendar.month_name[datetime.now().month]
    user_check_ins_label = toga.Label(f'Your Check-ins and Check-outs for {current_month_name}:', style=theme_manager.current_theme.label_style)
    user_box.add(user_check_ins_label)

    check_ins = get_user_check_ins(app.current_user)
    current_month = datetime.now().month
    current_month_check_ins = [check_in for check_in in check_ins if datetime.strptime(check_in['check_in_time'], '%H:%M - %d/%m/%Y').month == current_month]
    
    check_in_table = toga.Table(
        headings=['Check-in Time', 'Check-out Time'],
        data=[(check_in['check_in_time'], check_in['check_out_time']) for check_in in current_month_check_ins],
        style=theme_manager.current_theme.table_style
    )
    user_box.add(check_in_table)

    current_week_check_ins = [check_in for check_in in check_ins if datetime.strptime(check_in['check_in_time'], '%H:%M - %d/%m/%Y').isocalendar()[1] == datetime.now().isocalendar()[1]]
    total_hours_week = calculate_work_hours(current_week_check_ins)

    total_hours_label = toga.Label(f'Total Work Hours This Week: {total_hours_week}', style=theme_manager.current_theme.label_style)
    user_box.add(total_hours_label)

    app.refresh_ui()

def add_user(username, password, is_admin, app):
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    add_user_to_db(username, password_hash, is_admin)
    if is_admin:
        show_message("You added a new Admin.", app)
    else:
        show_message("You added a new User.", app)

def check_in(widget, app):
    username = app.current_user
    open_check_in = get_open_check_in(username)
    if open_check_in:
        show_message("You already have an open check-in. Please check out first.", app)
    else:
        insert_check_in(username)
        show_message("Checked in successfully.", app)
        setup_user_ui(app.user_box, app)  # Refresh user UI to show updated check-ins

def check_out(widget, app):
    username = app.current_user
    open_check_in = get_open_check_in(username)
    if not open_check_in:
        show_message("No open check-in found. Please check in first.", app)
    else:
        update_check_out(open_check_in['id'])
        show_message("Checked out successfully.", app)
        setup_user_ui(app.user_box, app)  # Refresh user UI to show updated check-outs

def logout(widget, app):
    app.current_user = None
    app.main_window.content = app.login_box
    app.main_window.show()
    app.refresh_ui()
