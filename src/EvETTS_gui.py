import os
import sys
import time

from PyQt5.QtCore import Qt, QThread
from PyQt5.QtGui import QColor, QIcon
from PyQt5.QtWidgets import (
    QAction,
    QApplication,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QSlider,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)

from src.EvETTS import TTS
from src.utils import TTS_variables as tts


class EvETTSGUI(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.TTS = None

        if os.path.exists("./.config.json"):
            tts.loadConfig()

        self.setup_main_window()
        self.set_window_layout()
        self.setUpBars()

        self.show()

    def setup_main_window(self):
        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)
        self.resize(800, 400)
        self.setWindowTitle("EvE TTS")
        self.setWindowIcon(QIcon("./src/data/tts_icon.png"))

    def setUpBars(self):
        # Menubar
        menubar = self.menuBar()
        settingMenu = menubar.addMenu("Settings")

        settingStatusBar = QAction("View StatusBar", self, checkable=True)
        settingStatusBar.setStatusTip("View StatusBar")
        settingStatusBar.setChecked(True)
        settingStatusBar.triggered.connect(self.toggleStatus)

        settingMenu.addAction(settingStatusBar)

        # StatusBar
        self.statusbar = self.statusBar()
        self.statusbar.showMessage("Ready")

    def volumeSliderMoved(self, value):
        self.volumeDisplay.setText("Volume: {}".format(value))
        tts.settings["tts_volume"] = value

    def setUpButtons(self):
        self.startTTSButton = QPushButton("Start TTS")
        self.startTTSButton.clicked.connect(self.startTTS)

        self.stopTTSButton = QPushButton("Stop TTS")
        self.stopTTSButton.clicked.connect(self.stopTTS)

        self.clearChatHistoryButton = QPushButton("Clear History")
        self.clearChatHistoryButton.clicked.connect(self.clearChatHistory)

        self.saveNames = QPushButton("Save")

    def setUpLayout(self):
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalSettingBox = QGroupBox("Buttons")
        self.left_vertical_layout = QVBoxLayout()

        self.horizontalSettingBox.setLayout(self.left_vertical_layout)

        self.right_grid_layout = QGridLayout()
        self.right_grid_layout.setSpacing(10)
        self.horizontalGroupBox = QGroupBox("Chathistory")

        self.horizontalGroupBox.setLayout(self.right_grid_layout)

    def setUpTextFields(self):
        self.textField = QTextEdit()
        self.textField.setReadOnly(True)

        self.nameFieldText = QLabel("Nickname(s) seperated by comma ','")
        self.nameField = QLineEdit()
        self.nameField.setText(",".join(tts.settings["characterNames"]))

        self.channelNamesFieldText = QLabel("Channelname(s) seperated by comma ','")
        self.channelNamesField = QLineEdit()
        self.channelNamesField.setText(",".join(tts.settings["channelNames"]))

    def setUpVolumeDisplay(self):
        self.volumeSlider = QSlider(Qt.Horizontal, self)
        self.volumeSlider.setValue(tts.settings["tts_volume"])

        self.volumeDisplay = QLabel(
            "Volume: {}".format(tts.settings["tts_volume"]), self
        )
        self.volumeDisplay.setMinimumWidth(80)

        self.volumeSlider.valueChanged.connect(lambda x: self.volumeSliderMoved(x))

    def addWidegetsInLayout(self):
        # left and right box
        self.horizontalLayout.addWidget(self.horizontalSettingBox)
        self.horizontalLayout.addWidget(self.horizontalGroupBox)

        # buttons on the left
        self.left_vertical_layout.addWidget(self.startTTSButton)
        self.left_vertical_layout.addWidget(self.stopTTSButton)
        self.left_vertical_layout.addStretch(1)
        self.left_vertical_layout.addWidget(self.clearChatHistoryButton)
        self.left_vertical_layout.addWidget(self.saveNames)

        # Chat history
        self.right_grid_layout.addWidget(self.textField, 1, 0, 3, 2)

        self.right_grid_layout.addWidget(self.channelNamesFieldText, 5, 0)
        self.right_grid_layout.addWidget(self.channelNamesField, 5, 1)

        # Volume regulation
        self.right_grid_layout.addWidget(self.volumeSlider, 6, 0)
        self.right_grid_layout.addWidget(self.volumeDisplay, 6, 1)

        # Name fields
        self.right_grid_layout.addWidget(self.nameFieldText)
        self.right_grid_layout.addWidget(self.nameField)

    def set_window_layout(self):
        self.setUpButtons()
        self.setUpTextFields()
        self.setUpVolumeDisplay()
        self.setUpLayout()
        self.addWidegetsInLayout()

        self.saveNames.clicked.connect(self.saveConfig)

    def toggleStatus(self, state):
        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()

    def startTTS(self):
        if tts.settings["tts_enabled"]:
            return

        self.updateChatHistory()

        self.thread = QThread()
        tts.settings["tts_enabled"] = True

        self.TTS = TTS()
        self.TTS.characterNames = tts.settings["characterNames"]
        self.TTS.channelNames = tts.settings["channelNames"]
        self.TTS.moveToThread(self.thread)

        self.thread.started.connect(self.TTS.run)

        self.TTS.new_message.connect(self.updateChatHistory)

        self.TTS.finished.connect(self.thread.quit)
        self.TTS.finished.connect(self.TTS.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)

        self.statusbar.showMessage("TTS running")
        self.thread.start()
        self.thread.exec()

    def updateChatHistory(self):
        self.textField.setText("\n".join(tts.chatHistory))

    def stopTTS(self):
        tts.settings["tts_enabled"] = False
        self.statusbar.showMessage("TTS stopped")

    def clearChatHistory(self):
        tts.chatHistory = ["Booting up TTS..."]
        self.stopTTS()
        self.updateChatHistory()
        self.statusbar.showMessage("Chat history cleared")

    def saveConfig(self):
        self.stopTTS()
        tts.settings["channelNames"] = self.channelNamesField.text().split(",")
        tts.settings["characterNames"] = self.nameField.text().split(",")
        tts.saveConfig()
        self.statusbar.showMessage("Settings saved")

    def closeEvent(self, event):
        self.saveConfig()

        event.accept()


def main():
    app = QApplication(sys.argv)
    EvETTSGUI()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
