import time
import threading
import tkinter as tk
from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Listener, KeyCode, Controller as KeyboardController

start_end = KeyCode(char="k")
exit_key = KeyCode(char="z")


class AutoClickerClass(threading.Thread):
    def __init__(self):
        super(AutoClickerClass, self).__init__()
        self.delay = 1.5
        self.button = Button.left
        self.key = KeyCode(char='w')
        self.running = False
        self.program_run = True

    def begin_clicking(self):
        self.running = True

    def clicking_stop(self):
        self.running = False

    def exit(self):
        self.clicking_stop()
        self.program_run = False

    def run(self):
        while self.program_run:
            while self.running:
                mouse_ob.press(self.button)
                keyboard_ob.press(self.key)

                time.sleep(self.delay)
                mouse_ob.release(self.button)
                keyboard_ob.release(self.key)
            time.sleep(0.1)


window = tk.Tk()
window.geometry("400x100+500+80")
window.title('Clicker')
lbl = tk.Label(window, text="This window will close in 5 seconds! \n Press k to start \n Press k again to pause \n "
                            "And press z to exit", font='Terminal 12')
lbl.pack()
window.attributes('-topmost', True)
window.after(5000, lambda: window.destroy())
window.overrideredirect(True)
window.mainloop()
mouse_ob, keyboard_ob = MouseController(), KeyboardController()
t = AutoClickerClass()
t.start()


def fun(k):
    if k == start_end:
        if t.running:
            window = tk.Tk()
            window.geometry("400x100+500+80")
            window.title('Clicker')
            lbl = tk.Label(window, text="Pause", font='Terminal 12')
            lbl.pack()
            window.attributes('-topmost', True)
            window.after(5000, lambda: window.destroy())
            window.overrideredirect(True)
            window.mainloop()
            t.clicking_stop()
        else:
            window = tk.Tk()
            window.geometry("400x100+500+80")
            window.title('Clicker')
            lbl = tk.Label(window, text="Starting", font='Terminal 12')
            lbl.pack()
            window.attributes('-topmost', True)
            window.after(5000, lambda: window.destroy())
            window.overrideredirect(True)
            window.mainloop()
            t.begin_clicking()

    elif k == exit_key:
        window = tk.Tk()
        window.geometry("400x100+500+80")
        window.title('Clicker')
        lbl = tk.Label(window, text="Exiting", font='Terminal 12')
        lbl.pack()
        window.attributes('-topmost', True)
        window.after(2000, lambda: window.destroy())
        window.overrideredirect(True)
        window.mainloop()
        t.exit()
        listener.stop()


with Listener(on_press=fun) as listener:
    listener.join()
