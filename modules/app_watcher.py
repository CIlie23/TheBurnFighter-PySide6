import pygetwindow as gw
from PySide6.QtCore import QTimer

class AppWatcher:
    def __init__(self, targets, on_detected, interval=10):
        """
        targets = list of strings to watch for in window titles
        on_detected = function to call when detected for long enough
        interval = seconds before triggering
        """

        self.targets = targets
        self.on_detected = on_detected
        self.threshold = interval
        self.open_time = 0
        self.triggered = False

        self.timer = QTimer()
        self.timer.timeout.connect(self.check)
        self.timer.start(1000)

    def check(self):
        try:
            windows = gw.getAllTitles()
            detected = any(
                target.lower() in title.lower()
                for title in windows
                for target in self.targets
            )

            if detected:
                self.open_time += 1
                print(f"Target detected... {self.open_time}'s")

                if self.open_time >= self.threshold and not self.triggered:
                    self.triggered = True
                    self.on_detected()
            
            else:
                self.open_time = 0
                self.triggered = False

        except Exception as e:
            print(f"Watcher error: {e}")