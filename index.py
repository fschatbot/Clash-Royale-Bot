from PIL import ImageGrab, Image, ImageChops
import time
import win32gui
import win32con
import pyautogui
import numpy as np 
import os

screen_width, screen_height = pyautogui.size()
game_width = 1262 - 656
bbox = (screen_width / 2 - game_width / 2, 0, screen_width / 2 + game_width / 2, screen_height)  # Full screen

current_i = len(os.listdir('database'))

def bring_focus():
    window_title = "BlueStacks App Player"
    hwnd = win32gui.FindWindow(None, window_title)
    if hwnd == 0: raise Exception("Window not found: " + window_title)

    win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
    win32gui.SetForegroundWindow(hwnd)

    while True:
        if win32gui.GetForegroundWindow() == hwnd: break
        time.sleep(0.1)

    return hwnd

def screenshot():
    global current_i

    bring_focus()
    screenshot = ImageGrab.grab(bbox=bbox)
    # screenshot = screenshot.convert('L')
    # Save this in the database folder
    screenshot.save(f'database/test{current_i}.png')
    current_i += 1

def page(ss: Image.Image):
    # Find if start.png is present in ss at (230, 810)
    start_menu = Image.open('assets/start.png').convert('L')
    region = ss.crop((230, 810, 230 + start_menu.width, 810 + start_menu.height))
    difference = ImageChops.difference(region, start_menu)
    if np.max(np.array(difference)) == 5:
        return 'START_PAGE'
    
    

    return np.max(np.array(difference))
    

    raise Exception("Unknown page")



def is_end_screen():
    ...

def count_crown():
    ...


def main():
    ...

if __name__ == "__main__":
    while True:
        time.sleep(1)
        ss = screenshot()
        # ss.save("screenshot.png")
    # ss.show()
    # print(page(ss))