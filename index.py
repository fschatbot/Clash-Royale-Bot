from PIL import ImageGrab
import time
import win32gui
import win32con
import pyautogui

screen_width, screen_height = pyautogui.size()
game_width = 1262 - 656
bbox = (screen_width / 2 - game_width / 2, 0, screen_width / 2 + game_width / 2, screen_height)  # Full screen

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
    bring_focus()
    screenshot= ImageGrab.grab(bbox=bbox)
    return screenshot


def is_end_screen():
    ...

def count_crown():
    ...


def main():
    ...

if __name__ == "__main__":
    ss = screenshot()
    ss.show()