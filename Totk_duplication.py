import pyautogui
import threading
import ctypes
from pynput.keyboard import Listener, KeyCode

activation = KeyCode(char="-")
running = False

directions = ["", "", "s", "a", "w", "d", ""]

print(
    "To start duplicating be sure to be playing with your keyboard then you need to to get, drop and pick back the item you are interest in duplicating\nthen click - to start the program or to stop it\nthis program wont change your shiled if it broke so just be careful on that"
)


def press_button(button):
    pyautogui.keyDown(button)
    pyautogui.keyUp(button)


def Glitch():
    while True:
        if running:
            i = 0
            j = 0

            press_button("v")

            pyautogui.keyDown("r")
            pyautogui.keyDown("c")
            pyautogui.keyUp("r")
            pyautogui.keyUp("c")

            press_button("m")
            press_button("v")

            while i < 5:
                pyautogui.keyDown("c")
                pyautogui.keyUp("c")
                i += 1

            ctypes.windll.user32.keybd_event(0x5A, 0, 0, 0)
            ctypes.windll.user32.keybd_event(0x58, 0, 0, 0)

            while j < 7:
                press_button("c")
                pyautogui.keyDown(directions[j])
                pyautogui.sleep(0.1)
                pyautogui.keyUp(directions[j])
                press_button("c")
                j += 1

            pyautogui.keyUp("x")
            pyautogui.keyUp("z")


def toggle_event(key):
    if key == activation:
        global running
        running = not running


click_thread = threading.Thread(target=Glitch)
click_thread.start()

with Listener(on_press=toggle_event) as listener:
    listener.join()
