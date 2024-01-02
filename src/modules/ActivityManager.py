import time
import threading
from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener

pause_event = threading.Event()
new_connection = threading.Event()
inactive_event = threading.Event()

class ActivityManager:
    def __init__(self):
        self.start_listeners()
        self.timer_user = 0
        self.timer_inactive = 0
        self.is_paused = False
        self.is_connected = True
        self.inactivity_threshold = 1800
        self.pause_time = 60
        self.pause_timer = None

    def pause_program(self):
        """Pause the program for 60 seconds"""
        try:
            self.is_paused = True
            self.is_connected = False
            pause_event.set()
            time.sleep(self.pause_time)
            self.is_paused = False
        except Exception as e:
            print(f"Error during pause_program: {e}")

    def timer_of_activity(self):
        """Timer for count the consecutive seconds of user activity"""
        try:
            while self.is_connected:
                time.sleep(1)
                self.timer_user += 1
                print("time 1:", self.timer_user)
                if self.timer_user >= self.inactivity_threshold:
                    self.pause_timer = threading.Thread(target=self.pause_program)
                    self.pause_timer.start()
        except Exception as e:
            print(f"Error during timer_of_activity: {e}")

    def time_without_activity(self, interactive):
        """Timer for count the consecutive seconds between user interactions whit mouse or keyboard"""
        try:
            while self.is_connected:
                time.sleep(1)
                self.timer_inactive += 1
                print("time 2:", self.timer_inactive)
                if interactive and self.timer_inactive >= 300:
                    self.is_connected = False
                    inactive_event.set()
                    pause_event.set()
                elif not interactive and self.timer_inactive >= 900:
                    self.is_connected = False
                    inactive_event.set()
                    pause_event.set()
        except Exception as e:
            print(f"Error during time_without_activity: {e}")

    def have_interaction(self, *args):
        """Reset the timers when user have interaction"""
        try:
            self.timer_inactive = 0
            if not self.is_paused and not self.is_connected:
                new_connection.set()
                self.is_connected = True
        except Exception as e:
            print(f"Error during have_interaction: {e}")

    def start_listeners(self):
        """Start the listeners for mouse and keyboard"""
        try:
            mouse_listener = MouseListener(
                on_move=self.have_interaction,
                on_click=self.have_interaction,
                on_scroll=self.have_interaction
            )
            keyboard_listener = KeyboardListener(on_press=self.have_interaction)
            mouse_listener.start()
            keyboard_listener.start()
        except Exception as e:
            print(f"Error during start_listeners: {e}")

    def start(self, time_to_pause, time_of_pause, interactive):
        """Start the timers"""
        self.stop_threads_and_reset()
        try:
            self.inactivity_threshold = time_to_pause
            self.pause_time = time_of_pause
            thread1 = threading.Thread(target=self.timer_of_activity)
            thread2 = threading.Thread(target=self.time_without_activity, args=(interactive,))
            thread1.start()
            thread2.start()
        except Exception as e:
            print(f"Error during start: {e}")

    def stop_threads_and_reset(self):
        """Stop the timers and reset the variables"""
        try:
            self.timer_user = 0
            self.timer_inactive = 0
            self.is_paused = False
            new_connection.clear()
            pause_event.clear()
            inactive_event.clear()
        except Exception as e:
            print(f"Error during stop_threads_and_reset: {e}")
