from modules.ActivityManager import ActivityManager, pause_event, new_connection, inactive_event
from interfaces.Message import show_message_with_countdown

activity_manager = ActivityManager()
timer = 1500 # Duranción en segundos del timer
pause = 300  # Duración en segundos del mensaje
interactive = False

while True:
    try:
        activity_manager.start(timer, pause, interactive)
        pause_event.wait()
        if not inactive_event.is_set():
            show_message_with_countdown(pause)
        new_connection.wait()
    except Exception as e:
        print(f"Error in main loop: {e}")
