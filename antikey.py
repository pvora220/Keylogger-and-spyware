import os
import psutil
import time
import tkinter as tk
from tkinter import messagebox
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import threading

# CONFIG
SUSPICIOUS_MODULES = ['pynput', 'keyboard', 'pyxhook']
SUSPICIOUS_KEYWORDS = ['keylogger', 'key_log', 'keystroke', 'hook', 'capture']
WATCH_PATH = os.path.expanduser("~")  # Monitor user's home directory
LOG_FILE = "anti_keylogger_log.txt"

# Logging
logging.basicConfig(filename=LOG_FILE, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# GUI alert
def show_alert(title, msg):
    root = tk.Tk()
    root.withdraw()
    messagebox.showwarning(title, msg)

# Process scanning
def check_running_processes():
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            name = proc.info['name'] or ''
            cmdline = ' '.join(proc.info['cmdline']) if proc.info['cmdline'] else ''
            if any(kw in name.lower() or kw in cmdline.lower() for kw in SUSPICIOUS_KEYWORDS + SUSPICIOUS_MODULES):
                alert = f"Suspicious process detected: {name} ({proc.pid})"
                logging.warning(alert)
                show_alert("Anti-Keylogger Alert", alert)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

# File scanning
def scan_files():
    for root, _, files in os.walk(WATCH_PATH):
        for file in files:
            if file.endswith(('.py', '.exe', '.dll')):
                full_path = os.path.join(root, file)
                try:
                    with open(full_path, 'r', errors='ignore') as f:
                        content = f.read()
                        if any(mod in content for mod in SUSPICIOUS_MODULES):
                            alert = f"Suspicious script found: {full_path}"
                            logging.warning(alert)
                            show_alert("Anti-Keylogger Alert", alert)
                except Exception:
                    continue

# Realtime file monitoring
class SuspiciousFileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        filepath = event.src_path
        if filepath.endswith(('.py', '.exe', '.dll')):
            try:
                with open(filepath, 'r', errors='ignore') as f:
                    content = f.read()
                    if any(mod in content for mod in SUSPICIOUS_MODULES):
                        alert = f"New suspicious file created: {filepath}"
                        logging.warning(alert)
                        show_alert("Anti-Keylogger Alert", alert)
            except Exception:
                pass

def start_file_monitoring():
    observer = Observer()
    event_handler = SuspiciousFileHandler()
    observer.schedule(event_handler, WATCH_PATH, recursive=True)
    observer.start()
    return observer

# Main loop
def monitor_loop():
    while True:
        check_running_processes()
        scan_files()
        time.sleep(60)

if __name__ == "__main__":
    print("🔍 Advanced Anti-Keylogger started.")
    observer = start_file_monitoring()
    try:
        monitor_thread = threading.Thread(target=monitor_loop)
        monitor_thread.daemon = True
        monitor_thread.start()
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
