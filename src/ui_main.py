# -*- coding: utf-8 -*-
################################################################################
##
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide2
# V: 1.0.0
##
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
##
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
##
################################################################################

from PySide2.QtCore import (
    QCoreApplication,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    Qt,
    QThread,
    QUrl,
)
from PySide2.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QIcon,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
)
from PySide2.QtWidgets import *

import src.files_rc
import src.TTS_variables as tts
from src.EvETTS import TTS


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 720)
        MainWindow.setMinimumSize(QSize(1000, 720))

        self.addFonts()

        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(66, 73, 90, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(55, 61, 75, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(22, 24, 30, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(29, 32, 40, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        brush6 = QBrush(QColor(210, 210, 210, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush7 = QBrush(QColor(0, 0, 0, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush7)
        brush8 = QBrush(QColor(85, 170, 255, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Active, QPalette.Link, brush8)
        brush9 = QBrush(QColor(255, 0, 127, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush4)
        brush10 = QBrush(QColor(44, 49, 60, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
        brush11 = QBrush(QColor(210, 210, 210, 128))
        brush11.setStyle(Qt.NoBrush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
        # endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.Link, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
        brush12 = QBrush(QColor(210, 210, 210, 128))
        brush12.setStyle(Qt.NoBrush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
        # endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush7)
        brush13 = QBrush(QColor(51, 153, 255, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush13)
        palette.setBrush(QPalette.Disabled, QPalette.Link, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
        brush14 = QBrush(QColor(210, 210, 210, 128))
        brush14.setStyle(Qt.NoBrush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush14)
        # endif
        MainWindow.setPalette(palette)
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(
            u"QMainWindow {background: transparent; }\n"
            "QToolTip {\n"
            "	color: #ffffff;\n"
            "	background-color: rgba(27, 29, 35, 160);\n"
            "	border: 1px solid rgb(40, 40, 40);\n"
            "	border-radius: 2px;\n"
            "}"
        )
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(
            u"background: transparent;\n" "color: rgb(210, 210, 210);"
        )
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setStyleSheet(
            u"/* LINE EDIT */\n"
            "QLineEdit {\n"
            "	background-color: rgb(27, 29, 35);\n"
            "	border-radius: 5px;\n"
            "	border: 2px solid rgb(27, 29, 35);\n"
            "	padding-left: 10px;\n"
            "}\n"
            "QLineEdit:hover {\n"
            "	border: 2px solid rgb(64, 71, 88);\n"
            "}\n"
            "QLineEdit:focus {\n"
            "	border: 2px solid rgb(91, 101, 124);\n"
            "}\n"
            "\n"
            "/* SCROLL BARS */\n"
            "QScrollBar:horizontal {\n"
            "    border: none;\n"
            "    background: rgb(52, 59, 72);\n"
            "    height: 14px;\n"
            "    margin: 0px 21px 0 21px;\n"
            "	border-radius: 0px;\n"
            "}\n"
            "QScrollBar::handle:horizontal {\n"
            "    background: rgb(85, 170, 255);\n"
            "    min-width: 25px;\n"
            "	border-radius: 7px\n"
            "}\n"
            "QScrollBar::add-line:horizontal {\n"
            "    border: none;\n"
            "    background: rgb(55, 63, 77);\n"
            "    width: 20px;\n"
            "	border-top-right-radius: 7px;\n"
            "    border-bottom-right-radius: 7px;\n"
            "    subcontrol-position: right;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::sub-line:horizontal {\n"
            "    border: none;\n"
            "    background: rgb(55, 63, 77);\n"
            "    width: 20px;\n"
            ""
            "	border-top-left-radius: 7px;\n"
            "    border-bottom-left-radius: 7px;\n"
            "    subcontrol-position: left;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            " QScrollBar:vertical {\n"
            "	border: none;\n"
            "    background: rgb(52, 59, 72);\n"
            "    width: 14px;\n"
            "    margin: 21px 0 21px 0;\n"
            "	border-radius: 0px;\n"
            " }\n"
            " QScrollBar::handle:vertical {	\n"
            "	background: rgb(85, 170, 255);\n"
            "    min-height: 25px;\n"
            "	border-radius: 7px\n"
            " }\n"
            " QScrollBar::add-line:vertical {\n"
            "     border: none;\n"
            "    background: rgb(55, 63, 77);\n"
            "     height: 20px;\n"
            "	border-bottom-left-radius: 7px;\n"
            "    border-bottom-right-radius: 7px;\n"
            "     subcontrol-position: bottom;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::sub-line:vertical {\n"
            "	border: none;\n"
            "    background: rgb(55, 63"
            ", 77);\n"
            "     height: 20px;\n"
            "	border-top-left-radius: 7px;\n"
            "    border-top-right-radius: 7px;\n"
            "     subcontrol-position: top;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            "/* CHECKBOX */\n"
            "QCheckBox::indicator {\n"
            "    border: 3px solid rgb(52, 59, 72);\n"
            "	width: 15px;\n"
            "	height: 15px;\n"
            "	border-radius: 10px;\n"
            "    background: rgb(44, 49, 60);\n"
            "}\n"
            "QCheckBox::indicator:hover {\n"
            "    border: 3px solid rgb(58, 66, 81);\n"
            "}\n"
            "QCheckBox::indicator:checked {\n"
            "    background: 3px solid rgb(52, 59, 72);\n"
            "	border: 3px solid rgb(52, 59, 72);	\n"
            "	background-image: url(:/16x16/icons/16x16/cil-check-alt.png);\n"
            "}\n"
            "\n"
            "/* RADIO BUTTON */\n"
            "QRadioButton::indicator {\n"
            "    border: 3px solid rgb(52, 59, 72);\n"
            "	width: 15px;\n"
            "	height: 15px;\n"
            "	border-radius"
            ": 10px;\n"
            "    background: rgb(44, 49, 60);\n"
            "}\n"
            "QRadioButton::indicator:hover {\n"
            "    border: 3px solid rgb(58, 66, 81);\n"
            "}\n"
            "QRadioButton::indicator:checked {\n"
            "    background: 3px solid rgb(94, 106, 130);\n"
            "	border: 3px solid rgb(52, 59, 72);	\n"
            "}\n"
            "\n"
            "/* COMBOBOX */\n"
            "QComboBox{\n"
            "	background-color: rgb(27, 29, 35);\n"
            "	border-radius: 5px;\n"
            "	border: 2px solid rgb(27, 29, 35);\n"
            "	padding: 5px;\n"
            "	padding-left: 10px;\n"
            "}\n"
            "QComboBox:hover{\n"
            "	border: 2px solid rgb(64, 71, 88);\n"
            "}\n"
            "QComboBox::drop-down {\n"
            "	subcontrol-origin: padding;\n"
            "	subcontrol-position: top right;\n"
            "	width: 25px; \n"
            "	border-left-width: 3px;\n"
            "	border-left-color: rgba(39, 44, 54, 150);\n"
            "	border-left-style: solid;\n"
            "	border-top-right-radius: 3px;\n"
            "	border-bottom-right-radius: 3px;	\n"
            "	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
            "	background-position: center;\n"
            "	background-repeat: no-reperat;\n"
            " }\n"
            "QComboBox QAbstractItemView {\n"
            "	color: rgb("
            "85, 170, 255);	\n"
            "	background-color: rgb(27, 29, 35);\n"
            "	padding: 10px;\n"
            "	selection-background-color: rgb(39, 44, 54);\n"
            "}\n"
            "\n"
            "/* SLIDERS */\n"
            "QSlider::groove:horizontal {\n"
            "    border-radius: 9px;\n"
            "    height: 18px;\n"
            "	margin: 0px;\n"
            "	background-color: rgb(52, 59, 72);\n"
            "}\n"
            "QSlider::groove:horizontal:hover {\n"
            "	background-color: rgb(55, 62, 76);\n"
            "}\n"
            "QSlider::handle:horizontal {\n"
            "    background-color: rgb(85, 170, 255);\n"
            "    border: none;\n"
            "    height: 18px;\n"
            "    width: 18px;\n"
            "    margin: 0px;\n"
            "	border-radius: 9px;\n"
            "}\n"
            "QSlider::handle:horizontal:hover {\n"
            "    background-color: rgb(105, 180, 255);\n"
            "}\n"
            "QSlider::handle:horizontal:pressed {\n"
            "    background-color: rgb(65, 130, 195);\n"
            "}\n"
            "\n"
            "QSlider::groove:vertical {\n"
            "    border-radius: 9px;\n"
            "    width: 18px;\n"
            "    margin: 0px;\n"
            "	background-color: rgb(52, 59, 72);\n"
            "}\n"
            "QSlider::groove:vertical:hover {\n"
            "	background-color: rgb(55, 62, 76);\n"
            "}\n"
            "QSlider::handle:verti"
            "cal {\n"
            "    background-color: rgb(85, 170, 255);\n"
            "	border: none;\n"
            "    height: 18px;\n"
            "    width: 18px;\n"
            "    margin: 0px;\n"
            "	border-radius: 9px;\n"
            "}\n"
            "QSlider::handle:vertical:hover {\n"
            "    background-color: rgb(105, 180, 255);\n"
            "}\n"
            "QSlider::handle:vertical:pressed {\n"
            "    background-color: rgb(65, 130, 195);\n"
            "}\n"
            "\n"
            ""
        )
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Raised)

        self.verticalLayout = QVBoxLayout(self.frame_main)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.frame_top = QFrame(self.frame_main)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMinimumSize(QSize(0, 65))
        self.frame_top.setMaximumSize(QSize(16777215, 65))
        self.frame_top.setStyleSheet(u"background-color: transparent;")
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)

        self.frame_toggle = QFrame(self.frame_top)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 16777215))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_toggle.setFrameShape(QFrame.NoFrame)
        self.frame_toggle.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)

        self.btn_toggle_menu = QPushButton(self.frame_toggle)
        self.btn_toggle_menu.setObjectName(u"btn_toggle_menu")

        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_toggle_menu.sizePolicy().hasHeightForWidth()
        )
        self.btn_toggle_menu.setSizePolicy(sizePolicy)
        self.btn_toggle_menu.setStyleSheet(
            u"QPushButton {\n"
            "	background-image: url(:/24x24/icons/24x24/cil-menu.png);\n"
            "	background-position: center;\n"
            "	background-repeat: no-reperat;\n"
            "	border: none;\n"
            "	background-color: rgb(27, 29, 35);\n"
            "}\n"
            "QPushButton:hover {\n"
            "	background-color: rgb(33, 37, 43);\n"
            "}\n"
            "QPushButton:pressed {	\n"
            "	background-color: rgb(85, 170, 255);\n"
            "}"
        )

        self.verticalLayout_3.addWidget(self.btn_toggle_menu)

        self.horizontalLayout_3.addWidget(self.frame_toggle)

        self.frame_top_right = QFrame(self.frame_top)
        self.frame_top_right.setObjectName(u"frame_top_right")
        self.frame_top_right.setStyleSheet(u"background: transparent;")
        self.frame_top_right.setFrameShape(QFrame.NoFrame)
        self.frame_top_right.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2 = QVBoxLayout(self.frame_top_right)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.frame_top_btns = QFrame(self.frame_top_right)
        self.frame_top_btns.setObjectName(u"frame_top_btns")
        self.frame_top_btns.setMaximumSize(QSize(16777215, 42))
        self.frame_top_btns.setStyleSheet(u"background-color: rgba(27, 29, 35, 200)")
        self.frame_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_top_btns.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4 = QHBoxLayout(self.frame_top_btns)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)

        self.frame_label_top_btns = QFrame(self.frame_top_btns)
        self.frame_label_top_btns.setObjectName(u"frame_label_top_btns")

        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.frame_label_top_btns.sizePolicy().hasHeightForWidth()
        )

        self.frame_label_top_btns.setSizePolicy(sizePolicy1)
        self.frame_label_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_label_top_btns.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10 = QHBoxLayout(self.frame_label_top_btns)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(5, 0, 10, 0)

        self.frame_icon_top_bar = QFrame(self.frame_label_top_btns)
        self.frame_icon_top_bar.setObjectName(u"frame_icon_top_bar")
        self.frame_icon_top_bar.setMaximumSize(QSize(30, 30))
        self.frame_icon_top_bar.setStyleSheet(
            u"background: transparent;\n"
            "background-image: url(:/16x16/icons/16x16/cil-terminal.png);\n"
            "background-position: center;\n"
            "background-repeat: no-repeat;\n"
            ""
        )
        self.frame_icon_top_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_icon_top_bar.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.frame_icon_top_bar)

        self.label_title_bar_top = QLabel(self.frame_label_top_btns)
        self.label_title_bar_top.setObjectName(u"label_title_bar_top")
        self.label_title_bar_top.setFont(self.font1)
        self.label_title_bar_top.setStyleSheet(u"background: transparent;\n" "")

        self.horizontalLayout_10.addWidget(self.label_title_bar_top)

        self.horizontalLayout_4.addWidget(self.frame_label_top_btns)

        self.frame_btns_right = QFrame(self.frame_top_btns)
        self.frame_btns_right.setObjectName(u"frame_btns_right")
        sizePolicy1.setHeightForWidth(
            self.frame_btns_right.sizePolicy().hasHeightForWidth()
        )
        self.frame_btns_right.setSizePolicy(sizePolicy1)
        self.frame_btns_right.setMaximumSize(QSize(120, 16777215))
        self.frame_btns_right.setFrameShape(QFrame.NoFrame)
        self.frame_btns_right.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_btns_right)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_minimize = QPushButton(self.frame_btns_right)
        self.btn_minimize.setObjectName(u"btn_minimize")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(
            self.btn_minimize.sizePolicy().hasHeightForWidth()
        )
        self.btn_minimize.setSizePolicy(sizePolicy2)
        self.btn_minimize.setMinimumSize(QSize(40, 0))
        self.btn_minimize.setMaximumSize(QSize(40, 16777215))
        self.btn_minimize.setStyleSheet(
            u"QPushButton {	\n"
            "	border: none;\n"
            "	background-color: transparent;\n"
            "}\n"
            "QPushButton:hover {\n"
            "	background-color: rgb(52, 59, 72);\n"
            "}\n"
            "QPushButton:pressed {	\n"
            "	background-color: rgb(85, 170, 255);\n"
            "}"
        )
        icon = QIcon()
        icon.addFile(
            u":/16x16/icons/16x16/cil-window-minimize.png",
            QSize(),
            QIcon.Normal,
            QIcon.Off,
        )
        self.btn_minimize.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.btn_minimize)

        self.btn_maximize_restore = QPushButton(self.frame_btns_right)
        self.btn_maximize_restore.setObjectName(u"btn_maximize_restore")
        sizePolicy2.setHeightForWidth(
            self.btn_maximize_restore.sizePolicy().hasHeightForWidth()
        )
        self.btn_maximize_restore.setSizePolicy(sizePolicy2)
        self.btn_maximize_restore.setMinimumSize(QSize(40, 0))
        self.btn_maximize_restore.setMaximumSize(QSize(40, 16777215))
        self.btn_maximize_restore.setStyleSheet(
            u"QPushButton {	\n"
            "	border: none;\n"
            "	background-color: transparent;\n"
            "}\n"
            "QPushButton:hover {\n"
            "	background-color: rgb(52, 59, 72);\n"
            "}\n"
            "QPushButton:pressed {	\n"
            "	background-color: rgb(85, 170, 255);\n"
            "}"
        )
        icon1 = QIcon()
        icon1.addFile(
            u":/16x16/icons/16x16/cil-window-maximize.png",
            QSize(),
            QIcon.Normal,
            QIcon.Off,
        )
        self.btn_maximize_restore.setIcon(icon1)

        self.horizontalLayout_5.addWidget(self.btn_maximize_restore)

        self.btn_close = QPushButton(self.frame_btns_right)
        self.btn_close.setObjectName(u"btn_close")
        sizePolicy2.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy2)
        self.btn_close.setMinimumSize(QSize(40, 0))
        self.btn_close.setMaximumSize(QSize(40, 16777215))
        self.btn_close.setStyleSheet(
            u"QPushButton {	\n"
            "	border: none;\n"
            "	background-color: transparent;\n"
            "}\n"
            "QPushButton:hover {\n"
            "	background-color: rgb(52, 59, 72);\n"
            "}\n"
            "QPushButton:pressed {	\n"
            "	background-color: rgb(85, 170, 255);\n"
            "}"
        )
        icon2 = QIcon()
        icon2.addFile(
            u":/16x16/icons/16x16/cil-x.png", QSize(), QIcon.Normal, QIcon.Off
        )
        self.btn_close.setIcon(icon2)

        self.horizontalLayout_5.addWidget(self.btn_close)

        self.horizontalLayout_4.addWidget(self.frame_btns_right, 0, Qt.AlignRight)

        self.verticalLayout_2.addWidget(self.frame_top_btns)

        # top bar
        self.frame_top_info = QFrame(self.frame_top_right)
        self.frame_top_info.setObjectName(u"frame_top_info")
        self.frame_top_info.setMaximumSize(QSize(16777215, 65))
        self.frame_top_info.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.frame_top_info.setFrameShape(QFrame.NoFrame)
        self.frame_top_info.setFrameShadow(QFrame.Raised)

        # top bar layout
        self.horizontalLayout_8 = QHBoxLayout(self.frame_top_info)
        self.horizontalLayout_8.setSpacing(1)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(10, 0, 10, 0)

        # top bar left
        self.label_top_info_1 = QLabel(self.frame_top_info)
        self.label_top_info_1.setObjectName(u"label_top_info_1")
        self.label_top_info_1.setMaximumSize(QSize(16777215, 15))

        self.label_top_info_1.setFont(self.font2)
        self.label_top_info_1.setStyleSheet(u"color: rgb(98, 103, 111); ")

        # top bar right
        self.label_top_info_2 = QLabel(self.frame_top_info)
        self.label_top_info_2.setObjectName(u"label_top_info_2")
        self.label_top_info_2.setMinimumSize(QSize(0, 0))
        self.label_top_info_2.setMaximumSize(QSize(250, 20))

        self.label_top_info_2.setFont(self.font3)
        self.label_top_info_2.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_top_info_2.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter
        )

        self.horizontalLayout_8.addWidget(self.label_top_info_1)
        self.horizontalLayout_8.addWidget(self.label_top_info_2)

        self.verticalLayout_2.addWidget(self.frame_top_info)

        self.horizontalLayout_3.addWidget(self.frame_top_right)

        self.verticalLayout.addWidget(self.frame_top)

        self.frame_center = QFrame(self.frame_main)
        self.frame_center.setObjectName(u"frame_center")
        sizePolicy.setHeightForWidth(self.frame_center.sizePolicy().hasHeightForWidth())
        self.frame_center.setSizePolicy(sizePolicy)
        self.frame_center.setStyleSheet(u"background-color: rgb(40, 44, 52);")
        self.frame_center.setFrameShape(QFrame.NoFrame)
        self.frame_center.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2 = QHBoxLayout(self.frame_center)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.frame_left_menu = QFrame(self.frame_center)
        self.frame_left_menu.setObjectName(u"frame_left_menu")

        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(
            self.frame_left_menu.sizePolicy().hasHeightForWidth()
        )

        self.frame_left_menu.setSizePolicy(sizePolicy3)
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setLayoutDirection(Qt.LeftToRight)
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_left_menu.setFrameShape(QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)

        self.verticalLayout_5 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_5.setSpacing(1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)

        self.frame_menus = QFrame(self.frame_left_menu)
        self.frame_menus.setObjectName(u"frame_menus")
        self.frame_menus.setFrameShape(QFrame.NoFrame)
        self.frame_menus.setFrameShadow(QFrame.Raised)

        self.layout_menus = QVBoxLayout(self.frame_menus)
        self.layout_menus.setSpacing(0)
        self.layout_menus.setObjectName(u"layout_menus")
        self.layout_menus.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_5.addWidget(self.frame_menus, 0, Qt.AlignTop)

        self.frame_extra_menus = QFrame(self.frame_left_menu)
        self.frame_extra_menus.setObjectName(u"frame_extra_menus")
        sizePolicy3.setHeightForWidth(
            self.frame_extra_menus.sizePolicy().hasHeightForWidth()
        )
        self.frame_extra_menus.setSizePolicy(sizePolicy3)
        self.frame_extra_menus.setFrameShape(QFrame.NoFrame)
        self.frame_extra_menus.setFrameShadow(QFrame.Raised)

        self.layout_menu_bottom = QVBoxLayout(self.frame_extra_menus)
        self.layout_menu_bottom.setSpacing(10)
        self.layout_menu_bottom.setObjectName(u"layout_menu_bottom")
        self.layout_menu_bottom.setContentsMargins(0, 0, 0, 25)

        self.label_user_icon = QLabel(self.frame_extra_menus)
        self.label_user_icon.setObjectName(u"label_user_icon")

        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(
            self.label_user_icon.sizePolicy().hasHeightForWidth()
        )

        self.label_user_icon.setSizePolicy(sizePolicy4)
        self.label_user_icon.setMinimumSize(QSize(60, 60))
        self.label_user_icon.setMaximumSize(QSize(60, 60))

        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(12)

        self.label_user_icon.setFont(font4)
        self.label_user_icon.setStyleSheet(
            u"QLabel {\n"
            "	border-radius: 30px;\n"
            "	background-color: rgb(44, 49, 60);\n"
            "	border: 5px solid rgb(39, 44, 54);\n"
            "	background-position: center;\n"
            "	background-repeat: no-repeat;\n"
            "}"
        )
        self.label_user_icon.setAlignment(Qt.AlignCenter)

        self.layout_menu_bottom.addWidget(self.label_user_icon, 0, Qt.AlignHCenter)

        self.verticalLayout_5.addWidget(self.frame_extra_menus, 0, Qt.AlignBottom)

        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_content_right = QFrame(self.frame_center)
        self.frame_content_right.setObjectName(u"frame_content_right")
        self.frame_content_right.setStyleSheet(u"background-color: rgb(44, 49, 60);")
        self.frame_content_right.setFrameShape(QFrame.NoFrame)
        self.frame_content_right.setFrameShadow(QFrame.Raised)

        self.verticalLayout_4 = QVBoxLayout(self.frame_content_right)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)

        self.frame_content = QFrame(self.frame_content_right)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setFrameShape(QFrame.NoFrame)
        self.frame_content.setFrameShadow(QFrame.Raised)

        self.verticalLayout_9 = QVBoxLayout(self.frame_content)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(5, 5, 5, 5)

        self.stackedWidget = QStackedWidget(self.frame_content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")

        self.createPages(MainWindow)

        self.setTabOrder(MainWindow)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        # set Names for Ui Elements

        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", u"EVE TTS", None)
        )
        self.btn_toggle_menu.setText("")
        self.label_title_bar_top.setText(
            QCoreApplication.translate("MainWindow", u"EVE TTS", None)
        )
        self.btn_minimize.setToolTip(
            QCoreApplication.translate("MainWindow", u"Minimize", None)
        )
        self.btn_minimize.setText("")
        self.btn_maximize_restore.setToolTip(
            QCoreApplication.translate("MainWindow", u"Maximize", None)
        )
        self.btn_maximize_restore.setText("")
        self.btn_close.setToolTip(
            QCoreApplication.translate("MainWindow", u"Close", None)
        )
        self.btn_close.setText("")

        self.btn_clearHistory.setToolTip(
            QCoreApplication.translate("MainWindow", u"Clear History", None)
        )
        self.btn_clearHistory.setText("Clear History")

        self.btn_startTTS.setToolTip(
            QCoreApplication.translate("MainWindow", u"Start TTS", None)
        )
        self.btn_startTTS.setText("Start TTS")

        self.btn_stopTTS.setToolTip(
            QCoreApplication.translate("MainWindow", u"Stop TTS", None)
        )
        self.btn_stopTTS.setText("Stop TTS")

        self.label_top_info_1.setText(
            QCoreApplication.translate("MainWindow", u"TEXT-TO-SPEECH", None)
        )
        self.label_top_info_2.setText(
            QCoreApplication.translate("MainWindow", u"| HOME", None)
        )

        # Main Page
        self.label_home_headline.setText(
            QCoreApplication.translate("MainWindow", u"Welcome to Eve TTS", None)
        )
        self.label_home_center.setText(
            QCoreApplication.translate(
                "MainWindow",
                u"Head to the settings page first to add \n the characters you want to listen for and the channels \n that should be checked ",
                None,
            )
        )
        self.label_home_bottom.setText(
            QCoreApplication.translate(
                "MainWindow",
                u'<a href="https://github.com/Daholli/EveTTS"> <font color=grey> https://github.com/Daholli/EveTTS </font> </a>',
                None,
            )
        )

        # Settings Page
        if len(tts.settings["characterNames"]) == 0:
            self.lineEdit1.setPlaceholderText(
                QCoreApplication.translate(
                    "MainWindow", u"Character Names (seperated by ',')", None
                )
            )
        else:
            self.lineEdit1.setText(",".join(tts.settings["characterNames"]))

        if len(tts.settings["characterNames"]) == 0:
            self.lineEdit2.setPlaceholderText(
                QCoreApplication.translate(
                    "MainWindow", u"Channel Names (seperated by ',')", None
                )
            )
        else:
            self.lineEdit2.setText(",".join(tts.settings["channelNames"]))

        self.settings_div1_label.setText(
            QCoreApplication.translate("MainWindow", u"Main Configuration", None)
        )

        self.label_credits.setText(
            QCoreApplication.translate(
                "MainWindow", u"Registered by: Christoph Hollizeck", None
            )
        )
        self.label_version.setText(
            QCoreApplication.translate("MainWindow", u"v0.4-beta", None)
        )

    def addFonts(self):
        # font1
        self.font1 = QFont()
        self.font1.setFamily(u"Segoe UI")
        self.font1.setPointSize(10)
        self.font1.setBold(True)
        self.font1.setWeight(75)

        # font2
        self.font2 = QFont()
        self.font2.setFamily(u"Segoe UI")

        # font 3
        self.font3 = QFont()
        self.font3.setFamily(u"Segoe UI")
        self.font3.setBold(True)
        self.font3.setWeight(75)

        # Size 40
        self.font5 = QFont()
        self.font5.setFamily(u"Segoe UI")
        self.font5.setPointSize(40)

        # Size 14
        self.font6 = QFont()
        self.font6.setFamily(u"Segoe UI")
        self.font6.setPointSize(14)

        # Size 15
        self.font7 = QFont()
        self.font7.setFamily(u"Segoe UI")
        self.font7.setPointSize(15)

        # Size 9
        self.font8 = QFont()
        self.font8.setFamily(u"Segoe UI")
        self.font8.setPointSize(9)

    def createPageHome(self):
        # create Widget for Page
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")

        # Set Main Layout
        self.page_layout_home = QVBoxLayout(self.page_home)
        self.page_layout_home.setObjectName(u"page_layout_home")

        self.label_home_headline = QLabel(self.page_home)
        self.label_home_headline.setObjectName(u"label_home_headline")
        self.label_home_headline.setFont(self.font5)
        self.label_home_headline.setStyleSheet(u"")
        self.label_home_headline.setAlignment(Qt.AlignCenter)

        self.label_home_center = QLabel(self.page_home)
        self.label_home_center.setObjectName(u"label_home_center")
        self.label_home_center.setFont(self.font6)
        self.label_home_center.setAlignment(Qt.AlignCenter)

        self.label_home_bottom = QLabel(self.page_home)
        self.label_home_bottom.setObjectName(u"label_home_bottom")
        self.label_home_bottom.setFont(self.font7)
        self.label_home_bottom.setAlignment(Qt.AlignCenter)
        self.label_home_bottom.setOpenExternalLinks(True)

        self.page_layout_home.addWidget(self.label_home_headline)
        self.page_layout_home.addWidget(self.label_home_center)
        self.page_layout_home.addWidget(self.label_home_bottom)

        self.stackedWidget.addWidget(self.page_home)

    def createPageTTS(self):
        self.page_tts = QWidget()
        self.page_tts.setObjectName(u"page_tts")

        # Set Main Layout
        self.page_layout_tts = QVBoxLayout(self.page_tts)
        self.page_layout_tts.setObjectName(u"page_layout_tts")

        self.tts_box = QFrame(self.page_tts)
        self.tts_box.setObjectName(u"tts_box")
        self.tts_box.setStyleSheet(u"border-radius: 5px;")
        self.tts_box.setFrameShape(QFrame.StyledPanel)
        self.tts_box.setFrameShadow(QFrame.Raised)

        self.tts_main_layout = QVBoxLayout(self.tts_box)
        self.tts_main_layout.setObjectName(u"tts_main_layout")

        self.tts_chatbox_frame = QFrame(self.tts_box)
        self.tts_chatbox_frame.setObjectName(u"tts_chatbox_frame")
        self.tts_chatbox_frame.setMinimumSize(QSize(0, 220))
        self.tts_chatbox_frame.setStyleSheet(
            u"background-color: rgb(41, 45, 56);\n" "border-radius: 5px;\n" ""  # 41
        )
        self.tts_chatbox_frame.setFrameShape(QFrame.NoFrame)
        self.tts_chatbox_frame.setFrameShadow(QFrame.Raised)

        self.chatHistory_grid = QGridLayout()
        self.chatHistory_grid.setObjectName(u"chatHistory_grid")
        self.chatHistory_grid.setSpacing(1)
        self.chatHistory_grid.setContentsMargins(-1, -1, -1, 0)

        self.chatHistory = QTextEdit(self.tts_chatbox_frame)
        self.chatHistory.setObjectName(u"chatHistory")
        self.chatHistory.setReadOnly(True)
        self.chatHistory.setFont(self.font6)

        self.chatHistory_hbox = QHBoxLayout(self.tts_chatbox_frame)
        self.chatHistory_hbox.setObjectName(u"tts_buttonlayout")

        self.btn_clearHistory = QPushButton(self.tts_chatbox_frame)
        self.btn_clearHistory.setObjectName(u"btn_clearHistory")
        self.btn_clearHistory.setMinimumSize(QSize(120, 30))
        self.btn_clearHistory.setMaximumSize(QSize(120, 30))
        self.btn_clearHistory.setFont(self.font2)

        self.btn_clearHistory.setStyleSheet(
            u"QPushButton {\n"
            "	border: 2px solid rgb(52, 59, 72);\n"
            "	border-radius: 5px;	\n"
            "	background-color: rgb(52, 59, 72);\n"
            "}\n"
            "QPushButton:hover {\n"
            "	background-color: rgb(57, 65, 80);\n"
            "	border: 2px solid rgb(61, 70, 86);\n"
            "}\n"
            "QPushButton:pressed {	\n"
            "	background-color: rgb(35, 40, 49);\n"
            "	border: 2px solid rgb(43, 50, 61);\n"
            "}"
        )
        self.btn_clearHistory.clicked.connect(self.clearChatHistory)

        self.btn_startTTS = QPushButton(self.tts_chatbox_frame)
        self.btn_startTTS.setObjectName(u"btn_startTTS")
        self.btn_startTTS.setMinimumSize(QSize(120, 30))
        self.btn_startTTS.setMaximumSize(QSize(120, 30))
        self.btn_startTTS.setFont(self.font2)

        self.btn_startTTS.setStyleSheet(
            u"QPushButton {\n"
            "	border: 2px solid rgb(52, 59, 72);\n"
            "	border-radius: 5px;	\n"
            "	background-color: rgb(52, 59, 72);\n"
            "}\n"
            "QPushButton:hover {\n"
            "	background-color: rgb(57, 65, 80);\n"
            "	border: 2px solid rgb(61, 70, 86);\n"
            "}\n"
            "QPushButton:pressed {	\n"
            "	background-color: rgb(35, 40, 49);\n"
            "	border: 2px solid rgb(43, 50, 61);\n"
            "}"
        )
        self.btn_startTTS.clicked.connect(self.startTTS)

        self.btn_stopTTS = QPushButton(self.tts_chatbox_frame)
        self.btn_stopTTS.setObjectName(u"btn_startTTS")
        self.btn_stopTTS.setMinimumSize(QSize(120, 30))
        self.btn_stopTTS.setMaximumSize(QSize(120, 30))
        self.btn_stopTTS.setFont(self.font2)

        self.btn_stopTTS.setStyleSheet(
            u"QPushButton {\n"
            "	border: 2px solid rgb(52, 59, 72);\n"
            "	border-radius: 5px;	\n"
            "	background-color: rgb(52, 59, 72);\n"
            "}\n"
            "QPushButton:hover {\n"
            "	background-color: rgb(57, 65, 80);\n"
            "	border: 2px solid rgb(61, 70, 86);\n"
            "}\n"
            "QPushButton:pressed {	\n"
            "	background-color: rgb(35, 40, 49);\n"
            "	border: 2px solid rgb(43, 50, 61);\n"
            "}"
        )
        self.btn_stopTTS.clicked.connect(self.stopTTS)

        self.chatHistory_grid.addWidget(self.chatHistory, 0, 0, 1, 5)
        self.chatHistory_grid.addWidget(self.btn_clearHistory, 2, 0)
        self.chatHistory_grid.addWidget(self.btn_startTTS, 2, 4)
        self.chatHistory_grid.addWidget(self.btn_stopTTS, 2, 5)

        self.chatHistory_hbox.addLayout(self.chatHistory_grid)

        self.tts_main_layout.addWidget(self.tts_chatbox_frame)
        self.page_layout_tts.addWidget(self.tts_box)
        self.stackedWidget.addWidget(self.page_tts)

    def createPageSettings(self):
        self.page_settings = QWidget()
        self.page_settings.setObjectName(u"page_settings")

        # Set Main Layout
        self.page_layout_settings = QVBoxLayout(self.page_settings)
        self.page_layout_settings.setObjectName(u"page_layout_tts")

        self.settings_box = QFrame(self.page_settings)
        self.settings_box.setObjectName(u"settings_box")
        self.settings_box.setStyleSheet(u"border-radius: 5px;")
        self.settings_box.setFrameShape(QFrame.StyledPanel)
        self.settings_box.setFrameShadow(QFrame.Raised)

        self.settings_main_layout = QVBoxLayout(self.settings_box)
        self.settings_main_layout.setSpacing(10)
        self.settings_main_layout.setObjectName(u"settings_main_layout")
        self.settings_main_layout.setContentsMargins(0, 0, 0, 0)

        self.settings_div1 = QFrame(self.settings_box)
        self.settings_div1.setObjectName(u"settings_div1")
        self.settings_div1.setMinimumSize(QSize(0, 110))
        self.settings_div1.setMaximumSize(QSize(16777215, 160))
        self.settings_div1.setStyleSheet(
            u"background-color: rgb(41, 45, 56);\n" "border-radius: 5px;\n" ""  # 41
        )
        self.settings_div1.setFrameShape(QFrame.NoFrame)
        self.settings_div1.setFrameShadow(QFrame.Raised)

        # create Darker Box at the top
        self.settings_div1_titlebox = QVBoxLayout(self.settings_div1)
        self.settings_div1_titlebox.setSpacing(2)
        self.settings_div1_titlebox.setObjectName(u"settings_div1_titlebox")
        self.settings_div1_titlebox.setContentsMargins(0, 0, 0, 0)

        self.settings_div1_title = QFrame(self.settings_div1)
        self.settings_div1_title.setObjectName(u"settings_div1_title")
        self.settings_div1_title.setMaximumSize(QSize(16777215, 35))
        self.settings_div1_title.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.settings_div1_title.setFrameShape(QFrame.StyledPanel)
        self.settings_div1_title.setFrameShadow(QFrame.Raised)

        self.settings_div1_label_layout = QVBoxLayout(self.settings_div1_title)
        self.settings_div1_label_layout.setObjectName(u"settings_div1_label_layout")

        # add text to darker Box
        self.settings_div1_label = QLabel(self.settings_div1_title)
        self.settings_div1_label.setObjectName(u"settings_div1_label")
        self.settings_div1_label.setFont(self.font1)
        self.settings_div1_label.setStyleSheet(u"")

        self.settings_div1_label_layout.addWidget(self.settings_div1_label)
        self.settings_div1_titlebox.addWidget(self.settings_div1_title)

        # creating Box for content

        self.frame_content_wid_1 = QFrame(self.settings_div1)
        self.frame_content_wid_1.setObjectName(u"frame_content_wid_1")
        self.frame_content_wid_1.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_1.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_9 = QHBoxLayout(self.frame_content_wid_1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")

        # GridLayout for Text Boxes

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSpacing(1)
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)

        # add text fields for grid
        self.lineEdit1 = QLineEdit(self.frame_content_wid_1)
        self.lineEdit1.setObjectName(u"lineEdit1")
        self.lineEdit1.setMinimumSize(QSize(0, 30))
        self.lineEdit1.setStyleSheet(
            u"QLineEdit {\n"
            "	background-color: rgb(27, 29, 35);\n"
            "	border-radius: 5px;\n"
            "	border: 2px solid rgb(27, 29, 35);\n"
            "	padding-left: 10px;\n"
            "}\n"
            "QLineEdit:hover {\n"
            "	border: 2px solid rgb(64, 71, 88);\n"
            "}\n"
            "QLineEdit:focus {\n"
            "	border: 2px solid rgb(91, 101, 124);\n"
            "}"
        )

        self.lineEdit2 = QLineEdit(self.frame_content_wid_1)
        self.lineEdit2.setObjectName(u"lineEdit2")
        self.lineEdit2.setMinimumSize(QSize(0, 30))
        self.lineEdit2.setStyleSheet(
            u"QLineEdit {\n"
            "	background-color: rgb(27, 29, 35);\n"
            "	border-radius: 5px;\n"
            "	border: 2px solid rgb(27, 29, 35);\n"
            "	padding-left: 10px;\n"
            "}\n"
            "QLineEdit:hover {\n"
            "	border: 2px solid rgb(64, 71, 88);\n"
            "}\n"
            "QLineEdit:focus {\n"
            "	border: 2px solid rgb(91, 101, 124);\n"
            "}"
        )

        self.volumeSlider = QSlider(self.frame_content_wid_1)
        self.volumeSlider.setObjectName(u"volumeSlider")
        self.volumeSlider.setStyleSheet(u"")
        self.volumeSlider.setOrientation(Qt.Horizontal)
        self.volumeSlider.setValue(tts.settings["tts_volume"])
        self.volumeSlider.valueChanged.connect(self.volumeSliderMoved)

        self.volumeDisplay = QLabel("Volume: {}".format(tts.settings["tts_volume"]))
        self.volumeDisplay.setMinimumWidth(100)
        self.volumeDisplay.setFont(self.font7)

        self.rateSlider = QSlider(self.frame_content_wid_1)
        self.rateSlider.setObjectName(u"rateSlider")
        self.rateSlider.setStyleSheet(u"")
        self.rateSlider.setOrientation(Qt.Horizontal)
        self.rateSlider.setRange(0, 200)
        self.rateSlider.setValue(tts.settings["tts_rate"])
        self.rateSlider.valueChanged.connect(self.rateSliderMoved)

        self.rateDisplay = QLabel("Rate: {}".format(tts.settings["tts_rate"]))
        self.rateDisplay.setMinimumWidth(100)
        self.rateDisplay.setFont(self.font7)

        self.gridLayout.addWidget(self.lineEdit1, 0, 0, 1, 2)
        self.gridLayout.addWidget(self.lineEdit2, 0, 2, 1, 2)
        self.gridLayout.addWidget(self.volumeSlider, 2, 0)
        self.gridLayout.addWidget(self.volumeDisplay, 2, 1)
        self.gridLayout.addWidget(self.rateSlider, 2, 2)
        self.gridLayout.addWidget(self.rateDisplay, 2, 3)

        self.horizontalLayout_9.addLayout(self.gridLayout)

        self.settings_div1_titlebox.addWidget(self.frame_content_wid_1)
        self.settings_main_layout.addWidget(self.settings_div1)

        self.page_layout_settings.addWidget(self.settings_box)
        self.stackedWidget.addWidget(self.page_settings)

    def createBottomWindowBoarder(self, MainWindow):
        self.frame_grip = QFrame(self.frame_content_right)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setMinimumSize(QSize(0, 25))
        self.frame_grip.setMaximumSize(QSize(16777215, 25))
        self.frame_grip.setStyleSheet(u"background-color: rgb(35, 37, 43);")
        self.frame_grip.setFrameShape(QFrame.NoFrame)
        self.frame_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6 = QHBoxLayout(self.frame_grip)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 2, 0)
        self.frame_label_bottom = QFrame(self.frame_grip)
        self.verticalLayout_9.addWidget(self.stackedWidget)
        self.verticalLayout_4.addWidget(self.frame_content)

        self.frame_label_bottom.setObjectName(u"frame_label_bottom")
        self.frame_label_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_label_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_label_bottom)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 0, 10, 0)
        self.label_credits = QLabel(self.frame_label_bottom)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setFont(self.font2)
        self.label_credits.setStyleSheet(u"color: rgb(98, 103, 111);")

        self.horizontalLayout_7.addWidget(self.label_credits)

        self.label_version = QLabel(self.frame_label_bottom)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setMaximumSize(QSize(100, 16777215))
        self.label_version.setFont(self.font2)
        self.label_version.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_version.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter
        )

        self.horizontalLayout_7.addWidget(self.label_version)

        self.horizontalLayout_6.addWidget(self.frame_label_bottom)

        self.frame_size_grip = QFrame(self.frame_grip)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMaximumSize(QSize(20, 20))
        self.frame_size_grip.setStyleSheet(
            u"QSizeGrip {\n"
            "	background-image: url(:/16x16/icons/16x16/cil-size-grip.png);\n"
            "	background-position: center;\n"
            "	background-repeat: no-reperat;\n"
            "}"
        )
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.frame_size_grip)
        self.verticalLayout_4.addWidget(self.frame_grip)
        self.horizontalLayout_2.addWidget(self.frame_content_right)
        self.verticalLayout.addWidget(self.frame_center)
        self.horizontalLayout.addWidget(self.frame_main)

        MainWindow.setCentralWidget(self.centralwidget)

        self.labelVersion_3 = QLabel(self.frame_content_wid_1)
        self.labelVersion_3.setObjectName(u"labelVersion_3")
        self.labelVersion_3.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.labelVersion_3.setLineWidth(1)
        self.labelVersion_3.setAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter
        )

        self.gridLayout.addWidget(self.labelVersion_3, 1, 0, 1, 2)

    def volumeSliderMoved(self, value):
        self.volumeDisplay.setText("Volume: {}".format(value))
        tts.settings["tts_volume"] = value

    def rateSliderMoved(self, value):
        self.rateDisplay.setText("Rate: {}".format(value))
        tts.settings["tts_rate"] = value

    def createPages(self, MainWindow):

        # initialize Pages
        self.createPageHome()
        self.createPageTTS()
        self.createPageSettings()

        # render border for every page
        self.createBottomWindowBoarder(MainWindow)

        # self.pushButton = QPushButton(self.frame_content_wid_1)
        # self.pushButton.setObjectName(u"pushButton")
        # self.pushButton.setMinimumSize(QSize(150, 30))

    def setTabOrder(self, MainWindow):
        QWidget.setTabOrder(self.btn_minimize, self.btn_maximize_restore)
        QWidget.setTabOrder(self.btn_maximize_restore, self.btn_close)
        QWidget.setTabOrder(self.btn_close, self.btn_toggle_menu)

    def startTTS(self):
        if tts.settings["tts_enabled"]:
            return

        self.updateChatHistory()
        self.saveConfig()

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

        self.thread.start()

    def stopTTS(self):
        tts.settings["tts_enabled"] = False

    def clearChatHistory(self):
        tts.chatHistory = ["Booting up TTS..."]
        self.stopTTS()
        self.updateChatHistory()

    def updateChatHistory(self):
        self.chatHistory.setText("\n".join(tts.chatHistory))

    def saveConfig(self):
        self.stopTTS()
        tts.settings["channelNames"] = self.lineEdit2.text().split(",")
        tts.settings["characterNames"] = self.lineEdit1.text().split(",")
        tts.saveConfig()
