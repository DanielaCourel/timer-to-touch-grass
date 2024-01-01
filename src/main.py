from modules.ActivityManager import ActivityManager, pause_event, new_connection, inactive_event
from interfaces.Message import show_message_with_countdown

activity_manager = ActivityManager()
pause_message = "Es hora de hacer una pausa. \n Levántate y estira las piernas por 1 min.\n"
duration = 60  # Duración en segundos del mensaje

while True:
    try:
        activity_manager.stop_threads_and_reset()
        activity_manager.start()
        pause_event.wait()
        if not inactive_event.is_set():
            show_message_with_countdown(pause_message, duration)
        new_connection.wait()
    except Exception as e:
        print(f"Error in main loop: {e}")
