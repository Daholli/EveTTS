import json

settings = {
    "characterNames": [],
    "channelNames": [],
    "tts_enabled": False,
    "tts_volume": 99,
    "tts_rate": 135,
}

chatHistory = ["Booting up TTS..."]


def loadConfig():
    with open("./.config.json", "r") as f:
        global settings
        settings = json.load(f)


def saveConfig():
    with open("./.config.json", "w") as f:
        json.dump(settings, f, sort_keys=True, indent=4, ensure_ascii=False)
