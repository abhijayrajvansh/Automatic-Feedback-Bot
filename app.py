#/
#    author:   abhijayrajvansh
#    created:  27.12.2022 11:23:38
#    updated:  4.01.2024 06:41:23
#/

from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

def pressTab():
    keyboard.press(Key.tab)
    time.sleep(0.1)
    keyboard.release(Key.tab)
    time.sleep(0.1)

def pressDown():
    keyboard.press(Key.down)
    time.sleep(0.1)
    keyboard.release(Key.down)
    time.sleep(0.1)

def fill_feedback():
    pressDown()
    time.sleep(2)
    pressDown()
    pressDown()
    pressDown()
    pressDown()
    pressDown()
    pressDown()
    pressDown()
    pressDown()
    pressTab()

print("Get ready, and point your cursor at the first index position...")
time.sleep(3)

while(True):
    fill_feedback()