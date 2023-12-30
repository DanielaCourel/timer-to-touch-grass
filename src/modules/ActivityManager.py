import time
import threading
from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener
import asyncio
import warnings

warnings.filterwarnings("ignore", category=RuntimeWarning)


pause_event = asyncio.Event()

class ActivityManager:
    def __init__(self):
        self.timer_user = 0
        self.timer_inactive = 0
        self.pause = False
        self.connect = True
        self.PAUSE_TIME = 1800
        self.pause_timer = None
        self.suspend_time = 60

    async def pause_program(self):
        self.pause = True
        self.connect = False
        pause_event.set()
        await asyncio.sleep(self.suspend_time)
        self.pause = False
        self.pause_timer = None

    async def timer_of_activity(self):
        while self.connect:
            await asyncio.sleep(1)
            self.timer_user += 1
            print("time1:", self.timer_user)
            if self.timer_user >= self.PAUSE_TIME:
                await self.pause_program()  # Esperar a que pause_program termine

    async def time_without_activity(self):
        while self.connect:
            await asyncio.sleep(1)
            self.timer_inactive += 1
            print("time2:", self.timer_inactive)
            if self.timer_inactive >= 10:
                print("acá debería considerarse la inactividad")
                self.connect = False
                self.timer_inactive = 0
                self.timer_user = 0
                await pause_event.wait()

    async def have_interaction(self, *args):
        print("skdfjkasjdf")
        self.timer_inactive = 0
        if not self.connect and self.pause_timer is None:
            print("ahora acá debería llegar cuando haya actividad de nuevo...")
            self.connect = True
            await pause_event.clear()

    async def on_move_event(self, x, y):
        await self.have_interaction(x, y)

    async def on_click_event(self, x, y, button, pressed):
        await self.have_interaction(x, y, button, pressed)

    async def on_scroll_event(self, x, y, dx, dy):
        await self.have_interaction(x, y, dx, dy)

    async def on_press_event(self, key):
        await self.have_interaction(key)


    async def mouse_listener(self):
        listener = MouseListener(
            on_move=self.on_move_event,
            on_click=self.on_click_event,
            on_scroll=self.on_scroll_event
        )
        listener.start()
        await asyncio.sleep(0.1)

    async def keyboard_listener(self):
        listener = KeyboardListener(on_press=self.on_press_event)
        listener.start()
        await asyncio.sleep(0.1)


    async def start(self):
        task_mouse = self.mouse_listener()
        task_keyboard = self.keyboard_listener()

        await asyncio.gather(task_mouse, task_keyboard)

        # Esperar a que al menos una interacción ocurra para asegurarse de que los listeners estén activos
        while self.connect:
            if self.timer_inactive == 0:
                break
            await asyncio.sleep(0.1)

        await asyncio.gather(
            self.time_without_activity(), 
            self.timer_of_activity()
        )
