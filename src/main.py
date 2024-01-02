from modules.ActivityManager import ActivityManager, pause_event, new_connection, inactive_event
from interfaces.Message import show_message_with_countdown
from interfaces.Menu import SettingsWindow

settings_window = SettingsWindow()
settings_window.open_settings_window()

while not settings_window.ready:
    pass

activity_manager = ActivityManager()
timer = settings_window.activity_time
pause = settings_window.pause_time
interactive = settings_window.interactive

while True:
    try:
        activity_manager.start(timer, pause, interactive)
        pause_event.wait()
        if not inactive_event.is_set():
            show_message_with_countdown(pause)
        new_connection.wait()
    except Exception as e:
        print(f"Error in main loop: {e}")
