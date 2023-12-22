import time
import threading
from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener
import asyncio

pause_event = threading.Event()

class ActivityManager:
    def __init__(self):
        self.timer_user = 0
        self.timer_inactive = 0
        self.pause = False
        self.connect = True
        self.PAUSE_TIME = 1800
        self.pause_timer = None
        self.suspend_time = 60

    def pause_program(self):
        self.pause = True
        self.connect = False
        pause_event.set()
        time.sleep(self.suspend_time)
        self.pause = False
        self.pause_timer = None

    def timer_of_activity(self):
        while self.connect:
            time.sleep(1)
            self.timer_user += 1
            print("time1:", self.timer_user)
            if self.timer_user >= self.PAUSE_TIME:
                self.pause_timer = threading.Thread(target=self.pause_program)
                self.pause_timer.start()

    def time_without_activity(self):
        while self.connect:
            time.sleep(1)
            self.timer_inactive += 1
            print("time2:", self.timer_inactive)
            if self.timer_inactive >= 10:
                print("acá debería considerarse la inactividad")
                self.connect = False
                self.timer_inactive = 0
                self.timer_user = 0
                pause_event.wait()

    def have_interaction(self, *args):
        print("skdfjkasjdf")
        self.timer_inactive = 0
        if not self.connect and self.pause_timer is None:
            print("ahora acá debería llegar cuando haya actividad de nuevo...")
            self.connect = True
            pause_event.clear()

    async def start_listeners(self):
        async def async_mouse_listener():
            listener = MouseListener(on_move=self.have_interaction, on_click=self.have_interaction, on_scroll=self.have_interaction)
            listener.start()
            await asyncio.sleep(0.1)  # Permitir que el listener se inicie
            listener.join()

        async def async_keyboard_listener():
            listener = KeyboardListener(on_press=self.have_interaction)
            listener.start()
            await asyncio.sleep(0.1)  # Permitir que el listener se inicie
            listener.join()

        await asyncio.gather(
            async_mouse_listener(),
            async_keyboard_listener()
        )

    async def start(self):
        asyncio.create_task(self.start_listeners())
        await asyncio.sleep(0.1)
        asyncio.create_task(self.time_without_activity())
        asyncio.create_task(self.timer_of_activity())
        
