import logging
import os
import time

import pandas as pd
import pyttsx3
from PySide2 import QtCore, QtWidgets
from PySide2.QtCore import QObject, Signal
from PySide2.QtWidgets import *
from pyttsx3.drivers import sapi5

import src.TTS_variables as tts

logging.basicConfig(format="%(message)s", level=logging.INFO)


class TTS(QObject):
    finished = Signal()
    new_message = Signal()

    def __init__(self):
        super().__init__()
        self.characterNames = []
        self.channelNames = []

        self.newest_message = ""
        self.last_message = ""

        self.log_dir = os.path.expanduser("~/Documents/Eve/logs/Chatlogs")

        self.engine = pyttsx3.init()

    def newest(self, path):
        files = os.listdir(path)
        paths = [
            os.path.join(path, basename)
            for basename in files
            if any(
                basename.startswith(channelName)
                for channelName in tts.settings["channelNames"]
            )
        ]
        return max(paths, key=os.path.getmtime)

    def run(self):
        self.engine.setProperty("rate", tts.settings["tts_rate"])
        self.engine.setProperty("volume", tts.settings["tts_volume"] / 100)
        while tts.settings["tts_enabled"]:
            with open(
                self.newest(self.log_dir), "r", encoding="utf-16", errors="ignore"
            ) as f:
                lines = f.readlines()

                lines = pd.Series(lines)
                lines = lines[lines.str.contains("|".join(self.characterNames))]
                lines = lines.str.strip("\n")

                splitString = r""
                for name in tts.settings["characterNames"]:
                    splitString += name + r" >|"
                splitString = splitString[:-1]

                lines = lines.str.split(splitString, expand=True)

                if not lines.empty:
                    self.new_message.emit()
                    self.newest_message = lines[1].values[-1]

                if self.newest_message not in tts.chatHistory[-5:]:
                    tts.chatHistory.append(self.newest_message)
                    self.last_message = self.newest_message
                    self.engine.say(self.newest_message)
                    try:
                        self.engine.runAndWait()
                    except RuntimeError:
                        # print(re)
                        pass
            time.sleep(0.1)
        self.engine.stop()
        self.finished.emit()
