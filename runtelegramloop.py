from TelegramBridge import TelegramBridge
import time

class RunTelegramLoop:
    def __init__(self):
        self.bridge = TelegramBridge()

    def start_forever(self):
        print("[RUN] Launching persistent Telegram loop...")
        self.bridge.start()
        while True:
            time.sleep(60)