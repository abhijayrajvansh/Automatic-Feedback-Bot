#/
#    author:   abhijayrajvansh
#    created:  27.12.2022 11:23:38
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

def writeComment():
    keyboard.type('It was a very good experience.')

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
    pressDown()
    writeComment()
    pressTab()

print("Get ready, and point your cursor at the first index position...")
time.sleep(3)

while(True):
    fill_feedback()