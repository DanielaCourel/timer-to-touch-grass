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

    def pause_program(self):
        self.pause = True
        self.connect = False
        pause_event.set()
        time.sleep(60)
        self.pause = False
        self.pause_timer = None
        pause_event.clear()

    async def timer_of_activity(self):
        while self.connect:
            time.sleep(1)
            self.timer_user += 1
            if self.timer_user >= self.PAUSE_TIME:
                self.pause_timer = threading.Thread(target=self.pause_program)
                self.pause_timer.start()

    async def time_without_activity(self):
        while self.connect:
            time.sleep(1)
            self.timer_inactive += 1
            if self.timer_inactive >= 300:
                self.connect = False
                self.timer_inactive = 0
                self.timer_user = 0

    def have_interaction(self, *args):
        self.timer_inactive = 0
        if not self.connect and self.pause_timer is None:
            self.connect = True

    async def start(self):
        await asyncio.gather(
            self.timer_of_activity(),
            self.time_without_activity()
        )

