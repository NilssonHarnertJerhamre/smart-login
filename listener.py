from pynput import keyboard
from time import time
from type import *
from event import *
from msvcrt import getch

class Listener:

    start_time = 0

    input = []

    def __init__(self):
        pass

    def on_press(self, key):
        try:
            if len(self.input) == 0:
                self.start_time = time()

            e = Event()
            e.type = Type.key_pressed
            e.time = time() - self.start_time
            e.char = key.char
            self.input.append(e)

        except AttributeError:
            if key == keyboard.Key.enter:
                e = Event()
                e.type = Type.key_pressed
                e.time = time() - self.start_time
                e.char = key
                self.input.append(e)

    def on_release(self, key):

        try:
            if key == keyboard.Key.esc or key == keyboard.Key.enter and len(self.input) != 0:
                return False

            e = Event()
            e.type = Type.key_released
            e.time = time() - self.start_time
            e.char = key.char
            self.input.append(e)

        except AttributeError:
            pass

    def listen(self, phrase):
        self.input = []
        with keyboard.Listener(
                on_press=self.on_press,
                on_release=self.on_release) as listener:
            raw_input('type \''+phrase+'\': ')
            listener.join()
            listener.wait()
        return self.input   
            