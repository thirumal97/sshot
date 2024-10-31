import os
import time
from datetime import datetime
import pyautogui
from colorama import Fore, Back, Style, init

# Initialize colorama
init()

def get_region_dimensions():
    x1, y1, x2, y2 = None, None, None, None

    while True:
        x, y = pyautogui.position()

        # Capture top-left corner coordinates
        if x1 is None and y1 is None:
            print(Fore.BLACK + "top-left corner " + Style.RESET_ALL)
            time.sleep(2)  # Wait for 2 seconds to capture
            if pyautogui.position() == (x, y):
                x1, y1 = x, y
                print(Back.GREEN + f"Top-left corner captured: ({x1}, {y1})" + Style.RESET_ALL)

        # Capture bottom-right corner coordinates
        elif x2 is None and y2 is None:
            print(Fore.BLACK + "bottom-right corner " + Style.RESET_ALL)
            time.sleep(2)  # Wait for 2 seconds to capture
            if pyautogui.position() == (x, y):
                x2, y2 = x, y
                print(Back.RED + f"Bottom-right corner captured: ({x2}, {y2})" + Style.RESET_ALL)
                break  # Exit loop once both corners are captured

        time.sleep(0.5)  # Check mouse position every half second

    # Calculate width and height
    width = x2 - x1
    height = y2 - y1
    print(f"Width: {width}, Height: {height}")

    return x1, y1, width, height

def capture_screenshot(region):
    time.sleep(2)
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop/screenshot")
    ensure_directory_exists(desktop_path)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"screenshot_{timestamp}.png"
    file_path = os.path.join(desktop_path, file_name)
    screenshot = pyautogui.screenshot(region=region)
    screenshot.save(file_path)
    print(Fore.CYAN + f"Screenshot saved to {file_path}" + Style.RESET_ALL)

def ensure_directory_exists(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(Fore.BLUE + f"Directory created: {path}" + Style.RESET_ALL)
    else:
        print(Fore.BLUE + "Directory already exists." + Style.RESET_ALL)

def main_process():
    # Ensure screenshot directory exists
    screenshot_directory = os.path.expanduser('~/Desktop/screenshot')
    ensure_directory_exists(screenshot_directory)

    # Get region dimensions for screenshot
    x1, y1, w, h = get_region_dimensions()
    region_to_capture = (x1, y1, w, h)
    print(f"Region to capture: {region_to_capture}")

    # Capture initial screenshot
    capture_screenshot(region_to_capture)

if __name__ == "__main__":
    main_process()
