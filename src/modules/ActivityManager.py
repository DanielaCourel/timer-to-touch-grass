import time
import threading
from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener

pause_event = threading.Event()
new_connection = threading.Event()

class ActivityManager:
    def __init__(self):
        self.start_listeners()
        self.timer_user = 0
        self.timer_inactive = 0
        self.pause = False
        self.connect = True
        self.PAUSE_TIME = 6
        self.pause_timer = None

    def pause_program(self):
        self.timer_user = 0
        self.timer_inactive = 0
        self.pause = True
        self.connect = False
        pause_event.set()
        time.sleep(6)
        print("termina el tiempo de pausa")
        self.pause = False

    def timer_of_activity(self):
        while self.connect:
            time.sleep(1)
            self.timer_user += 1
            print("time 1:", self.timer_user)
            if self.timer_user >= self.PAUSE_TIME:
                self.pause_timer = threading.Thread(target=self.pause_program)
                self.pause_timer.start()

    def time_without_activity(self):
        while self.connect:
            time.sleep(1)
            self.timer_inactive += 1
            print("time 2:", self.timer_inactive)
            if self.timer_inactive >= 300:
                self.connect = False
                self.timer_inactive = 0
                self.timer_user = 0

    def have_interaction(self, *args):
        print("actividad")
        self.timer_inactive = 0
        if not self.pause and not self.connect:
            print("llega alguna vez acá?")
            new_connection.set()
            self.connect = True

    def start_listeners(self):
        mouse_listener = MouseListener(on_move=self.have_interaction, on_click=self.have_interaction, on_scroll=self.have_interaction)
        keyboard_listener = KeyboardListener(on_press=self.have_interaction)
        mouse_listener.start()
        keyboard_listener.start()

    def start(self):
        thread1 = threading.Thread(target=self.timer_of_activity)
        thread2 = threading.Thread(target=self.time_without_activity)
        thread1.start()
        thread2.start()

    def stop_threads_and_reset(self):
        self.timer_user = 0
        self.timer_inactive = 0
        self.pause = False
        self.pause_timer = None
        self.thread1 = None
        self.thread2 = None
        