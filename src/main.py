from modules.ActivityManager import ActivityManager, pause_event, new_connection, inactive_event
from interfaces.Message import show_message_with_countdown
import asyncio

activity_manager_instance = ActivityManager()
message = "Es hora de hacer una pausa. Levántate y estira las piernas por 1 min."
duration = 6  # Duración en segundos del mensaje

while True:
    activity_manager_instance.stop_threads_and_reset()
    activity_manager_instance.start()
    pause_event.wait()
    if not inactive_event.is_set():
        show_message_with_countdown(message, duration)
    new_connection.wait()