from modules.ActivityManager import ActivityManager, pause_event, new_connection, inactive_event
from interfaces.Message import show_message_with_countdown

activity_manager = ActivityManager()
timer = 1800 # Duranción en segundos del timer
pause = 60  # Duración en segundos del mensaje

while True:
    try:
        activity_manager.stop_threads_and_reset()
        activity_manager.start(timer, pause)
        pause_event.wait()
        if not inactive_event.is_set():
            show_message_with_countdown(pause)
        new_connection.wait()
    except Exception as e:
        print(f"Error in main loop: {e}")
