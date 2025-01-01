import time
import threading
from PIL import ImageGrab
import requests
from io import BytesIO
from pystray import Icon, Menu, MenuItem
from PIL import Image
import win32gui # type: ignore
from plyer import notification # type: ignore
import json
import os

INTERVAL = None
API_URL = None

def get_open_windows():
    focusedwindow = win32gui.GetWindowText(win32gui.GetForegroundWindow())
    openwindows = []
    def getopwin(hwnd, extra):
        if win32gui.IsWindowVisible(hwnd):
            if not win32gui.GetWindowText(hwnd) == '':
                openwindows.append(win32gui.GetWindowText(hwnd))
    win32gui.EnumWindows(getopwin, None)
    thelist = {
        'focused': focusedwindow,
        'open': openwindows
    }
    return thelist

def capture_and_send(api_url):
    while running[0]:
        open_windows = get_open_windows()

        screenshot = ImageGrab.grab()
        buffered = BytesIO()
        screenshot.save(buffered, format="PNG")
        buffered.seek(0)

        try:
            print({"windows": open_windows})
            response = requests.post(api_url, files={"file": ("screenshot.png", buffered, "image/png")}, data={"json": json.dumps({"windows": open_windows})}, timeout=10)
            print(f"Response: {response.status_code}, {response.text}")
        except Exception as e:
            print(f"Error sending capture: {e}")
            notification.notify(
                title="Orbi Capture Error",
                message=f"Error sending capture, check console for more details.",
                app_name="Orbi Client",
                timeout=10
            )
        
        time.sleep(INTERVAL)

def exit_program(icon):
    running[0] = False
    icon.stop()

def setup_tray_icon():
    menu = Menu(
        MenuItem("Status: Running", lambda: None, enabled=False),
        MenuItem("Exit", lambda icon: exit_program(icon))
    )
    icon_image = Image.open("orbi.png")
    icon = Icon("Orbi Client", icon_image, "Orbi Client", menu)
    icon.run()

def load_config():
    if not os.path.exists("config.json"):
        print("Config file not found, exiting.")
        exit(1)
    with open("config.json", "r") as f:
        config = json.load(f)
        global INTERVAL
        global API_URL
        INTERVAL = config["interval"]
        API_URL = config["api_url"]

load_config()

running = [True]

screenshot_thread = threading.Thread(target=capture_and_send, args=(API_URL,))
screenshot_thread.daemon = True
screenshot_thread.start()

setup_tray_icon()
