import os
import time

import pandas as pd
import pyttsx3
from PyQt5.QtWidgets import *
from pyttsx3.drivers import sapi5


class TTS:
    def __init__(self, names, volume=99):
        self.names = names
        self.log_dir = os.path.expanduser("~/Documents/Eve/logs/Chatlogs")

        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", 135)

        self.newest_message = ""
        self.last_message = ""

        self.enabled = False

    def change_volume(self, value):
        pass

    def newest(self, path):
        files = os.listdir(path)
        paths = [
            os.path.join(path, basename)
            for basename in files
            if basename.startswith("Corp") or basename.startswith("FluPZel")
        ]
        return max(paths, key=os.path.getmtime)

    def run(self):
        while self.enabled:
            # print(newest(log_dir))
            with open(
                self.newest(self.log_dir), "r", encoding="utf-16", errors="ignore"
            ) as f:
                lines = f.readlines()

                lines = pd.Series(lines)
                lines = lines[lines.str.contains("|".join(self.names))]
                lines = lines.str.strip("\n")

                splitString = r""
                for name in self.names:
                    splitString += name + r" >|"
                splitString = splitString[:-1]
                lines = lines.str.split(splitString, expand=True)

                if not lines.empty:
                    self.newest_message = lines[1].values[-1]

                if self.newest_message != self.last_message:
                    print(self.newest_message)
                    self.last_message = self.newest_message
                    self.engine.say(self.newest_message)
                    self.engine.runAndWait()

            time.sleep(0.5)
