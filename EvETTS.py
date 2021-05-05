import pyttsx3
from pyttsx3.drivers import sapi5
import os
import time
import pandas as pd

log_dir = os.path.expanduser("~/Documents/Eve/logs/Chatlogs")

names = ["JJ Masterson", "Meg theonlyone"]

def newest(path):
    files = os.listdir(path)
    paths = [os.path.join(path, basename) for basename in files if basename.startswith("Corp")]
    return max(paths, key=os.path.getmtime)

engine = pyttsx3.init()
engine.setProperty("rate", 125)

last_message = ""

while(1):
    # print(newest(log_dir))
    with open(newest(log_dir), "r", encoding="utf-16", errors="ignore") as f:
        lines = f.readlines()

        lines = pd.Series(lines)
        lines = lines[lines.str.contains("|".join(names))]
        lines = lines.str.strip("\n")
        lines = lines.str.split(r"(Meg theonlyone >|JJ Mastersen >)", expand=True)

        newest_message = ""

        if not lines.empty:
            newest_message = lines[2].values[-1]        
        

        if newest_message != last_message:
            print(newest_message)
            last_message = newest_message
            engine.say(newest_message)
            engine.runAndWait()

    time.sleep(1)




