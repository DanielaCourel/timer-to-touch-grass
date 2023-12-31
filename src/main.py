from modules.ActivityManager import ActivityManager, pause_event, new_connection
from interfaces.Message import show_message_with_countdown
import asyncio

activity_manager_instance = ActivityManager()
message = "Es hora de hacer una pausa. Levántate y estira las piernas por 1 min."
duration = 6  # Duración en segundos del mensaje

while True:
    activity_manager_instance.start()
    pause_event.wait()
    show_message_with_countdown(message, duration)
    new_connection.wait()
    new_connection.clear()
    pause_event.clear()