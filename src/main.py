from modules.ActivityManager import ActivityManager, pause_event
from interfaces.Message import show_message_with_countdown
import asyncio

activity_manager_instance = ActivityManager()
asyncio.run(activity_manager_instance.start())
message = "Es hora de hacer una pausa. Levántate y estira las piernas por 1 min."
duration = 60  # Duración en segundos del mensaje

while True:
    pause_event.wait()
    print("Cuando se pausa debería llegar acá")
    show_message_with_countdown(message, duration)