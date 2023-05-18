import pyautogui
import time

while True:
    # Move the mouse in a square pattern
    pyautogui.move(100, 0, duration=0.25)   # move right
    pyautogui.move(0, 100, duration=0.25)   # move down
    pyautogui.move(-100, 0, duration=0.25)  # move left
    pyautogui.move(0, -100, duration=0.25)  # move up

    pyautogui.click()  # Simulate left mouse click

    time.sleep(60)  # Wait for 60 seconds
