import json
import os
import sys

from EvETTS import TTS
from PyQt5.QtCore import Qt
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


class EvETTSGUI(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.config = {"names": [], "volume": 99}
        self.TTS = None

        if os.path.exists("./.config.json"):
            self.loadConfig()

        self.setup_main_window()
        self.set_window_layout()
        self.setUpBars()

        self.show()

    def loadConfig(self):
        with open("./.config.json", "r") as f:
            self.config = json.load(f)

    def saveConfig(self):
        self.config["names"] = self.nameField.text().split(",")
        with open("./.config.json", "w") as f:
            json.dump(self.config, f, sort_keys=True, indent=4, ensure_ascii=False)

    def setup_main_window(self):
        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)
        self.resize(800, 400)
        self.setWindowTitle("EvE TTS")
        self.setWindowIcon(QIcon("./data/tts_icon.png"))

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
        self.volumeDisplay.display(value)
        self.config["volume"] = value

    def set_window_layout(self):
        self.startTTSButton = QPushButton("Start TTS")
        self.startTTSButton.clicked.connect(self.startTTS)
        self.stopTTSButton = QPushButton("Stop TTS")
        self.stopTTSButton.clicked.connect(self.stopTTS)
        self.saveNames = QPushButton("Save")
        self.saveNames.clicked.connect(self.saveConfig)

        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalSettingBox = QGroupBox("Buttons")
        self.horizontalLayout.addWidget(self.horizontalSettingBox)
        self.left_vertical_layout = QVBoxLayout()

        self.horizontalSettingBox.setLayout(self.left_vertical_layout)

        self.left_vertical_layout.addWidget(self.startTTSButton)
        self.left_vertical_layout.addWidget(self.stopTTSButton)
        self.left_vertical_layout.addStretch(1)
        self.left_vertical_layout.addWidget(self.saveNames)

        self.right_grid_layout = QGridLayout()
        self.right_grid_layout.setSpacing(10)
        self.horizontalGroupBox = QGroupBox("Chathistory")
        self.horizontalLayout.addWidget(self.horizontalGroupBox)

        self.horizontalGroupBox.setLayout(self.right_grid_layout)

        self.textField = QTextEdit()
        self.textField.setReadOnly(True)

        self.nameFieldText = QLabel("Name(s) seperated by comma ','")
        self.nameField = QLineEdit()
        self.nameField.setText(",".join(self.config["names"]))

        self.volumeLabel = QLabel("Volume")
        self.volumeSlider = QSlider(Qt.Horizontal, self)
        self.volumeSlider.setValue(self.config["volume"])

        self.volumeDisplay = QLCDNumber(self)
        self.volumeDisplay.display(self.config["volume"])
        self.volumeDisplay.setSegmentStyle(QLCDNumber.Flat)

        display_palette = self.volumeDisplay.palette()
        display_palette.setColor(display_palette.WindowText, QColor(0, 0, 0))

        self.volumeDisplay.setPalette(display_palette)

        self.volumeSlider.valueChanged.connect(lambda x: self.volumeSliderMoved(x))

        # Chat history
        self.right_grid_layout.addWidget(self.textField, 1, 0, 4, 2)

        # Volume regulation
        self.right_grid_layout.addWidget(self.volumeLabel, 5, 0)
        self.right_grid_layout.addWidget(self.volumeSlider, 6, 0)
        self.right_grid_layout.addWidget(self.volumeDisplay, 6, 1)

        # Name fields
        self.right_grid_layout.addWidget(self.nameFieldText)
        self.right_grid_layout.addWidget(self.nameField)

    def toggleStatus(self, state):
        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()

    def startTTS(self):
        self.TTS = TTS(self.config["names"], self.config["volume"])
        self.TTS.enabled = True
        self.TTS.run()

    def stopTTS(self):
        if self.TTS is not None:
            self.TTS.enabled = False


def main():
    app = QApplication(sys.argv)
    EvETTSGUI()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
